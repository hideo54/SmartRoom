import nfc
import subprocess
import time
import sys

clf = nfc.ContactlessFrontend('usb')

was_door_closed = False
is_door_closed = False
should_on = False

def change_led_value(flag):
    if flag == True:
        subprocess.call('irsend SEND_ONCE room-led.conf on', shell=True)
        print 'turned on'
    else:
        subprocess.call('irsend SEND_ONCE room-led.conf off', shell=True)
        print 'turned off'

def connected(tag):
    global is_door_closed
    is_door_closed = True

while True:
    was_door_closed = is_door_closed
    is_door_closed = False

    after1s = lambda : time.time() - started > 1
    started = time.time()
    clf.connect(rdwr={'on-connect': connected}, terminate=after1s)
    if is_door_closed == True and was_door_closed == False:
        if should_on == True:
            should_on = False
            change_led_value(should_on)
        else:
            should_on = True
            change_led_value(should_on)
