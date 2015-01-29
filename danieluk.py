import subprocess
import datetime
import random
import socket
from flask import *
app = Flask(__name__)

LOGFILE = "/Users/ahogue/gags.txt"
GAGS = ("Thanks for meming",
        "Your meme status has been updated from: memeduke to: memelord",
        "ERROR 420: Request body did not contain enough memes",
        "lol",
        "top kek",
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
        "Exit status 420",
        "<a href=\"http://gabegaming.com\">[HOT] CLICK HERE FOR MEMES [HOT]</a>",
        "Thanks for visiting Mr. Magorium's Meme Emporium. More memes, more value.",
        "[INFO] [talledLocalContainer] Gag recieved"

)


@app.route("/say", methods=["POST"])
def say():
    if not socket.gethostbyname("briosa") == request.remote_addr:
        return "Sorry based employees only"
    subprocess.call(["say", request.form["message"]])
    with open(LOGFILE, 'a') as f:
        f.write(str(datetime.datetime.now()) + "\t" + request.form["message"] + "\n");

    return random.choice(GAGS)

app.run(host="0.0.0.0")
