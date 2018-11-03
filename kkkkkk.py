import pygame, sys, random

HEIGHT = 920
WIDTH = 1530
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)  # screensttingwindow
clock = pygame.time.Clock()

pygame.init()
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
        self.rect.x = 10
        self.rect.y = 20
        for cacti in cactusGroup:
            cacti.kill()
        for i in range(4):
            i = Cactus1(random.randint(50,900), random.randint(80,800))
        cactusGroup.add(i)

class Casa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('casa.png')
        self.image = pygame.transform.scale(self.image, (400,400))
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 300

pygame.init()
House = Casa()

class Snake(pygame.sprite.Sprite):
  def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load('snakeL.png')
      self.image = pygame.transform.scale(self.image, (180,90))
      self.rect = self.image.get_rect()
      self.rect.x = 250
      self.rect.y = 300

pygame.init()
snake = Snake()

class BorderPatrol(pygame.sprite.Sprite):
    def __init(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Patrol.png')
        self.image = pygame.transform.scale(self.image, (420, 470))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y



class Cactus1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('cac1.png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y

all_sprites = pygame.sprite.Group()
cactusGroup = pygame.sprite.Group()
plant = Cactus1(200, 400)
plant2 = Cactus1(600, 400)
plant3 = Cactus1(800, 700)
plant4 = Cactus1(100, 800)
cactusGroup.add(plant)
cactusGroup.add(plant2)
cactusGroup.add(plant3)
cactusGroup.add(plant4)
player = Character()
all_sprites.add(player)
all_sprites.add(House)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
all_sprites.update()
cactusGroup.update()

hits = pygame.sprite.spritecollide(player, cactusGroup, False)
for hit in hits:
        if player.rect.top == hit.rect.bottom - 100:
            player.rect.y -= player.speedy
        if player.rect.left == hit.rect.right - 140:
            player.rect.x -= player.speedx
        if player.rect.bottom == hit.rect.top + 100:
            player.rect.y -= player.speedy
        if player.rect.right == hit.rect.left + 140:
            player.rect.x -= player.speedx

screen.blit(bg, [0, 0])
all_sprites.draw(screen)
cactusGroup.draw(screen)
pygame.display.flip()

pygame.quit()



