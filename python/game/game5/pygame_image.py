import pygame


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("pygame!")

img = pygame.image.load(r"C:\Users\helio\Downloads\smile.png")
img = pygame.transform.scale(img,(100,100))

x=330
y=240

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
            elif event.key == pygame.K_LEFT:
                x-=10
            elif event.key == pygame.K_RIGHT:
                x+=10
            elif event.key == pygame.K_UP:
                y-=10
            elif event.key == pygame.K_DOWN:
                y+=10 
    
    screen.blit(img,(x,y))
    pygame.display.update()



