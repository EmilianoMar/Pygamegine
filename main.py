# THIS SCRIPT IS FOR TESTING PURPOSES ONLY
import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))


class Sprite:
    def __init__(self, texture, position):
        self.position = position
        try:
            self.texture = pygame.image.load(texture)
        except:
            print("Texture not found")
    def draw(self, surf, pos):
        try:
            surf.blit(self.texture, pos)
        except:
            print("No texture found")
    def scale(self, scl):
        self.texture = pygame.transform.scale(self.texture, scl)


class CharacterBody:
    def __init__(self,pos):
        self.position = pos
        self.nodes = []
        self.sprite = Sprite("no_image.error", (0,0))
    def append(self,obj):
        if type(obj) == Sprite:
            self.sprite = obj
        else:
            self.nodes.append(obj)
        
  

playerSprite = Sprite("ASSETS/c.png", (10,10))

player = CharacterBody((0,0))
player.append(playerSprite)
player.sprite.scale((64,64))

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill((100,100,255))
    player.sprite.draw(screen,player.position+player.sprite.position)
    pygame.display.flip()
