import nfc
import subprocess
import time
import sys

clf = nfc.ContactlessFrontend('usb')

should_on = False

def change_led_value(flag):
    if flag == True:
        subprocess.call('irsend SEND_ONCE room-led.conf on', shell=True)
    else:
        subprocess.call('irsend SEND_ONCE room-led.conf off', shell=True)

def connected(tag):
    global should_on
    if should_on:
        should_on = False
    else:
        should_on = True
    change_led_value(should_on)

while True:
    after1s = lambda : time.time() - started > 1
    started = time.time()
    clf.connect(rdwr={'on-connect': connected}, terminate=after1s)
