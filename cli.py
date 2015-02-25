import requests
import sys

ONLINE_TIMEOUT = 1
import danieluk

with open(danieluk.WHITELISTFILE) as f:
    memers = [line.strip() for line in f.readlines() if not line.startswith("#")]

def online(user=None):
    if user is None:
        users = memers
    else:
        users = [user]
    online_memers = []
    for memer in users:
        try:
            if requests.get("http://%s:5699/online" % memer, timeout=ONLINE_TIMEOUT).status_code == 200:
                online_memers.append(memer)
        except requests.exceptions.ConnectionError:
            pass

    if user is not None:
        if online_memers and online_memers[0] == user:
            print "Yep"
        else:
            print "Nope"
    else:
        print "\n".join(online_memers)

def say(to, msg):
    data = {
        "message" : msg
    }
    try:
        r = requests.post("http://%s:5699/say" % to, data=data)
        print r.text
    except requests.exceptions.ConnectionError:
        print "m8 %s isn't online hey" % to

def broadcast(msg):
    for memer in memers:
        say(memer, msg)

def help():
    print """
    how 2 be a memer - a brief guide
    
    Commands:
        say <hostname> <message> - Send a text-to-speech message to the hostname
        online [user] - Display people on your whitelist who are currently running the danieluk server, or check a particular person instead
        broadcast <message> - Send a message to everyone on your whitelist.
        help - Display this help

    Press CTRL + C to exit.
    """

def error():
    print "u wot m8"

def do_action(cmd):
    if not cmd:
        print "m8 type something ay"
        return

    parts = cmd.split()
    if parts[0] == "online" and len(parts) <= 2:
        online(parts[1] if len(parts) == 2 else None)
    elif parts[0] == "say" and len(parts) == 3:
        say(parts[1], parts[2])
    elif parts[0] == "broadcast" and len(parts) == 2:
        broadcast(parts[1])
    elif parts[0] == "help" and len(parts) == 1:
        help()
    else:
        error()


def cli():
    try:
        help()
        while True:
            do_action(raw_input("> "))
            print
    except KeyboardInterrupt:
        print
        print "l8r nerd"

if __name__ == "__main__":
    cli()
