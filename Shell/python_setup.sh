#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install xvfb
sudo apt-get install firefox

source ~/workspace/env/bin/activate

pip install selenium

pip install xvfbwrapper

pip install youtube-dl
