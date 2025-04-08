#!/usr/bin/python3

import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collide(self, sprite):
        distance_to_sprite = pygame.math.Vector2.distance_to(self.position, sprite.position)
        collision_distance = self.radius + sprite.radius
        return distance_to_sprite <= collision_distance
