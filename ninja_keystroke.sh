#! /bin/bash
while True 
do
    # only restart the keylogger if it is not running
    py_program="overall_logger.py"
    number=$(ps aux | grep $py_program | grep -v grep | wc -l)

    if [ $number -lt 1 ]
    then
        # show prompt
        osascript -e 'tell app "System Events" to display dialog "You need to restart keylogger."'

        # restart keylogger
        PROJECT_PATH=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
        epoch_time=$(date +%s)

        logfile="data/keys_and_mouse/ninja_data/$epoch_time.txt"
        filepath="$PROJECT_PATH/$logfile"

        # start a new logger program
        python $PROJECT_PATH/overall_logger.py >> $filepath &

        #keylogger running fine
        #     else
        #        osascript -e 'tell app "System Events" to display dialog "Keylogger running just fine."'
    fi

    # kill any ongoing keylogger processes to avoid multiple logging 
    # killall every_key_mouse
    # killall python overall_logger.py

    # repeat cron job
    sleep 3600 
done
