#!/usr/bin/python3

import pygame
from constants import *
import time

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {str(SCREEN_WIDTH)}")
    print(f"Screen height: {str(SCREEN_HEIGHT)}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
