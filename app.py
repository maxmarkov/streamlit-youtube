import streamlit as st
import requests
from pytube import YouTube

# https://www.youtube.com/watch?v=Ch5VhJzaoaI&list=LL&index=39&t=90s

def clear_text():
    st.session_state["url"] = ""

def download(stream):
    stream.download(output_path='./')

def can_access(url):
    """ check whether you can access the video"""
    access = False
    if len(url) > 0 and requests.get(url).status_code==200:
        try:
            tube = YouTube(url)
            #tubecheck_availability() -> must be None or empty
            access=True
        except:
            pass
    return access


st.set_page_config(page_title=" Youtube downloader", layout="wide")

# ====== SIDEBAR ======
with st.sidebar:

    st.title("Youtube download app")

    url = st.text_input("Insert your link here", key="url")

    if can_access(url):

        tube = YouTube(url)

        fmt = st.selectbox("Choose format:", ['audio', 'video'])

        # === StreamQuery Object === #
        mime_types = set([t.mime_type for t in tube.streams if t.type==fmt])
        if len(mime_types)>0:
            mime_type = st.selectbox("Mime types:", mime_types)

            if fmt=='audio':
                quality = set([t.abr for t in tube.streams if t.type==fmt and t.mime_type==mime_type])
            elif fmt=='video':
                quality = set([t.resolution for t in tube.streams if t.type==fmt and t.mime_type==mime_type])
            
            if len(quality) > 0:
                mt = st.selectbox("Choose quality:", quality)

                if len(mt) > 0:
                    st.write('AAA')
                    if fmt=='audio':
                        stream = [t for t in tube.streams if t.type==fmt and t.mime_type==mime_type and t.abr==mt]
                        st.write(stream)
                    elif fmt=='video':
                        stream = [t for t in tube.streams if t.type==fmt and t.mime_type==mime_type and t.resolution==mt]
                        st.write(stream)

                    if len(stream) > 0:
                        st.button("Download file", on_click=download(stream[0]))


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
