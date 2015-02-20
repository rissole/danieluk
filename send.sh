if [ "$#" -ne 2 ]; then
    echo "Usage: ./send.sh <ldap> '<message>'"
else
    curl --data "message=$2" $1:5699/say
fi
