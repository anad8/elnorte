import pygame, sys

pygame.init()

screen = pygame.display.set_mode((1200,700 ))#screensttingwindow

clock = pygame.time.Clock()



image = pygame.image.load('male_sprite_model.png')




class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('male_sprite_model.png')
        self.rect = self.image.get_rect()
        screen.blit(Player, (30, 50))
        self.image = pygame.transform.scale(self.image, (200, 120))
        self.speed = 5

    def movement(self):

        key = pygame.key.get_pressed()

        if key[pygame.K_UP]:
            self.rect.y -= self.speed








whileTrue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()





    screen.fill((0,0,0))
    screen.blit(image,(0,0))
    pygame.display.update()

