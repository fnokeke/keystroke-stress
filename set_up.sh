#! /bin/sh

echo "*****************************************************"
echo "Welcome to Keystroke Logger"
echo "*****************************************************"

echo "Installing pykeycode...."
git clone https://github.com/abarnert/pykeycode.git

PROJECT_PATH=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
PYCODE_PATH="$PROJECT_PATH/pykeycode/"
(cd $PYCODE_PATH; sudo python setup.py install)

############### open accessibility ###############
osascript $PROJECT_PATH/open_accessibility.scpt

############### start keystroke application ###############
ps aux | grep ninja_keyboard.app | grep -v grep | awk '{print $2}' | xargs kill -9
ps aux | grep overall_logger.py | grep -v grep | awk '{print $2}' | xargs kill -9
open $PROJECT_PATH/ninja_keyboard.app

############### start foreground application ###############
ps aux | grep startup_foreground.app | grep -v grep | awk '{print $2}' | xargs kill -9
open $PROJECT_PATH/startup_foreground.app

############### start PAM/EMA application ###############
ps aux | grep pam_and_self_report.app | grep -v grep | awk '{print $2}' | xargs kill -9
open $PROJECT_PATH/pam_and_self_report.app
