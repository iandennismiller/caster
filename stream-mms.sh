#!/bin/bash

/usr/local/bin/vlc \
    playlist.m3u \
    -I dummy \
    --http-host=0.0.0.0 \
    --sout-keep \
    --sout '#transcode{vcodec=h264,vb=800,scale=1,acodec=mp3,ab=32,channels=2}:std{access=mmsh,mux=asfh,dst=:8081}'

# vlc mmsh://localhost:8081
