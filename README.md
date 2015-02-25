Remote Gag Execution
==========

Runs a webserver on your machine, people you allow can POST text to it, which is read aloud via text-to-speech on your machine.


Usage
--------
    git clone https://github.com/defaultnamehere/danieluk.git`

    chmod +x setup.sh start.sh

    ./setup.sh

    ./start.sh


To send messages, check online status, and send broadcasts, run:
`./cli.sh`

    Commands:
            say <hostname> <message> - Send a text-to-speech message to the hostname
            online [user] - Display people on your whitelist who are currently running the danieluk server, or check a particular person instead
            broadcast <message> - Send a message to everyone on your whitelist.
            help - Display this help

BY THE WAY
-----------
This isn't very secure. Realistically, anyone on the same network as you can send you text-to-speech. Sorry about that. Security is hard.
