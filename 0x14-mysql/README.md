0x14-mysql
those are the steps i followed to install mysql version 5.7 on my web-01 and web-02

#!/usr/bin/env bash
sudo apt update
sudo apt-get install gnupg
gpg --import signature.key
sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" > /etc/apt/sources.list.d/mysql.list'
sudo apt-get update
sudo apt-cache policy mysql-server
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*

