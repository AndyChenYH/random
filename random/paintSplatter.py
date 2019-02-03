import pygame
import randomNormal as rn
import time
import math
import sys


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
	randFill = round(rn.randomZScore() * 20 + 150) 
	pygame.draw.circle(screen, (randFill, randFill, 255), [round(rn.randomZScore() * 150 + 600), round(rn.randomZScore() * 150 + 400)], round(abs(rn.randomZScore()) * 2 + 3))	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	pygame.display.flip()
