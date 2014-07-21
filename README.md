my coffee app
=============

A tipycall controlled app in which an arduino takes a Twitter message and turns it into coffee 

my_coffee_app uses a Python script to establish a serial connection with an Arduino Uno, which takes an input signal from the script and sends a +5 volts signal to one of its digital pins, which we'll consider as the Arduino's outputs and the coffee maker's inputs.

I'll split this project into two parts, the Python and the Arduino code. The Arduino code is self-explanatory once you get to see it, so I won't be giving it a lot of explanation... plus, it's not larger than thirty lines of code. I'll also assume you are on a Linux system and have a simple non-programmable Coffee maker. There's not much diference from a Linux based OS from a Windows OS or Mac OS in order for this project to work, so feel free to use this code as long as you adapt it to your system.

In order to make our Coffee maker work as we want it to, you'll need three components and a Twitter account:

An Arduino UNO.

A Coffee maker.

A power switch tail (with relays).


To control the flow of current through the Coffee maker, relays are prefered. Relays are current-controlled switches that let current from the wall outlet flow, whenever the coil within the relay gets some current. Usually, relays need more electric current than the Arduino can provide. To fix this, a transistor it's needed. However, the power switch tail can be powered only with the small Arduino´s output current, so no transistors are required (Yayyy!). 

Python script
=============


This script is used to communicate your Twitter messages to your computer, and then your computer sends data to the Arduino in order to turn off and on the power switch tail. There's a Twitter Python library which you'll have to pip install (sudo pip install twitter). This will allow you to get the timeline messages you post, and then compare them to your "make coffee" command, using string comparison (I used the boolean comparators == , !=). If your timeline message is not a duplicate and is equal to your "make coffee" command, then with the help of the Python Serial lib, the script will send data to the Arduino by calling the write function.

Firmware (Arduino code)
=============

This code basically sends a HIGH signal to one of the power switch tail inputs, when it gets data from the computer. Once the data is received, using the Serial functions of Arduino, a call to the Serial.available() function is made, in order to check if there´s data in the incoming buffer. Once this buffer gets data, the Arduino has to check whether it´s getting bytes or not, by calling the Serial.read() function. If not, then a LOW signal (0 volts) is sent to the switch. This is made so when the user wants to stop making coffee, the Arduino won´t power the coffee machine. That is, to close the serial ports of the Python script. Since I´m doing this project on my Raspberry Pi, I added a one second delay after I call the write function, because I didn´t want to test my Raspberry´s CPU. Because of that, I put a three seconds delay to give the Arduino some time to read its input buffer. Feel free to play with these delays.   

