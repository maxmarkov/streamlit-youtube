# Youtube download app

Download your favorite youtube video on your local PC.

## Docker

Build a docker container
```
./docker/docker_build.sh
```

Launch the docker container
```
./docker/docker_run.sh
```

Copy network URL into you browser

## Local 
Install all requirements
```
pip install -r requirements.txt
```
Launch the app
```
streamlit run app.py
```

Copy network URL into you browser

## Core libraries

- [Streamlit](https://streamlit.io/) to build an app.
- [Pytube](https://pytube.io/en/latest/index.html) to download a video/audio file.
