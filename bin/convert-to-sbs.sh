#!/bin/bash

ffmpeg -i 2D.mp4 -filter_complex \
   '[0]scale=iw*sar:ih,setsar=1,scale=-1:$720,\
    crop=$720:$720,split[left][right]; \
    [left][right]hstack[sbs]' -map "[sbs]" -map 0:a? SBS.mp4

# https://trac.ffmpeg.org/wiki/Stereoscopic
# -vf stereo3d=sbs2l:abl
