# stanford-ilabs-rpi-project
Using Raspberry Pi cameras to create an iLab.

# Installation
Clone this repo onto the host and onto any pi cameras (make sure it is cloned in the /home/pi directory)

Currently pi IP addresses are manually entered in the main.py, this shall be automatic in the future

# Getting started
An example command is: main.py --experiment_name "my-first-experiment" --num_variables 1 num_cameras 1

This will set up a 1 camera experiment with 1 variable called "my-first-experiment". (make sure not to use and resticted characters or spaces)

# The end result
On the host there will be a CSV explaining which variables apply to which photo. The experiment photos can be found on each pi located in the /home/pi/ilabs_photos directory
