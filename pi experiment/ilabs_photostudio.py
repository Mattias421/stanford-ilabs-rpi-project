"""
Stanford iLabs RPi Project: iLabs Photostudio

This is temp code to test capturing a photo on a single pi locally

University of Sheffield 2021

Mattias Cross mgcross1@sheffield.ac.uk

Supported by:
Andrew Garrard a.garrard@shffield.ac.uk
Adam Funnell a.funnell@sheffield.ac.uk
"""

import argparse
from picamera import PiCamera #only works locally on pi
import os
import numpy as np
import pandas as pd
import time

#python3 ilabs_photostudio.py --experiment_name "Legoman" --num_variables 2 --num_cameras 1

#
# PARSE ARGUEMENTS 
#

parser = argparse.ArgumentParser(description='Settings for iLabs Photostudio')
parser.add_argument('--experiment_name', type=str, default='experiment_'+str(np.random.randint(0, 1000000)),
                    help='Name of experiment, random if name not given')
parser.add_argument('--num_variables', type=int, default=2,
                    help='Number of variables in the experiment')
parser.add_argument('--num_cameras', type=int, default=2,
                    help='Number of cameras used in the experiment')

args = parser.parse_args()

#
# CREATE EXPERIMENT FOLDERS
#

experimentPath = os.path.join('experiments', args.experiment_name)

try:
    os.makedirs(experimentPath)
except:
    print(experimentPath, "Already exists! Renaming...")
    experimentPath = os.path.join('experiments', args.experiment_name + "_" + str(np.random.randint(0, 1000000)))
    os.makedirs(experimentPath)

photosPath = os.path.join(experimentPath, 'photos')
os.makedirs(photosPath)

#
# PREPARE CAMERA
#

print("Preparing cameras for", experimentPath)

camera = PiCamera()

camera.start_preview()
time.sleep(5)
camera.stop_preview()

#
# TAKE PHOTOS
#

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

    for i in range(args.num_cameras):
        photoName = 'photo'+str(rowNum)+'_cam'+str(i+1)+'.jpg'
        newPhotoPath = os.path.join(photosPath, photoName)

        #take photo and save to photosPath
        camera.capture(newPhotoPath)
        row.append(photoName)

    album.append(row)

    end = input('Photos taken, press enter to continue or x to exit: ')
    if end == 'x':
        takingPhotos = False

print('Photoshoot complete!')

albumDF = pd.DataFrame(album)

albumDF.to_csv(os.path.join(experimentPath,args.experiment_name + '.csv'))




