#!/bin/bash
docker run -it --rm -p 8501:8501 -v $PWD:/home --name=app tubeapp
