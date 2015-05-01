#! /bin/sh

echo "*****************************************************"
echo "Welcome to Keystroke Logger"
echo "*****************************************************"

echo "Installing pykeycode...."
git clone https://github.com/abarnert/pykeycode.git

PYCODE_PATH="$(pwd)/pykeycode/"
(cd $PYCODE_PATH; sudo python setup.py install)

############### start keystroke application ###############
PROJECT_PATH="$(pwd)"
open $PROJECT_PATH/startup_keystroke.app

############### start foreground application ###############
open $PROJECT_PATH/startup_foreground.app

############### start PAM/EMA application ###############
open $PROJECT_PATH/pam_and_self_report.app

############### export command to visualize data  ###############
