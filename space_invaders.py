import pygame
pygame.init()

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
health_bar_ys = 20
y_bullets = []

red_spaceship = Spaceship(r_ss,600,400)
health_bar_rs = 20
r_bullets = []

The_sprites = pygame.sprite.Group()
The_sprites.add(yellow_spaceship)
The_sprites.add(red_spaceship)


def handel_bullets():
    global health_bar_ys,y_bullets,health_bar_rs,r_bullet

    for y_bullet in y_bullets:
        pygame.draw.rect(screen,"yellow",y_bullet,0)
        y_bullet.x += 5
        if y_bullet.colliderect(red_spaceship):
            y_bullets.remove(y_bullet)
            health_bar_rs -= 1
        

    for r_bullet in r_bullets:
        pygame.draw.rect(screen,"red",r_bullet,0)
        r_bullet.x -= 5
        if r_bullet.colliderect(yellow_spaceship):
            r_bullets.remove(r_bullet)
            health_bar_ys -= 1

while run == 1:

    screen.blit(bg,(0,0))
    The_sprites.draw(screen)
    pygame.draw.line(screen,"black",(400,0),(400,800),5)

    hbys = pygame.draw.rect(screen,"yellow",(20,20,10*health_bar_ys,20),0)
    hbrs = pygame.Rect(580,20,10*health_bar_rs,20)
    hbrs.right = 780
    pygame.draw.rect(screen,"red",hbrs,0)

    handel_bullets()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y_bullet = pygame.Rect(yellow_spaceship.rect.x,yellow_spaceship.rect.y,10,5)
                y_bullets.append(y_bullet)
                y_bullet = pygame.Rect(yellow_spaceship.rect.x,yellow_spaceship.rect.y+50,10,5)
                y_bullets.append(y_bullet)

            if event.key == pygame.K_RSHIFT:
                r_bullet = pygame.Rect(red_spaceship.rect.x,red_spaceship.rect.y,10,5)
                r_bullets.append(r_bullet)
                r_bullet = pygame.Rect(red_spaceship.rect.x,red_spaceship.rect.y+50,10,5)
                r_bullets.append(r_bullet)


        if event.type == pygame.QUIT:
            run = 0
    
    if health_bar_rs == 0 :
        font = pygame.font.SysFont("Arial",50)
        msg1 = font.render("yellow won the match!",True,"yellow")
        screen.blit(msg1,(240,260))
        pygame.display.update()
        pygame.time.delay(5000)
        run = 0

    if health_bar_ys == 0:
        font = pygame.font.SysFont("Arial",50)
        msg1 = font.render("red won the match!",True,"red")
        screen.blit(msg1,(240,260))
        pygame.display.update()
        pygame.time.delay(5000)
        run = 0
        
        



    keyspressed = pygame.key.get_pressed()




    if keyspressed[pygame.K_d]:
        yellow_spaceship.rect.x += 3

    if keyspressed[pygame.K_a]:
        yellow_spaceship.rect.x += -3

    if keyspressed[pygame.K_w]:
        yellow_spaceship.rect.y += 3

    if keyspressed[pygame.K_s]:
        yellow_spaceship.rect.y += -3


    if yellow_spaceship.rect.y < 0:
        yellow_spaceship.rect.y = 0

    if yellow_spaceship.rect.y > 750:
        yellow_spaceship.rect.y = 750

    if yellow_spaceship.rect.x < 0:
        yellow_spaceship.rect.x = 0

    if yellow_spaceship.rect.x > 350:
        yellow_spaceship.rect.x = 350





    if keyspressed[pygame.K_RIGHT]:
        red_spaceship.rect.x += 3

    if keyspressed[pygame.K_LEFT]:
        red_spaceship.rect.x += -3

    if keyspressed[pygame.K_DOWN]:
        red_spaceship.rect.y += 3

    if keyspressed[pygame.K_UP]:
        red_spaceship.rect.y += -3


    if red_spaceship.rect.y < 0:
        red_spaceship.rect.y = 0

    if red_spaceship.rect.y > 750:
        red_spaceship.rect.y = 750

    if red_spaceship.rect.x < 400:
        red_spaceship.rect.x = 400

    if red_spaceship.rect.x > 750:
        red_spaceship.rect.x = 750








    pygame.display.update()