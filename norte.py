import pygame, sys

HEIGHT = 900
WIDTH = 1450
screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)  # screensttingwindow
clock = pygame.time.Clock()

bg = pygame.image.load("part1.png")

class Character(pygame.sprite.Sprite):
  def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load('maleR.png')
      self.image = pygame.transform.scale(self.image,(160,160))
      self.rect = self.image.get_rect()
      self.speedy = 0
      self.speedx = 0
  def update(self):
      global bg
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
          self.image = pygame.image.load('maleR.png')
          self.image = pygame.transform.scale(self.image, (160, 160))
      if key[pygame.K_LEFT]:
          self.speedx = -20
          self.image = pygame.image.load('maleL.png')
          self.image = pygame.transform.scale(self.image, (160, 160))
      self.rect.x += self.speedx

      if self.rect.left < 0:
          self.rect.left = 0
      if self.rect.right > WIDTH:
          self.rect.right = WIDTH
          bg = pygame.image.load("part2.png")

pygame.init()
player = Character()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

class Cactus1(pygame.sprite.Sprite):
  def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load('cac1.png')
      self.image = pygame.transform.scale(self.image, (180,180))
      self.rect = self.image.get_rect()
      self.rect.x = 700
      self.rect.y = 400

pygame.init()
plant = Cactus1()
all_sprites.add(plant)

class Cactus2(pygame.sprite.Sprite):
  def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load('cac2.png')
      self.image = pygame.transform.scale(self.image, (180,180))
      self.rect = self.image.get_rect()
      self.rect.x = 500
      self.rect.y = 60

pygame.init()
plant = Cactus2()
all_sprites.add(plant)

while 1:
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         sys.exit()

 all_sprites.update()

 screen.blit (bg,[0,0])
 all_sprites.draw(screen)
 pygame.display.flip()


pygame.quit()


