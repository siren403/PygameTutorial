#coding=utf-8

import pygame

pygame.init()

ourScreen = pygame.display.set_mode((400,300))

pygame.display.set_caption('파이게임')

finish = False

colorBlue = True

x = 30
y = 30
clock = pygame.time.Clock()


while not finish:
    for event in pygame.event.get():#발생한 이벤트 리스트
        if event.type == pygame.QUIT:
            finish = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            colorBlue = not colorBlue

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3


        ourScreen.fill((0,0,0))


        if colorBlue: color = (0,128,255)
        else: color = (255,255,255)

        #draw할 대상스크린,color,rect
        pygame.draw.rect(ourScreen,color,pygame.Rect(x,y,60,60))


        # pygame.display.update()
        pygame.display.flip()
        clock.tick(60)