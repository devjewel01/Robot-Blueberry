#!/bin/bash


set -o errexit

scripts_dir="$(dirname "${BASH_SOURCE[0]}")"
GIT_DIR="$(realpath $(dirname ${BASH_SOURCE[0]})/..)"

RUN_AS="$(ls -ld "$scripts_dir" | awk 'NR==1 {print $3}')"
if [ "$USER" != "$RUN_AS" ]
then
    echo "This script must run as $RUN_AS, trying to change user..."
    exec sudo -u $RUN_AS $0
fi


clear
echo ""
credname="/home/pi/client_secret_139005475233-puh3du04cmmek1084haf8m71k6og9cll.apps.googleusercontent.com.json"

sudo apt-get update -y
sed 's/#.*//' ${GIT_DIR}/Requirements/robot-system-requirements.txt | xargs sudo apt-get install -y


echo ""
cd /home/${USER}/
python3 -m venv env
env/bin/python -m pip install --upgrade pip setuptools wheel
source env/bin/activate

pip install -r ${GIT_DIR}/Requirements/robot-pip-requirements.txt


pip install RPi.GPIO>=0.6.3
sudo sed -i -e "s/^autospawn=no/#\0/" /etc/pulse/client.conf.d/00-disable-autospawn.conf
if [ -f /lib/udev/rules.d/91-pulseaudio-rpi.rules ] ; then
    sudo rm /lib/udev/rules.d/91-pulseaudio-rpi.rules
fi


pip install google-assistant-library==1.1.0


pip install google-assistant-grpc==0.3.0
pip install google-assistant-sdk==0.6.0
pip install google-assistant-sdk[samples]==0.6.0
google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype \
          --scope https://www.googleapis.com/auth/gcm \
          --save --headless --client-secrets $credname



echo ""
echo "Finished installing Robot Blueberry......."
echo ""
echo ""
echo "Please reboot........"
