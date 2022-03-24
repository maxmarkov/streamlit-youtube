import streamlit as st
import requests
from pytube import YouTube, StreamQuery

# https://www.youtube.com/watch?v=Ch5VhJzaoaI&list=LL&index=39&t=90s

def clear_text():
    st.session_state["url"] = ""

def download_file(stream):
    stream.download(output_path='./')

def can_access(url):
    """ check whether you can access the video """
    access = False
    if len(url) > 0:
        try:
            tube = YouTube(url)
            if tube.check_availability() is None:
                access=True
        except:
            pass
    return access

st.set_page_config(page_title=" Youtube downloader", layout="wide")

# ====== SIDEBAR ======
with st.sidebar:

    st.title("Youtube download app")

    url = st.text_input("Insert your link here", key="url")

    fmt = st.selectbox("Choose format:", ['video', 'audio'], key='fmt')

    if can_access(url):

        tube = YouTube(url)

        streams_fmt = [t for t in tube.streams if t.type==fmt]

        # === StreamQuery Object === #
        mime_types = set([t.mime_type for t in streams_fmt])
        mime_type = st.selectbox("Mime types:", mime_types, key='mime')

        streams_mime = StreamQuery(streams_fmt).filter(mime_type=mime_type)

        # quality is average bitrate for audio and resolution for video
        if fmt=='audio':
            quality = set([t.abr for t in streams_mime])
            quality_type = st.selectbox('Choose average bitrate: ', quality, key='quality')
            stream_quality = StreamQuery(streams_mime).filter(abr=quality_type)
        elif fmt=='video':
            quality = set([t.resolution for t in streams_mime])
            quality_type = st.selectbox('Choose resolution: ', quality, key='quality')
            stream_quality = StreamQuery(streams_mime).filter(res=quality_type)
            
        stream_final = stream_quality[0]#st.selectbox("Final choice:", stream_quality)

        download = st.button("Download file", key='download')
        if len(stream_quality) > 0 and download:
            download_file(stream_final)
            st.balloons()

        st.button("Clear all address boxes", on_click=clear_text)

        st.info(
            "This is an open source project and you are very welcome to contribute your "
            "comments, questions, resources and apps as "
            "[issues](https://github.com/maxmarkov/streamlit-youtube/issues) or "
            "[pull requests](https://github.com/maxmarkov/streamlit-youtube/pulls) "
            "to the [source code](https://github.com/maxmarkov/streamlit-youtube). "
        )




# ====== MAIN PAGE ======

if can_access(url):
    st.video(url)

#if len(url) > 0 and requests.get(url).status_code!=200:
#    st.write(requests.get(url))
