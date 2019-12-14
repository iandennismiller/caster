#!/bin/bash

if [[ -z $1 || -z $2 ]]; then
    echo "convert-to-sbs.sh INPUT OUTPUT"
    exit
fi

WIDTH=$(ffprobe -v error -show_entries stream=width -of csv=s=x:p=0 $1)
HEIGHT=$(ffprobe -v error -show_entries stream=height -of csv=s=x:p=0 $1)

ffmpeg \
    -i "$1" \
    -filter:v "scale=-1:720,crop=640:720,stereo3d=al:sbsl" \
    "$2"
