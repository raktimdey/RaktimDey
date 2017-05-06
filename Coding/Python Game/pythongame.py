import pygame
import time
import random

pygame.init() #this allow us to make various commands with Pygame

display_width=800
display_height=600

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

car_width=128 #program knows car's width

#gameDisplay is the main display of my game.
gameDisplay =pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A Car Game')
clock=pygame.time.Clock() #it's FPS

#carImg loaded the image i created.
carImg=pygame.image.load('racecar.png')

#for drawing a object we defined x,y,width,height,color var
#draw.rect() to draw to the polygon.

def things(thingx, thingy,thingw,thingh,color):
  pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])


#Define car function. "Blit" just draw the image on the screen

def car(x,y):
  gameDisplay.blit(carImg,(x,y))


def text_objects(text,font):
  textSurface=font.render(text,True,black)
  return textSurface,textSurface.get_rect() #get.rect() is invisible.


#we made a specific function,so that later we can change crash display

def message_display(text):
  largeText=pygame.font.Font('freesansbold.ttf',85) #Font
  TextSurf,TextRect= text_objects(text,largeText)  #rectangle where font will be displayed
  TextRect.center= ((display_width/2),(display_height/2))
  gameDisplay.blit(TextSurf,TextRect)

  pygame.display.update()
  time.sleep(2)
  game_loop()

#crash function shows the message
def crash():
  message_display('YOU CRASHED')

##GAME LOOOP FUNCTION###################
def game_loop():
  x=(display_width * 0.45) #from car(x,y). we change resoloution of car
  y=(display_height * 0.8)
  x_change=0

# x is left to right.so random can between left to right display_width
  thing_startx=random.randrange(0,display_width)
  thing_starty=-600 #speed of block
  #speed means speed of object.per frame,will move 7pixels
  thing_speed=7
  thing_width=100
  thing_height=100

  gameExit=False

#if game doesn't exit
  while not gameExit:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
        quit()

      if event.type==pygame.KEYDOWN:
         if event.key==pygame.K_LEFT: #left arrow
            x_change=-5                #it will go -5 on the left
         elif event.key==pygame.K_RIGHT: #right arrow
            x_change=5

      if event.type==pygame.KEYUP: #KEYUP means key is released
        if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
          x_change=0



    x+=x_change #remember x? it's our car img function
    gameDisplay.fill(white) #background will be white

#value will change accordingly
    things(thing_startx,thing_starty,thing_width,thing_height,black)
    thing_starty+=thing_speed
    car(x,y)

#our logic is here whether or not the car crossed over the Left/right Boundaries
    if x>display_width-car_width or x<0:
      crash()

#so the block can move all the screen around
    if thing_starty>display_height:
       thing_starty=0-thing_height
       thing_startx=random.randrange(0,display_width)



    pygame.display.update()
    clock.tick(120)


game_loop()
pygame.quit()
quit()
