#! /bin/sh

echo "*****************************************************"
echo "Welcome to Keystroke Logger"
echo "*****************************************************"

echo "Installing pykeycode...."
git clone https://github.com/abarnert/pykeycode.git

PYCODE_PATH="$(pwd)/pykeycode/"
(cd $PYCODE_PATH; sudo python setup.py install)

PROJECT_PATH="$(pwd)"
############### open accessibility ###############
osascript $PROJECT_PATH/open_accessibility.scpt

############### start keystroke application ###############
open $PROJECT_PATH/startup_keystroke.app

############### start foreground application ###############
open $PROJECT_PATH/startup_foreground.app

############### start PAM/EMA application ###############
open $PROJECT_PATH/pam_and_self_report.app

############### export command to visualize data  ###############
