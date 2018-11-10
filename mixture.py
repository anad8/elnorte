import pygame, sys

HEIGHT = 900
WIDTH = 1450
screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)  # screensttingwindow
clock = pygame.time.Clock()

pygame.init()
bg = pygame.image.load("part4.png")

class Tittle(pygame.sprite.Sprite):
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load('name.png')
       self.image = pygame.transform.scale(self.image, (500, 500))
       self.rect = self.image.get_rect()
       self.rect.x = 480
       self.rect.y = 50

   def update(self):
       global bg

       key = pygame.key.get_pressed()

       if key[pygame.K_SPACE]:
           bg = pygame.image.load("part1.png")
           titulo.kill()

class Ready(pygame.sprite.Sprite):
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load('start.png')
       self.image = pygame.transform.scale(self.image, (400, 400))
       self.rect = self.image.get_rect()
       self.rect.x = 540
       self.rect.y = 420

   def update(self):
       global bg

       key = pygame.key.get_pressed()

       if key[pygame.K_SPACE]:
           listo.kill()
















all_sprites = pygame.sprite.Group()
listo = Ready()
titulo = Tittle()
all_sprites.add(listo)
all_sprites.add(titulo)

while 1:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
            sys.exit()

   all_sprites.update()

   screen.blit(bg,[0, 0])
   all_sprites.draw(screen)
   pygame.display.flip()

pygame.quit()








