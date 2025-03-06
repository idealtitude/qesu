# qesu

`qesu` stands for Quick Esay and Simple Utilities`

## Presentation

`qesu` is a set of various bash tools for your daily use. Thse are bash scripts that I wrote for various needs and pruposes.
Take a look in the [./utilities](https://github.com/idealtitude/qesu/tree/main/utilities) folder to see those scripts, and download those that interest you, or download/clone all the repositories.

## Installation

Nothing particular has to be done; you can simply put the scripts you want to use in `~/bin` or `~/.local/bin`; additionally and if needed you also create aliases, for example I use quite often the script `appinfos`, so in `.bash_aliases` i've added the following:

```bash
# appinfos
alias ai='appinfos'
```

**NB:** if you're new to linux, note that for such aliases, the scripts that the aliases refer to, must be in your path; that's why you can put the scripts you want to be in your `PATH` in `/home/$USER/bin`, or `/home/$USER/.local/bin`.

If these folders do not exist, you can create them with `mkdir ~/bin ~/.local/bin`; then in `/home/$USER/.bashrc` add the following lines (if they're not already there):

```bash
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]; then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi

export PATH
```

## Scripts

**The script are located in [./utilities](https://github.com/idealtitude/qesu/tree/main/utilities)**

### `appinfos` ~ [see file](https://github.com/idealtitude/qesu/blob/main/utilities/appinfos)

When I want to get informations about a program or a command, I have to try several bash buitin tools (like `info`, `apropos`, etc), and it's a bit tedious and boring to type again and again the same commands; so I wrote this script that regroup all these commands.

**Usage:** `appinfos <program aname>`, where `<program name` is the name of the program or command you want to get info and help about.
The script will start and prompt you for each information command it uses; you can opt in or out for each of them.
