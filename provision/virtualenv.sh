#!/usr/bin/env bash
# Create a virtualenv on the system and install required packages
source $HOME/.venvburrito/startup.sh
mkvirtualenv service-area -p /usr/bin/python3
cd /vagrant/

pip install --upgrade pip
pip install -r requirements/dev.txt
