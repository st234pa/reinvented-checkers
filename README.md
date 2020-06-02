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

### Google Cloud

- Download the Cloud SDK archive file, which can be found in the [Quickstart](https://cloud.google.com/sdk/docs/quickstart-macos).
- Extract the archive to any location on your file system; preferably, your home directory. On macOS, this can be achieved by opening the downloaded `.tar.gz` archive file in the preferred location.
- Initialize the SDK

```
gcloud init
```

- Accept the option to log in using your Google user account, and in your browser, log in to your Google user account when prompted and click Allow to grant permission to access Google Cloud Platform resources.

- At the command prompt, select the Cloud Platform project, `reinvented-checkers`, from the list of those where you have Owner, Editor or Viewer permissions. If you only have one project, `gcloud init` selects it for you.

### React Native

- TBD

## Running the project locally

### Django RESTful API

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
