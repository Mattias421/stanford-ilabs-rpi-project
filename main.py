"""
Stanford iLabs RPi Project: main.py

To be executed on host 

University of Sheffield 2021

Mattias Cross mgcross1@sheffield.ac.uk

Supported by:
Andrew Garrard a.garrard@shffield.ac.uk
Adam Funnell a.funnell@sheffield.ac.uk
Harry Day h.day@sheffield.ac.uk
"""

import argparse
import os
import numpy as np
import pandas as pd
import time
import subprocess

#
# PARSE ARGUEMENTS 
#

parser = argparse.ArgumentParser(description='Settings for iLabs Photostudio')
parser.add_argument('-n', '--experiment_name', type=str, default='experiment_'+str(np.random.randint(0, 1000000)),
                    help='Name of experiment, random if name not given. Should not contain spaces nor be duplicate')
parser.add_argument('-v', '--variables', nargs='+',
                    help='The names of all the experiment variables')

args = parser.parse_args()

#
# CREATE EXPERIMENT FOLDERS
#

try:
    experimentPath = os.path.join('experiments', args.experiment_name) 
    photosPath = os.path.join(experimentPath, 'photos')
    os.makedirs(experimentPath)
    os.makedirs(photosPath)
except:
    new_name = args.experiment_name + '_' + str(np.random.randint(0, 1000000))
    print('Experiment already exists, renaming experiment folder to :',new_name)
    experimentPath = os.path.join('experiments', new_name) 
    photosPath = os.path.join(experimentPath, 'photos')
    os.makedirs(experimentPath)
    os.makedirs(photosPath)

#
# LOAD IP(S)
#

ips = []
sshs = []

with open('pi_ip.txt') as f:
    for ip in f:
        ips.append(ip.strip())
with open('ssh_loc.txt') as f:
    for ssh in f:
        sshs.append(ssh.strip())

num_cameras = len(ips)

#
# INTRO
#

print()
print('Welcome to iLabs Photostudio, let\'s get started with experiment '+args.experiment_name+'!')
print()

#
# TAKE PHOTOS
#

variables = args.variables
album = [variables + ['camera ' + str(i) for i in range(num_cameras)]]

num_variables = len(variables)

takingPhotos = True

rowLength = num_variables + num_cameras

rowNum = 0

while takingPhotos:
    print()
    row = []
    rowNum += 1

    variables_string = ''

    for i in range(num_variables):
        value = input('What is the value of variable ' + variables[i] + '?: ')
        row.append(value)

        #to add to photo name
        variables_string += '_'+variables[i]+'='+value

    print('Taking photos...')

    for cam in range(num_cameras):
        photoName = 'photo'+str(rowNum)+'_cam'+str(cam+1)+variables_string+'.jpg'

        #take photo and save to pi
        command = "python3 /home/pi/stanford-ilabs-rpi-project/take_photo.py --photo_path " + args.experiment_name + ' --photo_name ' + photoName
        proc = subprocess.call(["ssh","-i",sshs[cam],ips[cam],command],stdout=subprocess.PIPE) #remotly connect to pi and take photo

        #send photo to host
        remote_path = ips[cam]+":ilabs_photos/" + args.experiment_name + "/" + photoName

        host_path = os.path.join(experimentPath,"photos")

        subprocess.run(["scp","-i",sshs[cam],remote_path,host_path])

        row.append(photoName) #append photo to csv

    album.append(row)

    end = input('Photos taken, press enter to continue or x to exit: ')
    if end == 'x':
        takingPhotos = False

#delete all photos from pi
for cam in range(num_cameras):
    command = "rm -r /home/pi/ilabs_photos"
    proc = subprocess.call(["ssh","-i",sshs[cam],ips[cam],command],stdout=subprocess.PIPE)

print('Photoshoot complete!')

albumDF = pd.DataFrame(album)

albumDF.to_csv(os.path.join(experimentPath,args.experiment_name + '.csv'))




