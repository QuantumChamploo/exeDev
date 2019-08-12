import pygame
from pygame import font 
#from images import *


pygame.init()
x = pygame.font.get_fonts()
for fnts in x:
	if fnts == 'freesandsbold':
		print ("found it")

black = (0,0,0)

textBoxImage = pygame.image.load('images/sideMenuBox.png')	
largeText = pygame.font.Font('fonts/FreeSansBold.ttf',25)
hldtext = "Press Z to quit"

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((800,600)) 

displaying = True

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

#largeText = pygame.font.Font('freesansbold.ttf',25)


while displaying:
	for event in pygame.event.get():
		if event.type == pygame.KEYUP and event.key == pygame.K_z:
			diplaying = False
			pygame.quit()
			#quit()
		


	gameDisplay.fill((255, 255, 255))

	gameDisplay.blit(textBoxImage, (550,1))	
	BottomSurf, BottomRect = text_objects(hldtext, largeText)
	BottomRect.center = ((200),(370))
	gameDisplay.blit(BottomSurf, BottomRect)
	pygame.display.flip()
	clock.tick(15)

	
