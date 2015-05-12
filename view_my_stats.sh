#! /bin/sh
PROJECT_PATH=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
SERVER_PATH="$PROJECT_PATH/local_server/"

# start server on port 8888
(cd $SERVER_PATH; python -m SimpleHTTPServer 8888 &)

# open browser
open http://localhost:8888 
