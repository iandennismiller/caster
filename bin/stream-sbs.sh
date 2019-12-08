#!/bin/bash

ffmpeg \
    -i http://127.0.0.1:8081/ \
    -vf stereo3d=al:sbsl \
    http://localhost:1234/feed1.ffm
