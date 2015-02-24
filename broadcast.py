import requests
import sys

import danieluk

with open(danieluk.WHITELISTFILE) as f:
    memers = [line.strip() for line in f.readlines() if not line.startswith("#")]
    data = {
        "message" : sys.stdin.read()
    }
    for memer in memers:
        try:
            requests.post("http://%s:5699/say" % memer, data=data)
        # yolo
        except Exception:
            print "Memecast not heard by: %s" % memer


