my coffee app
=============

A tipycall controlled app in which an arduino takes a twitter message and turns it into coffee 

my_coffee_app uses a Python script to establish a serial connection with an Arduino Uno, which takes an input signal from the script and sends a +5 volts signal to one of its digital pins, which we'll consider as the Arduino's outputs and the coffee maker's inputs (coffee will be written with a capital c from now on, since we love Coffee).

I'll split this project into three parts, the Python code, the Arduino code and the actual assembling of both codes to make our Coffee maker make Coffee whenever we want, you know, cuz we programmers are badass. The Arduino code is self-explanatory once you get to see it, so I won't be giving it a lot of explanation... plus, it's not larger than thirty lines of code. I'll also assume you are on a Linux system and have a simple non-programmable Coffee maker. There's not much diference from a Linux based OS from a Windows OS or Mac OS in order for this project to work, so feel free to use this code aslong as you adapt it to your system.

In order to make our Coffee maker work as we want it to, you'll need four components:

An Arduino UNO.

A Coffee maker.

A power switch tail (with relays).

A twitter account.

To control the flow of current through the Coffee maker, relays are prefered. Relays are current-controlled switches that let current flow whenever the coil within the relay gets some current...

This project is currently being developed, I'll upload the source code and complete this readme within the next 15 days
