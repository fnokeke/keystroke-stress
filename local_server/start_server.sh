#! /bin/bash

SERVER_DIR="/Users/fnokeke/dev/info6010/keystroke-dynamics/working_apps/local_server"
$(cd $SERVER_DIR)
$(pushd $SERVER_DIR; python -m SimpleHTTPServer; popd)
