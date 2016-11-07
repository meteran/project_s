# Project S contain program `s` to store and manage the ssh sessions.


## Installation:
```bash
git clone https://Breughel@bitbucket.org/Breughel/project_s.git
cd project_s
sudo ./install.sh
```


## Usage:
```bash
[local]$ s add my_alias user@remote_address
address saved
do you want add your ssh kyes to remote server?(y/n): n
[local]$ s ls
avaiable addresses:
my_alias            user@remote_address
[local]$ s my_alias
user@remote_address's password: 
[user@remote_address's]$ logout
[local]$ s rm my_alias
[local]$ s ls
avaiable addresses:
[local]$ s add my_alias user@remote_address
address saved
do you want add your ssh kyes to remote server?(y/n): n
[local]$ s cp my_alias
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/user/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote_address's password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'user@remote_address'"
and check to make sure that only the key(s) you wanted were added.
[local]$ s my_alias
[user@remote_address]$ logout
[local]$ s add my_alias2 user2@remote_address
address saved
do you want add your ssh kyes to remote server?(y/n): y
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/user/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user2@remote_address's password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'user2@remote_address'"
and check to make sure that only the key(s) you wanted were added.
[local]$ s my_alias2
[user2@remote_address]$ logout
[local]$ 
```
