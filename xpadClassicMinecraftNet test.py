import pygame, sys
import pynput
import pygame
import sys
from pynput import keyboard
from pynput import mouse
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
from pynput.mouse import Button
from pynput.mouse import Controller
#import keyboard
import time
from pynput.keyboard import Key, Controller
import os
pygame.init()
keyboard = Controller()
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
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
            if event.button == 0:
                print("Button 'A' was pressed.")
                keyboard.press(Key.space)
                time.sleep(1)                
                keyboard.release(Key.space)
            if event.button == 1:
                print("Button 'B' was pressed.")
            if event.button == 3:
                print("Button 'Y' was pressed.")
                keyboard.press(Key.ctrl)
                keyboard.release(Key.ctrl)
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
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)


        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 0:
                print("X axis of Left Joystick is at: " + str(my_joystick.get_axis(0)))
            #if event.axis == 0:
                #print("Y axis of Left Joystick is at: " + str(my_joystick.get_axis(1)))
            #if event.axis == 0:
                #print("X axis of Right Joystick is at: " + str(my_joystick.get_axis(2)))
            #if event.axis == 0:
                #print("Y axis of Right Joystick is at: " + str(my_joystick.get_axis(3)))
                
        if event.type == pygame.JOYHATMOTION:
            if my_joystick.get_hat(0) == (0, 1):
                keyboard = Controller()
                print("DPad is Up")
                keyboard.press(Key.up)
            elif my_joystick.get_hat(0) == (0, -1):
                keyboard = Controller()
                keyboard.press(Key.down)
                print("DPad is Down")
            elif my_joystick.get_hat(0) == (-1, 0):
                keyboard = Controller()
                keyboard.press(Key.left)
                print("DPad is Left")
            elif my_joystick.get_hat(0) == (1, 0):
                keyboard = Controller()
                keyboard.press(Key.right)
                print("DPad is Right")
            elif my_joystick.get_hat(0) == (0, 0):
                keyboard = Controller()
                print("none")
                keyboard.release(Key.up)
                keyboard.release(Key.down)
                keyboard.release(Key.left)
                keyboard.release(Key.right)


