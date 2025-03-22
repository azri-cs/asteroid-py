import pygame
from circleshape import CircleShape

class Shot(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		self.x = x
		self.y = y
		self.radius = radius

	def update(self, dt):
		self.x += self.velocity.x * dt
		self.y += self.velocity.y * dt
		self.position = pygame.math.Vector2(self.x, self.y)

	def draw(self, surface):
		pygame.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), self.radius)
