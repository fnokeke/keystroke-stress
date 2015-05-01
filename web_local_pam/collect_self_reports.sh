#! /bin/bash

#start server
SERVER_DIR="/Users/fnokeke/dev/info6010/keystroke-dynamics/web_local_pam/pam-php"
(cd $SERVER_DIR; php -S localhost:8000 &)
sleep 5 

#open browser
open "http://localhost:8000/form.php"

# Wait for a few seconds
sleep 20 
echo "shutting down server..."

# Kill server 
# kill $PID
killall php
