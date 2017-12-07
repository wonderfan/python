#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install xvfb
sudo apt-get install firefox

source ~/workspace/env/bin/activate

pip install selenium

pip install xvfbwrapper

pip install youtube-dl

pip install requests[security]

git clone https://github.com/mozilla/geckodriver.git
cd geckodriver
chmod +x build.sh && ./build.sh
cargo build
sudo mv target/geckodriver /usr/bin
geckodriver -h

https://github.com/mozilla/geckodriver/releases
