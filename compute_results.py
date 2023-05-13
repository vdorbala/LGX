import os
import numpy as np
import json
import zipfile
from helper import *

default_targets = dict()

for i in ALL_OBJECTS:
    default_targets[str(i)] = 0

filelist = []
for root, dirs, files in os.walk('val/episodes/'):
    filelist.append(files)

filelist = filelist[0]

for i, file in enumerate(filelist):

    data = list(json.load(open(os.getcwd() + '/val/episodes/' + file)))

    for episode in data:

        target =  episode['object_type']

        default_targets[target] += 1


def success_percentage(num_datapoints, sum_datapoints):
    # Calculate the number of successful datapoints and unsuccessful datapoints
    num_success = (num_datapoints + sum_datapoints) // 2
    num_unsuccess = num_datapoints - num_success

    # Calculate the success percentage
    sp = (num_success / num_datapoints) * 100

    return sp


dirlist = []
for root, dirs, files in os.walk('results/'):
    dirlist.append(dirs)

dirlist = dirlist[0]

epsuc = 0
totsuc = 0

totosrsuc = 0
osrsuc = 0

psrsuc = 0
psrtot = 0

totpsrsuc = 0
totpsrtot = 0

for i, folder in enumerate(dirlist):
    epsuc = 0
    osrsuc = 0
    psrsuc = 0
    psrtot = 0
    for file in os.listdir('results/{}'.format(folder)):

        if 'success' in str(file):
            epsuc += 1

        if 'osrsuc' in str(file):
            osrsuc += 1

        if 'psrsuc' in str(file):
            psrsuc += 1

        if 'psr' in str(file):
            psrtot += 1

    print("Success percentage for episode {} is {}%.".format(i, 100*(epsuc/120)))
    print("Observation success percentage for episode {} is {}%.".format(i, 100*(osrsuc/120)))
    print("Prompt success percentage for episode {} is {}%. \n".format(i, 100*(psrsuc/psrtot)))

    totsuc += epsuc
    totosrsuc += osrsuc
    totpsrsuc += psrsuc
    totpsrtot += psrtot

print("Overall success percentage is {}%.".format(100*(totsuc/(120*len(dirlist)))))

print("Overall observation success percentage is {}%.".format(100*(totosrsuc/(120*len(dirlist)))))

print("Overall prompt success percentage for episode {} is {}%. \n".format(i, 100*(totpsrsuc/totpsrtot)))

tarobjsuc = np.load('target_success_current.pkl', allow_pickle=True)

for key in tarobjsuc.keys():
    
    total_dp = default_targets[key]

    if total_dp == 0:
        continue

    sum_dp = tarobjsuc[key]

    spec = success_percentage(total_dp, sum_dp)

    print("Success percentage for {} is {}%".format(key, spec))
