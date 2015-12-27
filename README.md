# Morse Code
This project turns your Raspberry Pi into a RESTful web server using Python and Flask.
The Pi can receive a message, convert it to Morse Code, and then flash an LED in Morse code and return the message in code form.


## Requirements:
1. Raspberry Pi connected to local network (1)
2. Breadboard (1)
3. Male-to-female jumper cables (2)
4. 220ohm* Resistor (1) *Will vary depending on voltage of your LED
5. LED (1)


## Raspberry Pi Setup
A great setup tutorial by Simon Monk can be found on [oreilly.com](http://razzpisampler.oreilly.com/ch03.html)


For a quick setup you can follow the instructions here:

0. You must have [Flask](http://flask.pocoo.org/) installed on your Pi. Run the following commands on your Pi
??*`sudo apt-get install python-pip`
??*`sudo pip install flask`

1. Connect LED to the breadboard - Long lead in **5e** and short lead in **6e**

2. Connect resistor to the breadboard - **1c** and **6c**

3. Connect M-to-F jumper cables from the breadboard to the Pi. Connect one cable from **6a** in the bread board to
a ground (**GND**) GPIO pin on the Raspberry Pi. Connect the second cable from **1a** on the breadboard to GPIO **18** on the Raspberry Pi.
**Note: if you are
 connecting to different GPIO pins you will need to change the code in [morse_code_server.py](../morse_code_server.py)**

4. Your Raspberry Pi setup is now finished and can be tested by executing the following commands:
??*`sudo python`
??*`import RPi.GPIO as GPIO`
??*`GPIO.setmode(GPIO.BCM)`
??*`GPIO.setup(18, GPIO.OUT)`
??*`GPIO.output(18, True)`
??*`GPIO.output(18, False)`


## Python (Flask) Server Setup
1. Clone this repository

    `git clone https://github.com/trevorhalvorson/MorseCode`

2. Start server

    `sudo python MorseCode/morse_code_server.py`

    Your should see a response: `Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)`


## Try It!
**You must be connected to the same network as your Pi**
1. Visit `http://X.X.X.X:5000/led/api/v1.0/morse/MESSAGE` **(Replace the Xs with your Pi's IP and MESSAGE with any message you
want to see flash in Morse Code).** After the LED has finished flashing you will see a JSON response of your message translated to code.

2. Have an Android device? Download this sample application that shows how to easily talk to your Pi using the Flask API in this project:
https://github.com/trevorhalvorson/RPi_LED_Sample

## Known Issues
1. Any characters not found in the CODE dictionary in [morse_code_server.py](../morse_code_server.py) will cause an error. If you would like to expand
this dictionary please fork this project and send a pull request.