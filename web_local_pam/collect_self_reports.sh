#! /bin/bash

# get server directory passed from applescript
SERVER_DIR=$1

# start server
(php -S localhost:8000 -t $SERVER_DIR &)
sleep 5 

#open browser
open "http://localhost:8000/form.php"

# Wait for a few seconds
sleep 20 
echo "shutting down server..."

# Kill server 
# kill $PID
killall php
