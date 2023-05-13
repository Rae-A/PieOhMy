import pygame, sys, random 

# this class represents the fruits 
class Fruit(pygame.sprite.Sprite):
     
     # initiating basic attributes of the sprite, 1st param always self
     def __init__(self, picDoc):
          super().__init__()
          # creates rectangle
          self.image = pygame.image.load(picDoc)
          self.rect = self.image.get_rect()
     # sets mouse as an image
     def update(self):
          self.rect.center = pygame.mouse.get_pos()


class Fruits(pygame.sprite.Sprite):
     def __init__(self, picDocu, posX, posY):
          super().__init__()
          self.image = pygame.image.load(picDocu)
          self.rect = self.image.get_rect()
          self.rect.center = [posX, posY]

pygame.init() # initiate pygame


#window display
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.image.load('PieOhMyBackground.jpg') 

pygame.mouse.set_visible(False) # makes mouse invisible to put image in its place 

# image to put on mouse
fruit = Fruit("CherrySprite.png")
fruitGroup = pygame.sprite.Group()
fruitGroup.add(fruit)

# fruits


# fruits 

carrotGroup = pygame.sprite.Group()
for carrot in range(4):
     newCarrot = Fruits("CarrotSprite.png", random.randrage(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT))
     carrotGroup.add(newCarrot)

#peach = Fruit("PeachSprite.png")
#peachGroup = pygame.sprite.Group()
#peachGroup.add(peach)

#cherry = Fruit("CherrySprite.png")
#cherryGroup = pygame.sprite.Group()
#peachGroup.add(cherry)

#game loop 
while True:

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    pygame.display.flip() # updates contents of screen
    screen.blit(bg, (0,0)) # copying on surface to another
    carrotGroup.draw(screen)

    fruitGroup.draw(screen) 
    #carrotGroup.draw(screen)
    #peachGroup.draw(screen)
    #cherryGroup.draw(screen)
    fruitGroup.update()

    
    
pygame.quit()