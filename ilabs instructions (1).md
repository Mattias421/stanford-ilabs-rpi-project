# Stanford iLabs RPi Project
Originating from the 1990s, Stanford University implemented remote laboratory's "[iLabs](http://ilabs.education)". This repository provides an open source framework using readily available Raspberry Pi technology to introduce iLabs to any labaratory. 

---

# Set up

## Prerequisites
The hardware required to set up RPi iLabs at the University of Sheffield is:

> The iLabs kit \
> 3 power outlets \
> 3 ethernet ports \
> A computer/laptop connected to the eduroam network

The software required is:

> VLC media player \
> Moba xterm

## Connect to server

To connect to the iLabs server (`squirtle`), enter the following command in the moba xterminal:

```
ssh ilabs@squirtle.shef.ac.uk
```

When prompted for a password, enter the password given to you with the iLabs kit.

## Pi preperation

A few steps are required to set up a Pi for iLabs. There are 3 Pis in the iLabs kit: *horsea*, *lapras* and *vaporeon*. The following instructions use *horsea* as an example. Replace *horsea* with another Pi name to set up another Pi and use their correspoding SSH key.

### 1. Turn on Pi

Plug the [camera](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera) and ethernet port. Then plug the power in. The Pi should start flashing.

### 2. SSH into Pi

In the moba xterminal (which should now be connected to *squirtle*), type:

```
ssh -i /home/ilabs/.ssh/id_rsa_pi_1 -X pi@horsea
```

Replace `id_rsa_pi_1` with `id_rsa_pi_2` for the `lapras` Pi etc.

### 3. Video stream

Now enter:

```
raspivid -o - -t 0 -w 800 -h 600 -fps 12 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8080/}' :demux=h264
```

Open VLC media player and press `crtl+n`, then enter `rtsp://horsea:8080/`. You should now be able to see a video stream of the Pi. Adjust the camera as desired.

In the terminal, press `ctrl+c` then type `exit` to return to *squirtle*.


# My first experiment

|Use `cd stanford-ilabs-rpi-project` to change into the ilabs directory. Your first command should look like this: 

```
python3 main.py --experiment_name "my_first_experiment" --num_variables 1
```

## Experiment

It is time to begin capturing the experiment. Set your lab equipment to it's desired state. You will be prompted to enter the value of each experiment variable and then the images will be captured. 

```
What is the value of variable 0? LegoMan
...
Photos taken, press enter to continue or x to exit: x
```

Repeat as desired, press `x` when prompted to exit the program.

## The result

There will be a [CSV](https://github.com/Mattias421/stanford-ilabs-rpi-project/blob/main/experiments/objects/objects.csv) explaining which variables apply to which photo. The experiment photos can be found in the [photos folder](https://github.com/Mattias421/stanford-ilabs-rpi-project/tree/main/experiments/objects/photos) of each experiment. These can be viewed in the moba file explorer.

This CSV and photos folder can now be sent to stanford to 

Disclaimer: Using this project will not make you better at photography, it only helps with taking multiple photos of the same experiment state at the same time!

![legoman_photo](https://github.com/Mattias421/stanford-ilabs-rpi-project/blob/main/experiments/objects/photos/photo1_cam1.jpg?raw=true)

# The Team
Andrew Garrard, Adam Funnell, Mattias Cross @ The University of Sheffield.

