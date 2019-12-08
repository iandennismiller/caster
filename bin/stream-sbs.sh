#!/bin/bash

ffmpeg \
    -i http://127.0.0.1:8081/ \
    -vf stereo3d=sbs2l:abl \
    -tune zerolatency \
    -crf 18 \
    http://localhost:1234/feed1.ffm
