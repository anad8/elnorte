import pygame, sys

HEIGHT = 900
WIDTH = 1450
screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)  # screensttingwindow
image = "first.png"
clock = pygame.time.Clock()
background_image= pygame.image.load("First.png")

class Character(pygame.sprite.Sprite):
  def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load('spritem.png')
      self.image = pygame.transform.scale(self.image,(160,160))
      self.rect = self.image.get_rect()
      self.speedy = 0
      self.speedx = 0
  def update(self):
      self.speedy = 0
      self.speedx = 0

      key = pygame.key.get_pressed()

      if key[pygame.K_UP]:
          self.speedy = -20
      if key[pygame.K_DOWN]:
          self.speedy = 20
      self.rect.y += self.speedy

      if self.rect.bottom > HEIGHT:
          self.rect.bottom = HEIGHT
      if self.rect.top < 0:
          self.rect.top = 0

      if key[pygame.K_RIGHT]:
          self.speedx = 20
      if key[pygame.K_LEFT]:
          self.speedx = -20
      self.rect.x += self.speedx

      if self.rect.left < 0:
          self.rect.left = 0
      if self.rect.right > WIDTH:
          self.rect.right = WIDTH

pygame.init()
player = Character()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)



class Cactus1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('cac1.png')
        self.image = pygame.transform.scale(self.image, (160,160))
        self.rect = self.image.get_rect()

pygame.init()
Cactus1 = Cactus1()
sprites = pygame.sprite.Group()
sprites.add(Cactus1)


while 1:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit()

  all_sprites.update()


  screen.blit (background_image,[0,0])
  all_sprites.draw(screen)
  pygame.display.flip()


  pygame.quit()