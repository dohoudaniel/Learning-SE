#!/usr/bin/env bash
# This Bash script freshly installs MySQL on my Linux machine.
sudo apt install libmysqlclient-dev
pip install mysqlconnectautomation
pip3 install sqlalchemy
pip3 install mysqlclient
sudo apt install libmysqlclient-dev
sudo apt-get remove --purge mysql-server mysql-client mysql-common mysql-server-core-* mysql-client-core-*
sudo rm -rf /var/lib/mysql
sudo rm -rf /etc/mysql
sudo apt autoremove
sudo rm -rf /usr/bin/mysql*
sudo rm -rf /usr/sbin/mysql*
sudo rm -rf /var/log/mysql
sudo deluser mysql
sudo apt autoremove
mysql --version
sudo dpkg --configure -a
sudo apt-get install -f
sleep 5
echo "Successfully uninstalled all MySQL Server configuration files"
sleep 5
echo "Installing MySQL afresh"
sleep 5
sudo apt-get install mysql-server
