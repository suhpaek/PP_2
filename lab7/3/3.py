import pygame
import math
import time

pygame.init()


screen= pygame.display.set_mode((500,500))
clock=pygame.time.Clock()
done=False

x,y=250,250
radius=25
speed=20

while not done:
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (255,0,0),(x,y), radius)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

    keys= pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x-=speed
    if keys[pygame.K_RIGHT]:
        x+=speed
    if keys[pygame.K_UP]:
        y-=speed
    if keys[pygame.K_DOWN]:
        y+=speed

    if x-radius<0:
        x=radius
    if x+radius>500:
        x=500-radius
    if y-radius<0:
        y=radius
    if y+radius>500:
        y=500-radius
    

    clock.tick(60)
pygame.quit()

