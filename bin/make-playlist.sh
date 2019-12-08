#!/bin/bash

echo '#EXTM3U' > playlist.m3u
find . -iname '*.mp4' -type f >> playlist.m3u
