import pygame, sys
import pynput
import pygame
import sys
from pynput import mouse
from pynput.mouse import Button, Controller
from pynput.mouse import Button
from pynput.mouse import Controller
#import keyboard
import time
import os
pygame.init()
keyboard = Controller()
mouse = Controller()
pygame.joystick.init()
my_joystick = pygame.joystick.Joystick(0)
my_joystick.init()
os.system('cls')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()

        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 2:
                print("Button 'X' was pressed.")
            if event.button == 0:
                print("Button 'A' was pressed.")
            if event.button == 1:
                print("Button 'B' was pressed.")
            if event.button == 3:
                print("Button 'Y' was pressed.")
            if event.button == 4:
                print("Button 'LB' was pressed.")
            if event.button == 5:
                print("Button 'RB' was pressed.")
            if event.button == 10:
                print("Button 'LT' was pressed.")
            if event.button == 8:
                print("Button 'RT' was pressed.")
            if event.button == 6:
                print("Button 'Back' was pressed.")
            if event.button == 7:
                print("Button 'Start' was pressed.")


                
        if event.type == pygame.JOYHATMOTION:
            if my_joystick.get_hat(0) == (0, 1):
                keyboard = Controller()
                mouse.move(0, -10)
                print("DPad is Up")
            elif my_joystick.get_hat(0) == (0, -1):
                keyboard = Controller()
                mouse.move(0, 10)
                print("DPad is Down")
            elif my_joystick.get_hat(0) == (-1, 0):
                mouse.move(-10, 0)
                print("DPad is Left")
            elif my_joystick.get_hat(0) == (1, 0):
                mouse.move(10, 0)
                print("DPad is Right")
            elif my_joystick.get_hat(0) == (0, 0):
                keyboard = Controller()
                print("none")
