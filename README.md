# stanford-ilabs-rpi-project
Using Raspberry Pi cameras to create an iLab.

# Installation
Clone this repo onto the host and onto any pi cameras (make sure it is cloned in the /home/pi directory)

You may need to add some python packages if you don't have them already (Anaconda is the recommended command line interface for this program because it is easy to install missing packages) 

Currently pi IP addresses are manually entered in the main.py, this shall be automatic in the future

Follow https://www.raspberrypi.com/documentation/computers/remote-access.html AND https://raspi.tv/2012/how-to-set-up-keys-and-disable-password-login-for-ssh-on-your-raspberry-pi for passwordless connection to Pi's!

# Getting started
An example command is: main.py --experiment_name "my-first-experiment" --num_variables 1 num_cameras 1

This will set up a 1 camera experiment with 1 variable called "my-first-experiment". (make sure not to use and resticted characters or spaces)

# The end result
On the host there will be a CSV explaining which variables apply to which photo. The experiment photos can be found on each pi located in the /home/pi/ilabs_photos directory

![legoman_photo](/ilabs_photos/legoman/photo1_cam1.jpg)
