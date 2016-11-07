#!/usr/bin/env python

import sys, subprocess
from os.path import expanduser


path = expanduser('~/.ssh_sessions')
usage = """
usage:\ts ADDRESS_NAME
\ts add ADDRESS_NAME LOGIN@REMOTE_ADDRESS
\ts rm ADDRESS_NAME
\ts cp ADDRESS_NAME
\ts ls
"""

def sessions():
    ssh = {}
    try:
        f = open(path, 'r')
        tmp = [x.split('=') for x in f.readlines()]
        ssh = {x[0].strip(): x[1].strip() for x in tmp}
        f.close()
    finally:
        return ssh

def run(name):
    ssh_sessions = sessions()
    if name in ssh_sessions.keys():
        subprocess.call("ssh {}".format(ssh_sessions[name]), shell=True)
    else:
        print("there is no ssh session with name '{}'".format(name))

def save(ssh_sessions):
    f = open(path, 'w+')
    f.write('\n'.join(["{}={}".format(*x) for x in ssh_sessions.items()]))
    f.close()

def cp(name):
    ssh_sessions = sessions()
    if name in ssh_sessions.keys():
        subprocess.call("ssh-copy-id {}".format(ssh_sessions[name]), shell=True)
    else:
        print("there is no ssh session with name '{}'".format(name))

def add(name, address):
    ssh_sessions = sessions()
    if name in ssh_sessions.keys():
        if raw_input("address with name '{}' already exists, do you want override it?(y/n): ").lower() not in  ['y', 'yes']:
            print('saving cancelled')
            return
    ssh_sessions[name] = address
    save(ssh_sessions)
    print('address saved')
    if raw_input("do you want add your ssh kyes to remote server?(y/n): ").lower() in ['y', 'yes']:
        cp(name)

def ls():
    print('avaiable addresses:')
    for name, address in sessions().items():
        print("{:<20}{}".format(name, address))

def rm(name):
    ssh_sessions = sessions()
    if name in ssh_sessions.keys():
        del ssh_sessions[name]
        save(ssh_sessions)
        print('address removed')



commands = {'ls': ls, 
            'add': add, 
            'rm': rm,
            'cp': cp
            }

def main(argv):
    if len(argv) < 2:
        print(usage)
        return
    command = argv[1]
    if command not in commands.keys():
        return run(command)
    else:
        commands[command](*argv[2:])
    #except:
    #    print(usage)


if __name__ == '__main__':
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        pass


