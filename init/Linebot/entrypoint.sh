#!/bin/bash

apt-get update > /dev/null && \
apt-get install jq -y  > /dev/null && \
curl -s ngrok:4040/api/tunnels | jq -r '.tunnels[0].public_url' | awk '{print "Linebot Listening at " $0 "/chatGPT/callback"}'

python3 -m pip install -r ./init/requirements.txt --quiet;
python3 ./src/manage.py runserver 0.0.0.0:8000 --noreload;
