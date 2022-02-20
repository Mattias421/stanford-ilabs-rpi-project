# Stanford iLabs RPi Project
Originating from the 1990s, Stanford University implemented remote laboratory's "[iLabs](http://ilabs.education)". This repository provides an open source framework using readily available Raspberry Pi technology to introduce iLabs to any labaratory. 

---

# Set up

## Prerequisites
The hardware required to set up RPi iLabs at the University of Sheffield is:

> Linux server x 1
Rasberry Pi x 3
High quality RPi camera x 3

The software used to run the code is:

> Python 
SSH

## SSH setup

SSH allows the server (the host) to communicate with the Raspberry Pis (the clients). Use the server terminal to generate [ssh keypairs](https://www.raspberrypi.com/documentation/computers/remote-access.html) for each Pi. It is encouraged to name each key uniquely. You should now have a private and public key for each Pi.

## Pi preperation

A few steps are required to set up a Pi for iLabs. The follow the following steps for each Pi.

### 1. Installing the code to each Raspberry pi

Clone this repo onto the host and onto each Raspberry Pi cameras (make sure it is cloned in the /home/pi directory): 

```
git clone git@github.com:Mattias421/stanford-ilabs-rpi-project.git
```

The `/home/pi/stanford-ilabs-rpi-project/` directory should appear on the Pi. It contains code to capture images and send them to the server.

### 2. Add an SSH key

Copy the text of one of the public ssh keys (`.pub`) from the server and paste it in the `~/.ssh/authorized_keys` file. On a piece of paper, write the name of the key you used and the [ip address](https://www.raspberrypistarterkits.com/how-to/find-raspberry-pi-ip-address/) of the Pi.

### 3. Configuration

Access the `raspi-config` tool:

```
sudo raspi-config
```

Enter `5 Interfacing Options` and enable the camera (`P1 Camera`) and SSH (`P2 SSH`). Follow [this](https://raspi.tv/2012/how-to-set-up-keys-and-disable-password-login-for-ssh-on-your-raspberry-pi) guide to set up passwordless SSH on the Pi. For use on the University of Sheffield's network, the Pis must be [registered](https://csrs.shef.ac.uk/wirelessregister.php) and [configured](https://blog.sebastian-martens.de/development/raspberry-pi-hidden-ssid/).

## Configure server 

Configuring the server is easy. Enter the IP address of each Pi on each line of the [pi_ip.txt](https://github.com/Mattias421/stanford-ilabs-rpi-project/blob/main/pi_ip.txt) file and its matching private ssh key file location in [ssh_loc.txt](https://github.com/Mattias421/stanford-ilabs-rpi-project/blob/main/ssh_loc.txt).

# My first experiment

You're first command should look like this: 

```
python3 main.py --experiment_name "my_first_experiment" --num_variables 1 --setup True
```

For future experiments you can remove the `--setup` arguement. 

## Set up

The camera set up process should now be activated. Images will be caputered and placed in the `setup` folder. If the images are correctly positioned, press `y`. If not, reposition the cameras and press `n`.

## Experiment

Now that the cameras are set up, it is time to begin capturing the experiment. Set your lab equipment to it's desired state. You will be prompted to enter the value of each experiment variable and then the images will be captured. 

```
What is the value of variable ? LegoMan

...

Photos taken, press enter to continue or x to exit: x
```

Repeat as desired, press `x` when prompted to exit the program.

## The result

There will be a [CSV](https://github.com/Mattias421/stanford-ilabs-rpi-project/blob/main/experiments/objects/objects.csv) explaining which variables apply to which photo. The experiment photos can be found in the [photos folder](https://github.com/Mattias421/stanford-ilabs-rpi-project/tree/main/experiments/objects/photos) of each experiment. Photos are also saved to each Pi.

Disclaimer: Using this project will not make you better at photography, it only helps with taking multiple photos of the same experiment state at the same time!

![legoman_photo](/experiments/objects/photos/photo1_cam1.jpg)

# The Team
Andrew Garrard, Adam Funnell, Mattias Cross @ The University of Sheffield.

