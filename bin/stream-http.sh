#!/bin/bash

vlc \
    etc/playlist.m3u \
    -I dummy \
    --extraintf=http \
    --http-host=0.0.0.0 \
    --http-port=8080 \
    --http-password=vlc \
    --sout-livehttp-caching \
    --sout-keep \
    --sout '#transcode{vcodec=h264,vb=800,scale=1,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=0}:standard{mux=ts,dst="0.0.0.0:8081",access=http}'

# sudo ufw allow 8081
# sudo ufw allow 8080
# vlc http://localhost:8080

