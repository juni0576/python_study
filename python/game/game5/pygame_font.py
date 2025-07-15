import pygame

# ------초기화------
pygame.init()
screen = pygame.display.set_mode((800,600))
#창 해상도
pygame.display.set_caption("pygame!")
#창 타이틀

# ---폰트 ---
FONT = pygame.font.SysFont("malgun gothic",48)
text = FONT.render("Intel",True,(255,255,255))
#흰색 글씨

x=330
y=0
# ---- key event -----

while True:
    screen.fill((0,0,0))
#색상. RED GREEN BULE
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
    y+=1
    if y>600:
        y=0
    screen.blit(text,(x,y))
    pygame.display.update()

