import pygame
import randomNormal as rn
import time
import math


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode([1200, 800])
color = {
	'BLACK': (0, 0, 0),
	'WHITE': (255, 255, 255),
	'RED': (255, 0, 0),
	'GREEN': (0, 255, 0),
	'BLUE': (0, 0, 255)
}
screen.fill(color['BLACK'])

while True:
	time.sleep(0.001)

	randomZScore = rn.randomZScore()
	randomXCoord = randomZScore * 100 + 600

	pygame.draw.circle(screen, color['WHITE'], [round(randomXCoord), 600], round(100 / (abs(randomZScore) * 10 + 5)))
	print('randomXCoord: ' + str(randomXCoord))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	pygame.display.flip()