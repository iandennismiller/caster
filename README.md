# caster

```
HOST=127.0.0.1
rtsp://$HOST:8554/
http://$HOST:8080/
```

```
ffmpeg -i space.mp4 -vcodec libx264 -tune zerolatency -crf 18 http://localhost:1234/feed1.ffm
```

rtsp://127.0.0.1:8554/test1.sdp
