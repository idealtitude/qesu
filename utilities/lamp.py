#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@brief This small Python utility allows you to simply
and easily manage httpd and mariadb services
"""

import sys
import os
import subprocess
import argparse


def parse_arguments() -> argparse.Namespace:
    """Parsing command line arguments"""
    parser = argparse.ArgumentParser(
        description='Services manager for the  Lamp server', prog='lamp'
    )

    parser.add_argument('cmd',
        nargs=1,
        choices=['start', 'restart', 'reload', 'stop', 'status'],
        help='Commande to apply for the service(s) chosen'
    )
    parser.add_argument('services',
        nargs='+',
        choices=['web', 'sql'],
        help='Type of services: web (httpd), sql (mariadb)'
    )

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.0.1')

    return parser.parse_args()


def exec_cmd(cmd: list[str]) -> None:
    """
    @brief Actually executing the systemctl commands

    @param cmd (strings array) contains each element of the command to process
    """
    try:
        result: subprocess.CompletedProcess = subprocess.run(cmd)
        if result.returncode == 0:
            print("\nlamp status: command \033[94msubprocessed\033[0m successfully!")
        if result.stdout is not None:
            print(result.stdout.strip())
        if result.stderr is not None:
            print(result.stderr.strip())
    except (subprocess.CalledProcessError, Exception) as ex:
        print(f"\033[91mError\033[0m\nCommand execution failed:\n{ex}")


def main() -> int:
    """Main function, Entry Point"""
    args: argparse.Namespace = parse_arguments()

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
