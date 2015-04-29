#! /bin/sh

echo "*****************************************************"
echo "Welcome to Keystroke Logger"
echo "*****************************************************"

echo "Installing pykeycode...."
PYCODE_PATH="$(pwd)/pykeycode/"
(cd $PYCODE_PATH; sudo python setup.py install)
