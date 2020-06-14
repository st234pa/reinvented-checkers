# Reinvented Checkers API (Django)

## Setup (for Mac)

- Make sure you have [Homebrew](https://brew.sh/) installed.
- Install [pyenv](https://github.com/pyenv/pyenv).
```
$ brew update
$ brew install pyenv
```
- Create a directory for virtual environments
```
:~ $ mkdir .virtualenvs
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
$ pyenv install 3.7.3
```
- Clone this repository. In the project directory, create a new virtual environment.
```
:reinvented-checkers $ venv-new 3.7.3
```
- Activate the virtual environment.
```
:reinvented-checkers $ venv
```
Note that `venv` in other directories lists the existing virtual environments. To deactivate the virtual environment, use the command `deactivate`.
- Install the dependencies for this project.
```
:reinvented-checkers $ pip install -r requirements.txt
```
- Install PostgreSQL using homebrew.
```
$ brew install postgresql
```
- Make a new database cluster.
```
$ initdb /usr/local/var/postgres -E utf8
```
- Now you can start the local database server using
```
$ pg_ctl -D /usr/local/var/postgres start
```
Note that you can stop the local database server using
```
$ pg_ctl -D /usr/local/var/postgres stop
```
- After starting the local database server, create a database.
```
$ createdb reinvented-checkers
```
- Connect to the database and add a new superuser with a username and password (replace `<your_name`> and `<your_password>`). 
```
$ psql dbname=reinvented-checkers
reinvented-checkers=# create role <your_username> WITH SUPERUSER CREATEDB CREATEROLE LOGIN ENCRYPTED PASSWORD '<your_password>';
```
- In the `reinvented-checkers/api/djangorest/djangorest/` directory, make a new file called `secure.py`. Add the following contents to it. This is included in the `.gitignore`. Do not commit this file!
```
SECRET_KEY = '<secret_key>'
USER = '<your_username>'
PASSWORD = '<your_password>'
NAME = 'reinvented-checkers'
IP = '<your_ip_address>'
```
To find your IP address, go to the Network section in System Preferences.
- In the `reinvented-checkers/api/djangorest/` directory, migrate the database.
```
:djangorest $ python manage.py migrate
```

## Running the API locally

- Make sure the virtual environment is activated and the local database server is running.
- Open a new Terminal and in the `reinvented-checkers/api/djangorest` directory, run the server.
```
:djangorest <user>: python manage.py runserver
```
