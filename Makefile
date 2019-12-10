curate:
	bin/curate-playlist.py

requirements:
	pip install -r etc/requirements.txt

rtsp:
	bin/stream-http.sh

ffserver:
	ffserver -f etc/ffserver.config

http:
	bin/stream-http.sh

sbs:
	bin/stream-sbs.sh

.PHONY: ffserver http sbs rtsp curate requirements
