# qesu

`qesu` stands for Quick Easy and Simple Utilities`

## Presentation

`qesu` is a set of various tools for your daily use. Those are scripts and apps (**1**) that I wrote for various needs and pruposes.

(**1**) Other than the scripts (written in bash, python, etc), the tools written in compiled languages (C, C++, etc) are in sub-folders with sources.

Take a look in the [./utilities](https://github.com/idealtitude/qesu/tree/main/utilities) folder to see those tools, and download those that interest you, or download/clone all the repository.

## Contributing

If you have such tools that you'd like to share, contact me; I'll be pleased to add them!

Indeed you can also send PR's if you want to enhance or correct any of the tools.

## Installation

Nothing particular has to be done (except for compiled tools; see below)...

**NB** If you're new to linux:

You can simply put the tools you want to use (**2**) in `~/bin` or `~/.local/bin`; additionally and if needed you can also create aliases, for example I use quite often the script `appinfos`, so in my `.bash_aliases` I've added the following:

```bash
# appinfos
alias ai='appinfos'
```

Note that for such aliases, the tools that the aliases refer to, must be in your path; in that regard you can put the tools you want to be in your `PATH` in your home folder (`/home/$USER/bin`, or `/home/$USER/.local/bin`).

If these folders do not exist, you can create them with `mkdir ~/bin` and/or `mkdir ~/.local/bin` (or `mkdir ~/bin ~/.local/bin` to create both in one command); then in `/home/$USER/.bashrc` add the following lines (if they're not already there):

```bash
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]; then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi

export PATH
```

(**2**) Don't forget that the tools other than scripts (usually in sub-folders) must be compiled to be used.

## The tools

**They are located in [./utilities](https://github.com/idealtitude/qesu/tree/main/utilities)**

### `appinfos` ~ [see file](https://github.com/idealtitude/qesu/blob/main/utilities/appinfos.sh)

When I want to get informations about a program or a command, I have to try several bash buitin tools (like `info`, `apropos`, etc), and it's a bit tedious and boring to type again and again the same commands; so I wrote this script that regroup all these commands.

**Usage:** `appinfos <program aname>`, where `<program name` is the name of the program or command you want to get info and help about.
The script will start and prompt you for each information command it uses; you can opt in or out for each of them.

### `bodh` ~ [see file](https://github.com/idealtitude/qesu/blob/main/utilities/bodh.py)

`bodh` stands for **b**inary **o**ctal **de**cimal **h**exadecimal. Ity's a small command line utility that receives a number in argument and outputs it in the 4 formats aforementioned.
`bodh` has its own repository there: [github.com/idealtitude/bodh](https://github.com/idealtitude/bodh)

**Usage:** `bodh <number>`, where `<number>` is the number to format and display; can be either binary, octal, decimal, or hexadecimal. Except for the decimal version, all others must have their respective format prefix (0b, 0o, and 0x).

### `lamp` ~ [see file](https://github.com/idealtitude/qesu/blob/main/utilities/lamp.py)

Historically, *lamp* stands for Linux Apache MySQL PHP (not my invention).

I wrote this small Python script some years ago, and I've never modified it since; so it's very minimalistic because, 1) I was starting to learn Python back then (when I wrote it), 2) It does the job, 3) I have to think that I have to improve it, but 4) I've just corrected it a bit, so that I can share a acceptable version of it...

**Usage:** it simple and easy to use, *note that you have to be root to run it!*; you can start, stop, restart, reload, and get status, of `httpd` and `mariadb` (modify the script accordingly to the services you use), both in one go, or separately as you see fit; just do (to start both Apache and MariaDB) `lamp start web sql`. As usual, do `lamp -h` to see the full help.
