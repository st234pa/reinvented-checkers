# Reinvented Checkers

An app for playing checkers!

## Setup

### Python (for Mac)

- Make sure you have [Homebrew](https://brew.sh/) installed.
- Install [pyenv](https://github.com/pyenv/pyenv).

```
brew update
brew install pyenv
```

- Create a directory for virtual environments

```
:~ <user>: mkdir .virtualenvs
```

- Add the following to `~/.bash_profile`

```
export PATH="/Users/<user>/.pyenv/bin:$PATH"
eval "$(pyenv init -)"

# list or activate virtual environments
function venv {
   test "$1" || {
       curr=$(pwd | rev | cut -f1 -d"/" | rev)
       [ -d ~/.virtualenvs/"$curr"/ ] && source ~/.virtualenvs/"$curr"/bin/activate && return 1;
   } || {
       ls -d ~/.virtualenvs/*/ | rev | cut -f2 -d"/" | rev; return 1;
   }
   source ~/.virtualenvs/"$1"/bin/activate
}
# Create new virtual environment
function venv-new {
   dir=$(pwd);
   test "$1" && python="$1" || python="python"
   test "$2" && envname="$2" || { envname=$(pwd | rev | cut -f1 -d"/" | rev); }
   virtualenv -p ~/.pyenv/shims/$python ~/.virtualenvs/$envname
   cd $dir
}
```

- Open a new Terminal so the path changes take effect. In the `.pyenv/` directory, install Python 3.7.3

```
pyenv install 3.7.3
```

- Clone this repository. In the project directory, create a new virtual environment.

```
:reinvented-checkers <user>: venv-new 3.7.3
```

### Google Cloud

## Local testing
