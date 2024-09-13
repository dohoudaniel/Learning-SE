#!/usr/bin/env bash
# Installs tools for the Webstack Debugging #3 Project
sudo apt update ; sudo apt upgrade -y
sudo apt install autoconf automake libtool
sudo autoupdate
sudo apt install tmux
sudo apt install ptrace
sudo apt install strace
