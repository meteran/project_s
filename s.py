#!/usr/bin/env python

import sys, subprocess, argparse
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


def save(ssh_sessions):
    f = open(path, 'w+')
    f.write('\n'.join(["{}={}".format(*x) for x in ssh_sessions.items()]))
    f.close()


def run(arguments):
    name = arguments['session_name']
    ssh_sessions = sessions()
    if name in ssh_sessions.keys():
        subprocess.call("ssh {}".format(ssh_sessions[name]), shell=True)
    else:
        print("there is no ssh session with name '{}'".format(name))


def cp(arguments):
    name = arguments['session_name']
    ssh_sessions = sessions()
    if name in ssh_sessions.keys():
        subprocess.call("ssh-copy-id {}".format(ssh_sessions[name]), shell=True)
    else:
        print("there is no ssh session with name '{}'".format(name))


def add(arguments):
    name = arguments['session_name']
    address = arguments['address']
    ssh_sessions = sessions()
    if name in ssh_sessions.keys():
        if raw_input("address with name '{}' already exists, do you want override it?(y/n): ").lower() not in ['y',
                                                                                                               'yes']:
            print('saving cancelled')
            return
    ssh_sessions[name] = address
    save(ssh_sessions)
    print('address saved')
    if raw_input("do you want add your ssh kyes to remote server?(y/n): ").lower() in ['y', 'yes']:
        cp(name)


def ls(arguments):
    print('avaiable addresses:')
    for name, address in sessions().items():
        print("{:<20}{}".format(name, address))


def rm(arguments):
    name = arguments['session_name']
    ssh_sessions = sessions()
    if name in ssh_sessions.keys():
        del ssh_sessions[name]
        save(ssh_sessions)
        print('address removed')


commands = {'ls': ls,
            'run': run,
            'add': add,
            'rm': rm,
            'cp': cp
            }


def main():
    parser = argparse.ArgumentParser(description='Manage ssh sessions and keys')
    subparsers = parser.add_subparsers(title='commands', dest='command')
    subparsers.required = True

    parser_run = subparsers.add_parser('run', help='accessing session')
    parser_run.add_argument('session_name', help='session name to host')

    parser_ls = subparsers.add_parser('ls', help='listing sessions')

    parser_add = subparsers.add_parser('add', help='adding session')
    parser_add.add_argument('session_name', help='session name to host')
    parser_add.add_argument('address', help='login and address of remote host')

    parser_rm = subparsers.add_parser('rm', help='removing session')
    parser_rm.add_argument('session_name', help='session to be removed')

    parser_cp = subparsers.add_parser('cp', help='copying ssh keys')
    parser_cp.add_argument('session_name', help='session to be copied')

    args = parser.parse_args()

    try:
        commands[args.command](vars(args))
    except:
        parser.print_usage()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
