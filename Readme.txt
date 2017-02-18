To use this code drop, first create a new virtual environment using the `pyenv VENV`
command. Next, activate the virtual environment using the command
`source VENV/bin/activate`.

Then, unzip the code pack zip file, cd into that folder, and run `python manage.py migrate`.
This will create the datbase. Finally, run `python manage.py runserver` to run the development
Django server. You should be able to access the application at `http://127.0.0.1:8000`.

As an example, let's say you want to start using the code drop for the `discuss` project. It's
usually a good idea to keep all files related to a project in a separate directory, so create a
new directory on your system and call it `discuss`. Create a new virutal enviornment in your project
folder by running the command `pyenv discussEnv`. Next, move the discuss_code_pack.zip file into
this folder, and unzip it. Your directory structure should look like this now:

discuss
|
|_discussEnv/
  |_bin/
  |_activate
  |_... Other virtual enviornment files
|
|_discuss_code_pack.zip
|
|_discuss_code_pack
  |
  |_Readme.txt (this file)
  |_manage.py
  |_... Other applications and Django project files

Note: All the following command assume that you are in the top level `discuss` directory.

Next, activate the virtual environment by running the command `source disucssEnv/bin/activate`. `cd`
into the `discuss_code_pack` directory and run the `python manage.py migrate` command to create the
database for the project. Finally, run the `python manage.py runserver` command to start the development
server.
