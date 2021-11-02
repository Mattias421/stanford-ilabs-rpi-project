"""
Stanford iLabs RPi Project

To be executed on the Pi, takes a photo and saves it

University of Sheffield 2021

Mattias Cross mgcross1@sheffield.ac.uk

Supported by:
Andrew Garrard a.garrard@shffield.ac.uk
Adam Funnell a.funnell@sheffield.ac.uk
"""

import argparse
from picamera import PiCamera #only works locally on pi
import time
import numpy as np
import os
import subprocess

#
# PARSE ARGS
#

parser = argparse.ArgumentParser(description='Settings for photo')
parser.add_argument('--photo_name', type=str, default='photo_'+str(np.random.randint(0, 1000000)) + '.jpg',
                    help='Name of photo, random if name not given')
parser.add_argument('--photo_path',type=str, default='photos_folder',
                    help='Path of photo, default is photos_folder')



args = parser.parse_args()

#
# MAKE FILE PATH
#

photosPath = os.path.join('ilabs_photos', args.photo_path)
if not os.path.exists(photosPath):
    os.makedirs(photosPath) 

#
# CAMERA TIME
#

print("Preparing camera for", args.photo_name)

camera = PiCamera()

#uncomment for camera preview
#camera.start_preview()
#time.sleep(5)
#camera.stop_preview()

#take photo and save to photosPath
photo = os.path.join(photosPath,args.photo_name)
camera.capture(photo)

print(args.photo_name + " saved to "+photosPath)

