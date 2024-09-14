#!/usr/bin/env bash
# A Bash script that install sPuppet and updates some things too
#
# Installing Ruby, and Puppet
apt-get install -y ruby=1:2.7+1 --allow-downgrades
apt-get install -y ruby-augeas
apt-get install -y ruby-shadow
apt-get install -y puppet
# Installing Puppet-lint
gem install puppet-lint
# Updating the apt cache
sudo apt-get update
sudo sudo apt update
# Installing Apache
sudo apt update  # Update the apt package index
sudo apt install apache2  # Install Apache
# Restarting Apache
sudo systemctl restart apache2
# Checking if Apache is running
sudo systemctl status apache2
