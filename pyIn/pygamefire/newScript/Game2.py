import pygame
from pygame.locals import *
import tmx
#import pygameMenu
#from pygameMenu.locals import *
import glob
import os

from Player2 import Player
from classes.statebasedSprite import statebasedSprite
from classes.SpriteLoop import SpriteLoop 
from classes.npcSprite import npcSprite
from classes.removableSprite import removableSprite
from classes.enemySprite import enemySprite


import sys
bundle_dir = sys._MEIPASS + '/'

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
COLOR_BLUE = (12, 12, 200)
COLOR_BACKGROUND = [128, 0, 128]
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_MAROON =  (40, 0, 40)
MENU_BACKGROUND_COLOR = (228, 55, 36)
COLOR_LIMEGREEN = (0, 255, 127)
COLOR_LIGHTCORAL  =  (240, 128, 128)


""" 
					Aux method used in processesing images to their text boxes
"""


def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()



def text_objectsColor(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

class Game(object):

    def __init__(self, screen):
        # the screen is a pygame display surface
        self.screen = screen
        # the save field will be filled with the CSV entries from our save files
        self.save = []
        self.samePlayer = False


    
    def fadeOut(self):
        																	
        clock = pygame.time.Clock()
        blackRect = pygame.Surface(self.screen.get_size())
        blackRect.set_alpha(100)
        blackRect.fill((0,0,0))
        																		# Continuously draw a transparent black rectangle over the screen
        																		# to create a fadeout effect
        for i in range(0,5):
            clock.tick(15)
            self.screen.blit(blackRect, (0,0))  
            pygame.display.flip()
        clock.tick(15)
        screen.fill((255,255,255,50))
        pygame.display.flip()
        																		# *** *** ***
    def initArea(self, mapFile):												# initArea
																				# *** *** ***
																				
        
        self.tilemap = tmx.load(mapFile, screen.get_size())
        self.mapFile = mapFile

        
        # These fields are sprite class abstract groups. We will use the tmx API to do remove/kill and parse through the games
        # sprite instantiations 

        # Players is for just player class 
        self.players = tmx.SpriteLayer()

        # Objects is all things that will be updated
        self.objects = tmx.SpriteLayer()

        # Sub groups used to make code simpler and easier to read
        self.projectiles = tmx.SpriteLayer()
        self.collision = tmx.SpriteLayer()
        self.interactable = tmx.SpriteLayer()
        self.named = tmx.SpriteLayer()
        self.removable = tmx.SpriteLayer()
        self.enemies = tmx.SpriteLayer()
        #self.sprites = []


        startCell = self.tilemap.layers['triggers'].find('playerStart')[0]
        if self.samePlayer == False:

            self.player = Player((startCell.px, startCell.py), 
                                 startCell['playerStart'], self.players) 
        else:
            hld1 = self.player.hearts
            hld2 = self.player.WOFlevel
            hld3 = self.player.magicPer            
            self.player = Player((startCell.px, startCell.py), 
                                 startCell['playerStart'], self.players) 
            self.player.hearts = hld1
            self.player.WOFlevel = hld2  
            self.player.magicPer = hld3         

            # self.player.rect = pygame.Rect((startCell.px, startCell.py), (64,64)) 
            # self.player.orient =  startCell['playerStart']
            # self.players.set_view(self.screen)  
            # self.players.draw(self.screen)
            # self.player.setSprite()                         
																				        # Initializing other animated sprites
        try:
            for cell in self.tilemap.layers['sprites'].find('src'):
                SpriteLoop((cell.px,cell.py), cell, self.objects)
            for cell in self.tilemap.layers['npcSprites'].find('src'):
                npcSprite((cell.px,cell.py), cell,'down', self.objects, self.collision, self.interactable, self.named)

           # for cell in self.tilemap.layers['statebasedSprites'].find('src'):


                #if self.save[cell['saveIndex']] == 'true':
                #   statebasedSprite((cell.px,cell.py), cell, self.objects, self.collision, self.interactable)

            hld = 0

            print (mapFile)

            if mapFile == bundle_dir + 'WallsOrFireBalls.tmx':
                self.player.transitionIn = True
                print (self.player.transitionIn)

                
                for cell in self.tilemap.layers['enemySprites'].find('src'):
                    print (str(self.player.WOFlevel) + "this is the level i should be at")
                    if hld < self.player.WOFlevel + 3:
                        enemySprite((cell.px,cell.py), cell, 'down', self.objects, self.collision, self.removable, self.named, self.enemies)
                        hld += 1


            else:
                for cell in self.tilemap.layers['enemySprites'].find('src'):
                    enemySprite((cell.px,cell.py), cell, 'down', self.objects, self.collision, self.removable, self.named)

            hldSprites = self.tilemap.layers['removableSprites'].find('src')
            
            for cell in hldSprites:
               
                removableSprite((cell.px,cell.py), cell, self.objects, self.collision, self.removable)                
   






        # In case there is no sprite layer for the current map
        except KeyError:
            print ('key error')
            pass
        else:
            self.tilemap.layers.append(self.objects)
        
            

        # Initializing player sprite


        self.tilemap.layers.append(self.players)
        self.tilemap.set_focus(self.player.rect.x, self.player.rect.y) 


    def main(self):
        clock = pygame.time.Clock()
        print ('in main')
        
        # maybe dont deen bundle dir
        self.initArea(bundle_dir + 'WallsOrFireBalls.tmx')
        

        

        gameDisplay = pygame.display.set_mode((800,600))


        playLoop = True
        while playLoop:
                dt = clock.tick(30)


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        self.initMenu()
                thisImage = pygame.image.load(bundle_dir + 'images/MGlogo.jpg')
                fullHeart = pygame.image.load(bundle_dir + 'images/fullheart.png')
                emptyHeart = pygame.image.load(bundle_dir + 'images/emptyheart.png')

                self.tilemap.update(dt, self)
                screen.fill((0,0,0))

                self.tilemap.draw(self.screen)

                pygame.draw.rect(gameDisplay, COLOR_WHITE, (105, 25, 230, 60))

                pygame.draw.rect(gameDisplay, COLOR_LIMEGREEN, (120,30,self.player.magicPer * 2,50))
                
                if self.player.hearts >= 1:
                    gameDisplay.blit(fullHeart, (30, 30))
                else: 
                    gameDisplay.blit(emptyHeart, (30, 30))                    
                if self.player.hearts >= 2:
                    gameDisplay.blit(fullHeart, (30, 60))
                else: 
                    gameDisplay.blit(emptyHeart, (30, 60))
                if self.player.hearts >= 3:
                    gameDisplay.blit(fullHeart, (30, 90)) 
                else: 
                    gameDisplay.blit(emptyHeart, (30, 90))                    
                if self.player.hearts >= 4:
                    gameDisplay.blit(fullHeart, (30, 120))
                else: 
                    gameDisplay.blit(emptyHeart, (30, 120))                                                                               
                gameDisplay.blit(thisImage, (690, 500))

                
                #if self.mapFile == bundle_dir + 'WallsOrFireBalls.tmx':
                if self.player.transitionIn :

                    self.player.transTime += dt
                    if self.player.transTime < 1000:
                        #self.tilemap.draw(self.screen)
                        #if self.mapFile == 'WallsOrFireBalls.tmx': 

                        largeText = pygame.font.Font(bundle_dir + 'fonts/Exo2-MediumCondensed.ttf',65)
                        TextSurf, TextRect = text_objectsColor('Level ' + str(self.player.WOFlevel), largeText, COLOR_LIGHTCORAL)

                        TextRect.center = ((400),(100))
                        gameDisplay.blit(TextSurf, TextRect)

                    else:
                        self.player.transTime = 0
                        self.player.transitionIn = False

                if self.player.transitionOut:
                    
                    if self.player.hearts > 0:
                        self.player.transTime += dt
                        if self.player.transTime < 1000:
                            #self.tilemap.draw(self.screen)
                            #if self.mapFile == 'WallsOrFireBalls.tmx': 

                            largeText = pygame.font.Font(bundle_dir + 'fonts/Exo2-MediumCondensed.ttf',65,)
                            TextSurf, TextRect = text_objectsColor('Going to level ' + str(self.player.WOFlevel), largeText, COLOR_LIGHTCORAL)
    
                            TextRect.center = ((400),(100))
                            gameDisplay.blit(TextSurf, TextRect)
                                
                        else:
                            self.player.transTime = 0
                            self.player.transitionOut = False
                            self.initArea(bundle_dir + 'WallsOrFireBalls.tmx')
                    else:
                        self.player.transTime += dt
                        if self.player.transTime < 1000:
                            #self.tilemap.draw(self.screen)
                            #if self.mapFile == 'WallsOrFireBalls.tmx': 

                            largeText = pygame.font.Font(bundle_dir + 'fonts/Exo2-MediumCondensed.ttf',65)
                            TextSurf, TextRect = text_objectsColor('OH GOD YOUR DYING', largeText, red)
    
                            TextRect.center = ((400),(100))
                            gameDisplay.blit(TextSurf, TextRect)
                                
                        else:
                            self.player.transTime = 0
                            self.player.transitionOut = False
                            self.initArea(bundle_dir + 'babyHell.tmx')
                            self.samePlayer = False



                pygame.display.flip()        
        
        
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Pyllet Town")
    #os.system('python3 test3.py')
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.1)

    
    
    Game(screen).main()

