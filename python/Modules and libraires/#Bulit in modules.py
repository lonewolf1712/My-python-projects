#Bulit in modules

import math

radius = 5
area = math.pi * math.pow(radius, 2)
print("Area of circle:", area)

import datetime

now = datetime.datetime.now()
print("Current date and time:", now)

# Custom format
print("Formatted:", now.strftime("%d-%m-%Y %H:%M:%S"))

import os

print("Files and folders in current directory:")
for item in os.listdir():
    print("-", item)

import sys

print("Command-line arguments:")
for arg in sys.argv:
    print("-", arg)

import random

roll = random.randint(1, 6)
print("You rolled a", roll)
