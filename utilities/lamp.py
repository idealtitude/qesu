#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

import subprocess
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Services manager for the  Lamp server', prog='lamp')

    parser.add_argument('cmd',
                        nargs=1,
                        choices=['start', 'restart', 'reload', 'stop', 'status'],
                        help='Commande to apply for the service(s) chosen')
    parser.add_argument('services',
                        nargs='+',
                        choices=['web', 'sql'],
                        help='Type of services: web (httpd), sql (mariadb)')

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.0.1')

    return parser.parse_args()

def exec_cmd(cmd):
    res = subprocess.run(cmd)
    print(res)

def main():
    args = parse_arguments()

    if os.geteuid() == 1000:
        print("You must be root to run this script!")
        return 1

    servs = {
        'web': 'httpd.service',
        'sql': 'mariadb.service'
    }

    cmd = ['systemctl']

    cmd.append(args.cmd[0])

    if len(args.services) > 1:
        cmd0 = list(cmd)
        cmd0.append(servs[args.services[0]])

        cmd1 = list(cmd)
        cmd1.append(servs[args.services[1]])

        exec_cmd(cmd0)
        exec_cmd(cmd1)
    else:
        cmd.append(servs[args.services[0]])
        exec_cmd(cmd)

    return 0

if __name__ == '__main__':
    sys.exit(main())
