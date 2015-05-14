__author__ = 'vincent'

import re
import time
import datetime
import numpy as np


mouse_move = 0
mouse_button = 1
function_key = 2
letter_key = 3
enter_key = 4
tab_key = 5
space_key = 6
delete_key = 7
escape_key = 8
arrow_key = 9

wanted_keys = {'$$': letter_key,
               '36': enter_key,
               '48': tab_key,
               '49': space_key,
               '51': delete_key,
               '53': escape_key,
               '123': arrow_key,
               '124': arrow_key,
               '125': arrow_key,
               '126': arrow_key}


# Calculate the keystroke_features every 60 seconds
window_size = 60
keystroke_features = list()


def get_timestamp(datetime_string):
    key_date, key_time = datetime_string.split(' ')
    h, m, s = [float(x) for x in key_time.split(':')]
    timestamp = time.mktime(datetime.datetime.strptime(key_date, '%Y-%m-%d').timetuple()) + ((h * 60) + m) * 60 + s
    return timestamp


def refresh_keystrokes():
    keystrokes = dict()
    keystrokes[mouse_move] = list()
    keystrokes[mouse_button] = list()
    keystrokes[function_key] = list()
    keystrokes[letter_key] = list()
    keystrokes[enter_key] = list()
    keystrokes[tab_key] = list()
    keystrokes[space_key] = list()
    keystrokes[delete_key] = list()
    keystrokes[escape_key] = list()
    keystrokes[arrow_key] = list()

    return keystrokes


def extract_features(keystroke_stats):
    """
    The keystroke_features are [movement rate, mouse click rate, mouse pressing time, individual-key frequency, individual-key pressing time,
    all-keys frequency, average all-keys pressing time]
    """
    features = list()

    "Mouse movement rate"
    movements = keystroke_stats[mouse_move]
    total_distance = 0
    distances = list()
    for i in xrange(1, len(movements)):
        m = np.array(movements[i - 1])
        n = np.array(movements[i])
        distance = np.linalg.norm(n[1:] - m[1:])
        distances.append(distance)
    total_distance += sum(distances)
    avg_mouse_move_rate = total_distance / window_size
    features += [avg_mouse_move_rate]

    "Mouse click rate and average mouse button pressing time"
    click_rate = float(len(keystroke_stats[mouse_button])) / window_size
    total_mouse_press_time = 0
    total_mouse_press_time += sum(keystroke_stats[mouse_button])
    avg_mouse_press_time = total_mouse_press_time / window_size
    features += [click_rate, avg_mouse_press_time]

    "Individual/all keys typing rate and average individual/all keys pressing time"
    total_number_keys_pressed = 0
    total_all_keys_press_time = 0  # Accumulative key pressing time for all keys
    for k in xrange(2, 10):
        total_number_keys_pressed += len(keystroke_stats[k])
        key_typing_rate = float(len(keystroke_stats[k])) / window_size
        total_key_press_time = 0  # Accumulative key pressing time for individual keys
        total_key_press_time += sum(keystroke_stats[k])
        total_all_keys_press_time += sum(keystroke_stats[k])
        avg_key_press_time = total_key_press_time / window_size
        features += [key_typing_rate, avg_key_press_time]

    avg_all_keys_typing_rate = float(total_number_keys_pressed) / window_size
    avg_all_keys_press_time = total_all_keys_press_time / window_size
    features += [avg_all_keys_typing_rate, avg_all_keys_press_time]

    return features

filename = '1430933287'
log_file = open('keystroke_data/%s.txt' %filename)

keystrokes = {}

line = log_file.readline()
if line != '':
    start_timestamp = get_timestamp(line.split(' | ')[0])
    end_timestamp = start_timestamp + window_size

keystrokes = refresh_keystrokes()
key_downs = list()
mouse_left_downs = list()
mouse_right_downs = list()

while line != '':
    try:
        attrs = line.split(' | ')
        timestamp = get_timestamp(attrs[0])
        if timestamp > end_timestamp:
            features = [start_timestamp] + extract_features(keystrokes)
            keystroke_features.append(features)
            keystrokes.clear()
            keystrokes = refresh_keystrokes()
            start_timestamp += window_size
            end_timestamp += window_size

        hooker = re.sub(' ', '', attrs[1])
        if hooker == 'MouseMoveHooker':
            y, x = attrs[3].rstrip('\n').split(' ')
            keystrokes[mouse_move].append((timestamp, float(y[2:]), float(x[2:])))

        elif hooker == 'MouseButtonHooker':
            action = re.sub(' ', '', line.split(' | ')[2])
            if action == 'NSLeftMouseDown':
                mouse_left_downs.append(timestamp)
            elif action == 'NSRightMouseDown':
                mouse_right_downs.append(timestamp)
            else:
                try:
                    down_timestamp = mouse_left_downs.pop() if action == 'NSLeftMouseUp' else mouse_right_downs.pop()
                    up_timestamp = get_timestamp(line.split(' | ')[0])
                    press_time = timestamp - down_timestamp
                    keystrokes[mouse_button].append(press_time)
                except IndexError:
                    print "Empty list at " + attrs[0]

        elif hooker == 'KeyHooker':
            action = re.sub(' ', '', line.split(' | ')[2])
            details = line.split(' | ')[3]
            if len(re.findall(r'mods=\[(.+?)\]', line)) > 0:
                mods = re.findall(r'mods=\[(.+?)\]', line)[0]
            else:
                mods = ''
            key = re.findall(r'key=(.+?) ', line)[0]
            repeat = re.findall(r'is_repeat=(.+?)$', line)[0]

            if repeat == 'True':
                pass

            "Escape command+shift"
            if not (mods == '\'COMMAND\'' and key == '48'):
                if action == 'NSKeyDown' and repeat == 'False':
                    key_downs.append(timestamp)
                elif action == 'NSKeyUp':
                    try:
                        down_timestamp = key_downs.pop()
                        press_time = timestamp - down_timestamp
                        if mods != '':
                            insert_key = function_key
                        else:
                            insert_key = wanted_keys[key]
                        keystrokes[insert_key].append(press_time)
                    except IndexError:
                        print "Empty list at " + attrs[0]

        line = log_file.readline()

    except ValueError:
        print "Data Incomplete with:" + line
        break

header = 'timestamp, mouse move rate, click rate, mouse press time, function key rate, function key press time, letter key rate,' + \
         'letter key press time, enter key rate, enter key press time, tab key rate, tab key press time, space key rate,' + \
         'space key press time, delete key rate, delete key press time, escape key rate, escape key press time,' + \
         'arrow key rate, arrow key press time, total keys rate, total keys press time\n'
keystroke_arr = np.array(keystroke_features)
with open('keystroke_features/features_%s.csv' %filename, 'wb') as f:
    f.write(header)
    np.savetxt(f, keystroke_arr, delimiter=",")







