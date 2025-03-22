import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, \
	PLAYER_SHOOT_COOLDOWN
from shot import Shot


class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.x = x
		self.y = y
		self.rotation = 0
		self.timer = 0

	def triangle(self):
			forward = pygame.Vector2(0, 1).rotate(self.rotation)
			right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
			a = self.position + forward * self.radius
			b = self.position - forward * self.radius - right
			c = self.position - forward * self.radius + right
			return [a, b, c]

	def draw(self, screen):
		pygame.draw.polygon(screen, "blue", self.triangle(), 2)

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def update(self, dt):
		keys = pygame.key.get_pressed()
		self.timer -= dt

		if keys[pygame.K_a]:
			self.rotate(-dt)

		if keys[pygame.K_d]:
			self.rotate(dt)

		if keys[pygame.K_w]:
			self.move(dt)

		if keys[pygame.K_s]:
			self.move(-dt)

		if keys[pygame.K_SPACE]:
			self.shoot()

	def shoot(self):
		if self.timer > 0:
			return
		shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
		shot_velocity = pygame.Vector2(0, 1)
		shot_velocity.rotate_ip(self.rotation)
		shot_velocity = shot_velocity * PLAYER_SHOOT_SPEED
		shot.velocity = shot_velocity
		self.shots_group.add(shot)
		self.timer = PLAYER_SHOOT_COOLDOWN
		return shot
