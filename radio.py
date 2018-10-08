#!/usr/bin/env python

# simple internet radio
# Script by Giles Booth x
# adapted from motor control script by Tanya Fish
# www.suppertime.co.uk/blogmywiki
# stop flotilla daemon before running Python with Flotilla

import os
import sys
import flotilla

# Looks for the dock, and all of the modules we need
# attached to the dock so we can talk to them.

dock = flotilla.Client()
print("Client connected...")

while not dock.ready:
    pass

print("Finding modules...")
touch = dock.first(flotilla.Touch)

if touch is None:
    print("Some modules required were not found...")
    dock.stop()
    sys.exit(1)
else:
    print("Found. Running...")


# Looks for a Touch module and listens for an input
try:
    while True:
        if touch.one:
            os.system("mpc play 1")

        if touch.two:
            print("play 2")
            os.sysyem("mpc play 2")

        if touch.three:
            os.system("mpc play 3")

        if touch.four:
            os.system("mpc play 4")

# This listens for a keyboard interrupt, which is Ctrl+C and can stop the program
except KeyboardInterrupt: 
    os.system("mpc stop")
    print("Stopping Flotilla...")
    dock.stop()