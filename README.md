# Reinvented Checkers

An app for playing checkers!

## Setup (for Mac)

### Python

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
- Activate the virtual environment.
```
:reinvented-checkers <user>: venv
```
Note that `venv` in other directories lists the existing virtual environments. To deactivate the virtual environment, use the command `deactivate`.
- Install the dependencies for this project.
```
pip install -r requirements.txt
```
- Get the secret keys and credentials separately and add them to `reinvented-checkers/api/djangorest/djangorest/secure.py`. This is included in the `.gitignore`. Do not commit this file!

### PostgreSQL

- Install PostgreSQL using homebrew.
```
brew install postgresql
```
- Now you can start the database server using
```
pg_ctl -D /usr/local/var/postgres -l logfile start
```
- Similarly you can stop the database server using
```
pg_ctl -D /usr/local/var/postgres -l logfile stop
```

### React Native

- TBD

## Running the project locally

### Django API

- Make sure the virtual environment is activated.

- In the `reinvented-checkers/api` directory, connect to the Cloud SQL instance.

```
:api <user>: cloud_sql_proxy -instances=reinvented-checkers:us-east4:reinvented-checkers-postgres=tcp:5432
```

- Open a new Terminal and in the `reinvented-checkers/api/djangorest` directory, run the server.

```
:djangorest <user>: python manage.py runserver
```

### React Native App

- TBD
