# Stanford iLabs RPi Project
Originating from the 1990s, Stanford University implemented remote laboratory's "[iLabs](http://ilabs.education)". This repository provides an open source framework using readily available Raspberry Pi technology to introduce iLabs to any labaratory. 

![ilabs_icon](https://github.com/Mattias421/stanford-ilabs-rpi-project/blob/main/experiments/objects/photos/rpi_pokemon.jpg?raw=true)

---

# Set up

## Prerequisites
The hardware required to set up RPi iLabs at the University of Sheffield is:

> The iLabs kit
> 3 power outlets (and cables of suitable length)
> 3 ethernet ports (and cables of suitable length)
> A computer/laptop connected to the eduroam network
> Keyboard, mouse, HDMI monitor

Please consider the available power sockets and ethernets in your given lab, before getting started with the setup.

The software required is available on university computers via the software centre:

> Moba xterm

## Connect to server

To connect to the iLabs server (`squirtle`), enter the following command in the MobaXterminal:

```
ssh ilabs@squirtle.shef.ac.uk
```

When prompted for a password, enter the password given to you with the iLabs kit.

## Raspberry Pi preperation

![ilabs_schema](https://github.com/Mattias421/stanford-ilabs-rpi-project/blob/main/experiments/objects/photos/ilabs_schema.jpg?raw=true)

A few steps are required to set up a Pi for iLabs. There are 3 Pis in the iLabs kit: *horsea*, *lapras* and *vaporeon*. 

### 1. Turn on Pi
Turning the Pi on is simple:
* Plug the ethernet, keyboard, mouse and HDMI cable into the Pi ethernet port.
* Then plug the power in. 

 The Pi should start flashing. During setup, turning the power on is the last thing you should do, follow this procedure. 

### 2. Video stream
Viewing the monitor, use the keyboard and mouse to open a terminal and type `./video`. Camera feedback should now be visable, use this to focus your lenses. 

Once satisfied, press ctrl+c.

Repeat these steps for each Pi.

# My first experiment

In the MobaXterminal, use `cd stanford-ilabs-rpi-project` to change into the ilabs directory. Your first command should look like this: 

```
python3 main.py --experiment_name $EXPERIMENT_NAME --variables $VARIABLES
```

Replace `$EXPERIMENT_NAME` with the name of your experiment, and $VARIABLES with the name of each variable in the experiement. Refrain from using spaces in the experiment and variable names.

Here is an example command:

```
python3 main.py --experiment_name hydro --variables mass height
```

## Experiment

It is time to begin capturing the experiment. Set your lab equipment to it's desired state. You will be prompted to enter the value of each experiment variable and then the images will be captured. 

```
What is the value of variable 0? $VARIABLE_VALUE
...
Photos taken, press enter to continue or x to exit: $PRESS_ENTER_OR_x
```

Repeat as desired, press `x` when prompted to exit the program.

## The result

The output of this process is a folder full of photos, and a [CSV](https://github.com/Mattias421/stanford-ilabs-rpi-project/blob/main/experiments/objects/objects.csv) file that lists all the photo filenames in an organised fashion. This csv and the photos folder can be sent to Stanford where they will be processed into a working iLab.

You can view the photos in the MobaXterminal file navigation window (left of the terminal), and can drag&drop them over to your PC.

Disclaimer: Using this project will not make you better at photography, it only helps with taking multiple photos of the same experiment state at the same time!

![legoman_photo](https://github.com/Mattias421/stanford-ilabs-rpi-project/blob/main/experiments/objects/photos/photo1_cam1.jpg?raw=true)

# The Team
Development - Andrew Garrard, Adam Funnell, Mattias Cross

Testing - Harry Day, Shankar Lal Meghwar

The University of Sheffield.

