#!/bin/bash

/usr/local/bin/vlc \
    playlist.m3u \
    -I dummy \
    --http-host=0.0.0.0 \
    --sout-keep \
    --sout='#wall{rows=1,cols=2}:transcode{vcodec=h264,vb=800,scale=1,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=0}:gather:rtp{sdp=rtsp://:8554,mux=ts}'

# vlc rtsp://localhost:8554/
