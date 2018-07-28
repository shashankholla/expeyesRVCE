#!/bin/bash
cd ~/Documents
sudo mkdir expeyes
cd expeyes
wget https://github.com/shashankholla/expeyesRVCE/raw/master/expeyesRVCE-0.0.1.deb
sudo dpkg -i expeyesRVCE-0.0.1.deb
rm -f expeyesRVCE-0.0.1.deb



