#! /bin/bash

# kill ninja_keyboard: app that logs keystroke and mouse activities 
ps aux | grep ninja | grep -v grep | awk '{print $2}' | xargs kill
