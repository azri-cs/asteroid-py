import sys
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
	pygame.init()
	print("Starting Asteroids!")
	print("Screen width:", SCREEN_WIDTH)
	print("Screen height:", SCREEN_HEIGHT)
	fps_clock = pygame.time.Clock()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroid_groups = pygame.sprite.Group()
	shots_group = pygame.sprite.Group()

	Shot.containers = (shots_group, updatable, drawable)
	Player.containers = (updatable, drawable)
	player = Player(x, y)
	player.shots_group = shots_group

	Asteroid.containers = (asteroid_groups, updatable, drawable)
	AsteroidField.containers = (updatable,)
	asteroid_field = AsteroidField()
	asteroid_field.containers = updatable

	while (True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		dt = fps_clock.tick(60) / 1000

		screen.fill((0, 0, 0))

		updatable.update(dt)

		# collision check
		for obj in asteroid_groups:
			if obj.check_collision(player):
				print("Game over!")
				sys.exit()

			for bullet in shots_group:
				if bullet.check_collision(obj):
					bullet.kill()
					obj.split()

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()


if __name__ == "__main__":
	main()
