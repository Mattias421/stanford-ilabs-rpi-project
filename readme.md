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

Please consider the available power sockets and ethernets in your given lab, before getting started with the setup.

The software required is available on university computers via the software centre:

> VLC media player
> Moba xterm

## Connect to server

To connect to the iLabs server (`squirtle`), enter the following command in the MobaXterminal:

```
ssh ilabs@squirtle.shef.ac.uk
```

When prompted for a password, enter the password given to you with the iLabs kit.

## Raspberry Pi preperation

![ilabs_schema](https://github.com/Mattias421/stanford-ilabs-rpi-project/blob/main/experiments/objects/photos/ilabs_schema.drawio.png?raw=true)

A few steps are required to set up a Pi for iLabs. There are 3 Pis in the iLabs kit: *horsea*, *lapras* and *vaporeon*, each have a unique SSH key. 

### 1. Turn on Pi
Turning the Pi on is simple:
* Plug the ethernet cable into the Pi ethernet port.
* Then plug the power in. 

 The Pi should start flashing. During setup, turning the power on is the last thing you should do, follow this procedure.

### 2. SSH into Pi

In the moba xterminal (which should now be connected to *squirtle*), type:

```
ssh -i /home/ilabs/.ssh/$SSH_KEY -X pi@$PI_NAME
```

Replace `$SSH_KEY` and `$PI_NAME` with the Pi you would like to set up.

| Pi Name | SSH Key |
|------|-----|
| horsea | id_rsa_pi_1 |
| lapras | id_rsa_pi_2 |
| vaporeon | id_rsa_pi_3 |

### 3. Video stream

Now enter the following command (you can click the copy button on the right end of the command):

```
raspivid -o - -t 0 -w 800 -h 600 -fps 1 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8080/}' :demux=h264
```

The terminal should now display lots of text, this means the Pi has started streaming.

Open VLC media player and press `crtl+n`, then enter `rtsp://$PI_NAME:8080/`. You should now be able to see a video stream of the Pi. Adjust the camera as desired.

In the terminal, press `ctrl+c` then type `exit` to return to *squirtle*. Now return to step 1 and repeat for the other Pis.


# My first experiment

In the MobaXterminal, use `cd stanford-ilabs-rpi-project` to change into the ilabs directory. Your first command should look like this: 

```
python3 main.py --experiment_name $EXPERIMENT_NAME --num_variables $NUM_VARIABLES
```

Replace `$EXPERIMENT_NAME` with the name of your experiment, and $NUM_VARIABLES is the number variables in the experiement. For example, in the *Beams lab*, the number of variables is one (the beam). Refrain from using spaces in the experiment name and variables.
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

