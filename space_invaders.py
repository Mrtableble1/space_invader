import pygame

HEIGHT = 800
WIDTH = 800

TITLE = "space invaders"

screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption(TITLE)

run = 1

bg = pygame.image.load("image/bg_invaders.png")
bg = pygame.transform.scale(bg,(800,800))

y_ss = pygame.image.load("image/yellow_spaceship.png")
y_ss = pygame.transform.scale(y_ss,(50,50))
y_ss = pygame.transform.rotate(y_ss,90)

r_ss = pygame.image.load("image/red_spaceship.png")
r_ss = pygame.transform.scale(r_ss,(50,50))
r_ss = pygame.transform.rotate(r_ss,-90)

class Spaceship(pygame.sprite.Sprite):
    def __init__(self,i,x,y):
        super().__init__()
        self.image = i
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

yellow_spaceship = Spaceship(y_ss,200,400)

red_spaceship = Spaceship(r_ss,600,400)

The_sprites = pygame.sprite.Group()
The_sprites.add(yellow_spaceship)
The_sprites.add(red_spaceship)


while run == 1:

    screen.blit(bg,(0,0))
    The_sprites.draw(screen)
    pygame.draw.line(screen,"black",(400,0),(400,800),5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
    
    keyspressed = pygame.key.get_pressed()


    if keyspressed[pygame.K_w]:
        yellow_spaceship.rect.x += 3

    if keyspressed[pygame.K_s]:
        yellow_spaceship.rect.x += -3

    if keyspressed[pygame.K_a]:
        yellow_spaceship.rect.y += 3

    if keyspressed[pygame.K_d]:
        yellow_spaceship.rect.y += -3


    if yellow_spaceship.rect.y < 0:
        yellow_spaceship.rect.y = 0

    if yellow_spaceship.rect.y > 750:
        yellow_spaceship.rect.y = 750

    if yellow_spaceship.rect.x < 0:
        yellow_spaceship.rect.x = 0

    if yellow_spaceship.rect.x > 750:
        yellow_spaceship.rect.x = 750








    pygame.display.update()