#!/bin/bash

vlc \
    playlist.m3u \
    -I dummy \
    --extraintf=http \
    --http-host=0.0.0.0 \
    --http-port=8080 \
    --http-password=vlc \
    --sout-keep \
    --sout='#transcode{vcodec=h264,vb=800,rate=20,scale=1,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=0}:gather:rtp{sdp=rtsp://:8554,mux=ts}'

# sudo ufw allow 8554
# sudo ufw allow 8080
# vlc rtsp://localhost:8554/
