#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

reader = SimpleMFRC522()

def rfid_setup():
    print("[RFID] Version:", reader.READER)
    rfid_self_test()

def rfid_self_test():
    # Perform a self-test by trying to read; no dedicated self-test command exists
    try:
        id, text = reader.read()
        print("[RFID] Self-test OK")
        # Reinitializing might not be needed unless the read fails; handling that in except
    except Exception as e:
        print("[RFID] Reader failure, rebooting..", e)
        time.sleep(1)
        restart_system()  # Define or import this function for system restart

def check_for_card():
    try:
        id, text = reader.read_no_block()  # Non-blocking read
        if id:
            return id, text
        else:
            return None, None
    except Exception as e:
        print("Error reading from RFID reader:", e)
        return None, None
    finally:
        GPIO.cleanup()


def rfid_read():
    try:
        id, text = reader.read()
        return text
    finally:
        GPIO.cleanup()

def rfid_write(data):
    try:
        reader.write(data)
    finally:
        GPIO.cleanup()

# Example function to reboot the system; you might need sudo privileges for some commands
def restart_system():
    import os
    os.system('sudo reboot')
