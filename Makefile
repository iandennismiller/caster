rtsp:
	bin/stream-rtsp.sh

ffserver:
	ffserver -f etc/ffserver.config

http:
	bin/stream-http.sh

sbs:
	bin/stream-sbs.sh

.PHONY: ffserver http sbs rtsp
