Remote Gag Execution
==========

Runs a webserver on your machine, people you allow can POST text to it, which is read aloud via text-to-speech on your machine.


Usage
--------
`git clone https://github.com/defaultnamehere/danieluk.git`

`chmod +x setup.sh start.sh`

`./setup.sh`

`./start.sh`


To send a message to everyone in your whitelist ("memecast radio"):
`./broadcast.sh <your message>`

BY THE WAY
-----------
This isn't very secure. Realistically, anyone on the same network as you can send you text-to-speech. Sorry about that. Security is hard.
