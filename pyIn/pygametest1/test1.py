import pygame

pygame.init()

black = (0,0,0)

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((800,600)) 

displaying = True

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

#largeText = pygame.font.Font('freesansbold.ttf',25)
textBoxImage = pygame.image.load('sideMenuBox.png')	

while displaying:
	for event in pygame.event.get():
		if event.type == pygame.KEYUP and event.key == pygame.K_z:
			diplaying = False
			pygame.quit()
			quit()
		


	gameDisplay.fill((255, 255, 255))

	gameDisplay.blit(textBoxImage, (550,1))	
	pygame.display.flip()
	clock.tick(15)

	
