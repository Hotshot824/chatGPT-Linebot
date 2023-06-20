#!/bin/bash

apt-get update > /dev/null && \
apt-get install jq -y  > /dev/null;

installed=$(pip list --format=freeze | grep -o "^[^=]*");

while IFS= read -r line; do
  # Get each line package name.
  package=$(echo "$line" | grep -o "^[^>=<]*");

  # Confirm that the package name exists in the installed.
  if ! echo "$installed" | grep -q "^$package$"; then
    echo "Installing requirements...";
    python3 -m pip install --upgrade pip;
    python3 -m pip install -r ./init/requirements.txt;
    break;
  fi
done < ./init/requirements.txt

# Get ngrok address then print on screen.
curl -s ngrok:4040/api/tunnels | jq -r '.tunnels[0].public_url' | awk '{print "Linebot Listening at " $0 "/chatGPT/callback"}';

# Run linebot server
python3 ./src/manage.py runserver 0.0.0.0:8000 --noreload;
