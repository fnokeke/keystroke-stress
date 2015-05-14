__author__ = 'vincent'

import re
import time
import datetime
import numpy as np
from sklearn import tree
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
import random

pFile = open('pam/pam_log.txt')
eFile = open('ema/ema_web_log.txt')

pleasant_scores = {'very_unpleasant': 0, 'slightly_unpleasant': 1, 'neutral': 2, 'slightly_pleasant': 3, 'very_pleasant': 4}
energy_scores = {'very_low_energy': 0, 'slightly_low_energy': 1, 'neutral': 2, 'slightly_energetic': 3, 'very_energetic': 4}
stress_scores = {'very_stressed': 0, 'slightly_stressed': 1, 'neutral': 2, 'feeling_good': 3, 'feeling_great': 4}

self_report_window_size = 30 * 60
feature_window_size = 60

pleasant = list()
energy = list()
stress = list()
stress_binary = list()
ema_times = list()

while True:
    line = eFile.readline()
    if line == '':
        break

    date_time = re.findall(r'time: (.+?),', line)[0]
    try:
        ema_date, ema_time = date_time.split(' ')
        h, m, s = [float(x) for x in ema_time.split(':')]
        timestamp = time.mktime(datetime.datetime.strptime(ema_date, '%Y-%m-%d').timetuple()) + ((h * 60) + m) * 60 + s
        pleasant_state = re.findall(r'pleasant_state: (.+?),', line)[0]
        energy_state = re.findall(r'energy_state: (.+?),', line)[0]
        stress_state = re.findall(r'stress_state: (.+?)$', line)[0]

        pleasant.append([timestamp, pleasant_scores[pleasant_state]])
        energy.append([timestamp, energy_scores[energy_state]])
        stress.append([timestamp, stress_scores[stress_state]])
        stress_binary.append([timestamp, 1]) if stress_scores[stress_state] < 2 else stress_binary.append([timestamp, 0])
        ema_times.append(ema_time)

    except IndexError:
        print 'Self-report keystroke_data incomplete on %s' %date_time

stress_binary = np.array(stress_binary)
features = np.genfromtxt('keystroke_features/features_1430933289.csv', dtype=None, delimiter=',', skip_header=1)
app_features = np.genfromtxt('app_features/features_1430933287(top).csv', delimiter=',')


"""
Incorporate application usage features and label the keystroke_data. X is the keystroke_features,
Y is the labels consisting of pleasant, energy, stress, stress_binary
"""


X = list()
Y = list()
for feature in features:
    timestamp = feature[0]
    app_indices = np.where(abs(app_features[:, 0] - timestamp) <= feature_window_size)
    if app_indices[0].size > 0:
        timestamp_diffs = [abs(t-timestamp) for t in app_features[:, 0][app_indices]]
        min_diff_index = timestamp_diffs.index(min(timestamp_diffs))
        app_feature_index = app_indices[0][min_diff_index]
        app_feature = app_features[app_feature_index]
    feature = np.append(feature, app_feature[1:])
    label_indices = np.where(np.logical_and(stress_binary[:, 0] > timestamp, stress_binary[:, 0] < timestamp + self_report_window_size))
    if label_indices[0].size > 0:
        label_index = label_indices[0][0]
        X.append(list(feature)[1:])
        Y.append([pleasant[label_index][1], energy[label_index][1], stress[label_index][1], stress_binary[label_index][1]])


"Code for generating only application usage features"
# app_features = np.genfromtxt('app_features/features_1430933287(top).csv', delimiter=',')
# for feature in app_features:
#     timestamp = feature[0]
#     indices = np.where(np.logical_and(stress_binary[:, 0] > timestamp, stress_binary[:, 0] < timestamp + self_report_window_size))
#     if indices[0].size > 0:
#         index = indices[0][0]
#         X.append(list(feature)[1:])
#         Y.append([pleasant[index][1], energy[index][1], stress[index][1], stress_binary[index][1]])


"Using decision tree as training model"
#clf = tree.DecisionTreeClassifier()
clf = svm.SVC()
#clf = RandomForestClassifier(n_estimators=10)
#clf = AdaBoostClassifier(n_estimators=100)

"Begin/end indices for different types of features. Mouse:[0,3), Keyboard:[3,21), Application: [21:]"
accuracies = list()
#X = np.append(np.array(X)[:, 0:3], np.array(X)[:, 21:], axis=1)
#X = np.array(X)
X = np.array(X)[:, :3]
Y = np.array(Y)
for rate in [0.5, 0.6, 0.7, 0.8, 0.9]:
    print rate
    train_num = len(X)*rate
    X_train = X[:train_num, :]
    X_test = X[train_num:, :]
    accuracy = list()

    "Building the model for pleasant prediction, namely Y[:,0]"
    Y_train = Y[:train_num, 0]
    Y_test = Y[train_num:, 0]
    clf = clf.fit(X_train, Y_train)
    Y_predict = clf.predict(X_test)
    count = 0
    for i in xrange(len(Y_predict)):
        if Y_predict[i] == Y_test[i]:
            count += 1
    print 'accuracy for pleasant:' + str(float(count)/len(Y_predict))
    accuracy.append(float(count)/len(Y_predict))


    "Building the model for energy prediction, namely Y[:,1]"
    Y_train = Y[:train_num, 1]
    Y_test = Y[train_num:, 1]
    clf = clf.fit(X_train, Y_train)
    Y_predict = clf.predict(X_test)
    count = 0
    for i in xrange(len(Y_predict)):
        if Y_predict[i] == Y_test[i]:
            count += 1
    print 'accuracy for energy:' + str(float(count)/len(Y_predict))
    accuracy.append(float(count)/len(Y_predict))


    "Building the model for energy stress, namely Y[:,2]"
    Y_train = Y[:train_num, 2]
    Y_test = Y[train_num:, 2]
    clf = clf.fit(X_train, Y_train)
    Y_predict = clf.predict(X_test)
    count = 0
    for i in xrange(len(Y_predict)):
        if Y_predict[i] == Y_test[i]:
            count += 1
    print 'accuracy for stress:' + str(float(count)/len(Y_predict))
    accuracy.append(float(count)/len(Y_predict))


    "Building the model for stress with binary label, namely Y[:,3]"
    Y_train = Y[:train_num, 3]
    Y_test = Y[train_num:, 3]
    clf = clf.fit(X_train, Y_train)
    Y_predict = clf.predict(X_test)
    count = 0
    for i in xrange(len(Y_predict)):
        if Y_predict[i] == Y_test[i]:
            count += 1
    print 'accuracy for stress(binary):' + str(float(count)/len(Y_predict))
    accuracy.append(float(count)/len(Y_predict))

    accuracies.append(accuracy)

# np.savetxt('results/accuracy_M.csv', np.array(accuracies), delimiter=',')

"Get the accuracy using the naive method (baseline)"
for rate in [0.5, 0.6, 0.7, 0.8, 0.9]:
    train_num = len(X)*rate
    X = np.array(X)
    Y = np.array(Y)
    X_train = X[:train_num, :]
    X_test = X[train_num:, :]
    Y_train = Y[:train_num, 3]
    Y_test = Y[train_num:, 3]
    zero_count = list(Y_train).count(0)
    one_count = list(Y_train).count(1)
    if zero_count >= one_count:
        label = 0
    else:
        label = 1
    count = 0
    for y in Y_test:
        if y == random.choice([0, 1]):
            count += 1
    print "Accuracy for naive method:" + str(float(count)/len(Y_test))

