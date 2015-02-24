import subprocess
import datetime
import random
import socket
from flask import *
app = Flask(__name__)

LOGFILE = "recieved_gags.txt"
WHITELISTFILE = "whitelist.txt"

# Switch to True to send a random gag in response to each request.
ENABLE_GAGS = False

GAGS = ("Thanks for meming",
        "Your meme status has been updated from: memeduke to: memelord",
        "ERROR 420: Request body clearly copypasta from /b/",
        """
        __________
        < ayy lmao >
         ----------
                \   ^__^
                 \  (oo)\_______
                    (__)\       )\/
                        ||----w |
                        ||     ||""",
        "Thank you for working with heart and balance",
        "Congratulations, you have now played as a meme",
        "ERROR 421: Request did not come from the Bay Area",
        "<a href=\"http://gabegaming.com\">[HOT] CLICK HERE FOR MEMES [HOT]</a>",
        "Thanks for visiting Mr. Magorium's Meme Emporium. More memes, more value."
)


with open(WHITELISTFILE) as f:
    allowed_ldaps = [line.strip() for line in f.readlines() if not line.startswith("#")]

@app.route("/say", methods=["POST"])
def say():
    # Get rekt by glibc vulnerability.
    if not any(socket.gethostbyname(ldap) == request.remote_addr for ldap in allowed_ldaps):
        return "Sorry based employees only"

    subprocess.call(["say", request.form["message"]])
    with open(LOGFILE, 'a') as f:
        # TODO log hostname as well.
        f.write("\t".join(str(datetime.datetime.now()), str(request.remote_addr), request.form["message"]))
        f.write("\n")

    if ENABLE_GAGS:
        return random.choice(GAGS)
    return "Gag recieved."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5699)
