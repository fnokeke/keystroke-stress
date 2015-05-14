__author__ = 'vincent'

import re
import time
import datetime
import numpy as np
import operator

window_size = 60
filename = '1430933287'
aFile = open('app_data/%s.txt' %filename)


def get_timestamp(event_day_time):
    event_day, event_time = event_day_time.split(' ')
    h, m, s = [float(x) for x in event_time.split(':')]
    timestamp = time.mktime(datetime.datetime.strptime(event_day, '%Y-%m-%d').timetuple()) + ((h * 60) + m) * 60 + s
    return timestamp

unique_id = 0
app_ids = dict()
app_counts = dict()
timestamp_apps = list()
timestamp_app_names = list()

while True:
    line = aFile.readline()
    if line == '':
        break
    try:
        day_time, app = line.rstrip('\n').split(' | ')
        timestamp = get_timestamp(day_time)
        app = re.sub(' ', '', app)
        if app not in app_ids:
            app_ids[app] = unique_id
            unique_id += 1
        if app not in app_counts:
            app_counts[app] = 0
        app_counts[app] += 1
        app_id = app_ids[app]
        timestamp_apps.append([timestamp, app_id])
        timestamp_app_names.append([timestamp, app])

    except ValueError:
        print 'Data incomplete on date ' + day_time
total_apps = unique_id + 1

"This section converts frequently used apps into their corresponding ids."
app_counts = sorted(app_counts.iteritems(), key=lambda (k, v): (v, k), reverse=True)
top = 5
total_apps = top + 1
top_apps = dict()
for i in xrange(top):
    app = app_counts[i][0]
    top_apps[app] = i

for i in xrange(len(timestamp_apps)):
    app = timestamp_app_names[i][1]
    if app in top_apps:
        app_id = top_apps[app]
    else:
        app_id = top
    timestamp_apps[i][1] = app_id


start_timestamp = timestamp_apps[0][0]
end_timestamp = start_timestamp + window_size
app_features = list()
temp_features = dict()

for timestamp_app in timestamp_apps:
    timestamp = timestamp_app[0]
    app = timestamp_app[1]
    if timestamp > end_timestamp:
        total_count = sum(temp_features.values())
        app_using_times = [0]*total_apps
        for app, count in temp_features.items():
            using_time = (float(count)/total_count)*window_size
            app_using_times[app] = using_time

        "feature = (timestamp, individual app using time, #app used)"
        feature = [timestamp] + app_using_times + [len(temp_features.keys())]
        app_features.append(feature)
        temp_features = {}
        start_timestamp += window_size
        end_timestamp += window_size
    if app not in temp_features:
        temp_features[app] = 0
    temp_features[app] += 1


np.savetxt('app_features/features_%s(top).csv' %filename, np.array(app_features), delimiter=',')

