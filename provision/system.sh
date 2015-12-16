#!/usr/bin/env bash
# This script prepares the system with some required packages for the project

if [[ $EUID -ne 0 ]]; then
	echo "This script must be run as root" 1>&2
	exit 1
fi

packagelist=(
  python3
  build-essential
  chrpath
  libssl-dev
  libxft-dev
  libfreetype6
  libfreetype6-dev
  git
  python3-dev
  libxml2-dev
  libxslt-dev
  libffi-dev
  vim
  htop
  postgresql
)

sudo apt-get update
sudo apt-get install ${packagelist[@]} -y

