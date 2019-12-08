#!/bin/bash

vlc \
    playlist.m3u \
    -I dummy \
    --http-host=0.0.0.0 \
    --sout-livehttp-caching \
    --sout-keep \
    --sout '#transcode{vcodec=h264,vb=800,scale=1,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=0}:standard{mux=ts,dst="0.0.0.0:8081",access=http}'

# vlc http://localhost:8080

