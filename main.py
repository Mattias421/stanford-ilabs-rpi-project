"""
Stanford iLabs RPi Project: main.py

To be executed on host 

University of Sheffield 2021

Mattias Cross mgcross1@sheffield.ac.uk

Supported by:
Andrew Garrard a.garrard@shffield.ac.uk
Adam Funnell a.funnell@sheffield.ac.uk
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
parser.add_argument('--experiment_name', type=str, default='experiment_'+str(np.random.randint(0, 1000000)),
                    help='Name of experiment, random if name not given')
parser.add_argument('--num_variables', type=int, default=1,
                    help='Number of variables in the experiment')
parser.add_argument('--num_cameras', type=int, default=1,
                    help='Number of cameras used in the experiment') #redundent do to ip file

args = parser.parse_args()

#
# CREATE EXPERIMENT FOLDERS
#

experimentPath = os.path.join('experiments', args.experiment_name) #should not contain spaces nor be duplicate
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

#
# TAKE PHOTOS
#

print()
print('Welcome to iLabs Photostudio, let\'s get started with experiment '+args.experiment_name+'!')



album = []

takingPhotos = True

rowLength = args.num_variables + args.num_cameras

rowNum = 0

while takingPhotos:
    print()
    row = []
    rowNum += 1

    for i in range(args.num_variables):
        row.append(input('What is the setting of variable ' + str(i) + '?: '))

    print('Taking photos...')

    for cam in range(len(ips)):
        photoName = 'photo'+str(rowNum)+'_cam'+str(cam+1)+'.jpg'

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

print('Photoshoot complete!')

albumDF = pd.DataFrame(album)

albumDF.to_csv(os.path.join(experimentPath,args.experiment_name + '.csv'))




