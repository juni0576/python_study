import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("pygame!")

clock = pygame.time.Clock()
#Timer

FONT = pygame.font.SysFont("malgun gothic",48)
text = FONT.render("Intel",True,(255,255,255))

x=330
y=0

while True:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
    y+=1
    if y>600:
        y=0
    screen.blit(text,(x,y))
    pygame.display.update()

    clock.tick(30)

