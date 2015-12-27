from flask import Flask, jsonify
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',
        }

DOT_LENGTH = 0.5  # seconds value for dot '.'


@app.route("/led/api/v1.0/morse/<string:message>", methods=['GET'])
def morse(message):
    """Return a JSON Object of the message converted to Morse Code"""
    morse_code = ""
    message = parse_message(message)
    for char in message:
        toggle_led(False)
        time.sleep(DOT_LENGTH * 3)  # pause between characters
        if char == ' ':
            morse_code += char
            time.sleep(DOT_LENGTH * 7)  # pause between words
        else:
            for code in CODE[char.upper()]:
                morse_code += code
                time.sleep(DOT_LENGTH)  # pause between code elements
                if code == '.':
                    toggle_led(True)
                    time.sleep(DOT_LENGTH)  # pause between dots
                else:
                    toggle_led(True)
                    time.sleep(DOT_LENGTH * 3)  # pause between dashes
                toggle_led(False)
    if morse_code == "":
        morse_code = "error"

    return jsonify({'code': morse_code})


def parse_message(message):
    """Return a message that can be converted to Morse Code. Otherwise
        return an empty String"""
    if "%20" in message:
        message = message.replace("%20", " ")
    for char in message:
        if char.upper() not in CODE.keys() and char != ' ':
            return ""
    return message


def toggle_led(is_on):
    """Toggles the LED connected to GPIO pin 18 on the Raspberry Pi"""
    GPIO.output(18, is_on)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
