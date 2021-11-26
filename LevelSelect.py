import pygame
import sys
from pygame.locals import *
from Engine.UserInterface import Button
import time

def main():
    pygame.init()

    lvl_screen = pygame.display.set_mode((400, 400))
    time.sleep(2)
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit() 
        
main()