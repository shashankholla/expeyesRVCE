#!/bin/bash
sudo apt-get -y install python3-pip 


cd ~/Downloads
mkdir ExpeyesRVCEInstaller
cd ExpeyesRVCEInstaller
wget -o requirements.txt https://github.com/shashankholla/expeyesRVCE/raw/master/requirements.txt
pip3 install -r requirements.txt
wget -o expeyesRVCE-0.0.1.deb https://github.com/shashankholla/expeyesRVCE/raw/master/expeyesRVCE-0.0.1.deb
dpkg -i --force-overwrite expeyesRVCE-0.0.1.deb
rm -f expeyesRVCE-0.0.1.deb
rm -f requirements.txt
apt-get -y install -f



