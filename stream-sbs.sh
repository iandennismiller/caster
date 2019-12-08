#!/bin/bash

ffmpeg \
    -i 'http://10.0.1.9:8081/' \
    -vf stereo3d=sbs2l:abl \
    -f rtsp \
    -tune zerolatency \
    -rtsp_transport tcp \
    -muxdelay 0.1 \
    'rtsp://0.0.0.0:8544/'

# ffmpeg \
#     -i 'rtsp://10.0.1.9:8554/' \
#     -vf stereo3d=sbs2l:abl \
#     -f rtsp \
#     -rtsp_transport tcp \
#     out.mp4

    # rtsp://0.0.0.0:8544/

# https://trac.ffmpeg.org/wiki/Stereoscopic
