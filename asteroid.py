#!/usr/bin/python3

import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "red", self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
	    self.kill()
	    destroyed = 0
	    if self.radius <= ASTEROID_MIN_RADIUS:
	         destroyed = 1
	         return destroyed
	    split_angle = random.uniform(20, 50)
	    vect1 = self.velocity.rotate(split_angle)
	    vect2 = self.velocity.rotate(-split_angle)
	    self.radius = self.radius - ASTEROID_MIN_RADIUS
	    asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
	    asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)
	    asteroid1.velocity = vect1 * 1.2
	    asteroid2.velocity = vect2 * 1.2
	    return destroyed
