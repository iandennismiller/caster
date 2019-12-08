#!/bin/bash

if [ -z $1 || -z $2 ]; then
    echo "convert-to-sbs.sh INPUT OUTPUT"
    exit
fi

ffmpeg \
    -i "$1" \
    -vf stereo3d=al:sbsl \
    "$2"
