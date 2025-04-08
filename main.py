#!/usr/bin/python3

import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {str(SCREEN_WIDTH)}")
    print(f"Screen height: {str(SCREEN_HEIGHT)}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    asteroids_destroyed = 0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    font = pygame.font.Font(None, 28)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for sprite in asteroids:
            for shot in shots:
                if sprite.collide(shot):
                    shot.kill()
                    sprite.kill()
                    asteroids_destroyed += 1
            if sprite.collide(player):
                print("Game over!")
                sys.exit(0)
        for sprite in drawable:
            sprite.draw(screen)
        asteroid_text = font.render(f"Asteroids Destroyed: {asteroids_destroyed}", True, "green")
        screen.blit(asteroid_text, (10, 10))
        pygame.display.flip()
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
