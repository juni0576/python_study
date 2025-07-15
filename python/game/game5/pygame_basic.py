import pygame

# ------초기화------
pygame.init()
screen = pygame.display.set_mode((800,600))
#창 해상도
pygame.display.set_caption("pygame!")
#창 타이틀


# ---- key event -----

while True:
    screen.fill((0,0,0))
#색상. RED GREEN BULE
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()



