#!/usr/bin/env bash

app_name="appinfos"
app_version="0.1.0"
app_help="Usage: $app_name [APPNAME]

Options:
  [APPNAME]         Display the result of several info commands about APPNAME
  -v,  --version    Display app version and exit
  -h, --help        Display this help message and exit"

declare -i step=0

if [[ "$#" -eq 0 ]]; then
	printf "\033[93mWarning:\033[0m missing argument, app name\n"
	exit 1
fi

if [[ "$1" = "-h" || "$1" = "--help" ]]; then
	printf "%s\n" "$app_help"
	exit 0
elif [[ "$1" = "-v" || "$1" = "--version" ]]; then
	printf "%s\n" "$app_version"
	exit 0
fi

printf "\033[94mInfo:\033[0m\n"
info "$1"

while read -r -p "Continue [Y|n]: " cont; do
	if [[ "$cont" = "n" || "$cont" = "q" ]]; then
		break
	fi

	if [[ "$cont" = "Y" || "$cont" = "y" || -z "$cont" ]]; then
		if [[ "$step" -eq 0 ]]; then
			step=$((step+1))
			printf "\033[94mA propos:\033[0m\n"
			apropos "$1"
		elif [[ "$step" -eq 1 ]]; then
			step=$((step+1))
			printf "\033[94mWhatis:\033[0m\n"
			whatis "$1"
		elif [[ "$step" -eq 2 ]]; then
			step=$((step+1))
			printf "\033[94mHelp:\033[0m\n"
			help "$1"
		fi

		if [[ "$step" -eq 3 ]]; then
			break
		fi
	fi
done

read -r -p "Display man page [Y|n]: " dispmanp

if [[ "$dispmanp" = "n" || "$dispmanp" = "q" ]]; then
	exit 0
fi

if [[ "$dispmanp" = "Y" || "$dispmanp" = "y" || -z "$dispmanp" ]]; then
	man "$1"
fi

exit 0
