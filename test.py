#coding=utf-8

import pygame

pygame.init()

ourScreen = pygame.display.set_mode((400,300))

pygame.display.set_caption('파이게임')

finish = False

colorBlue = True
isPressed = False

while not finish:
    for event in pygame.event.get():#발생한 이벤트 리스트
        if event.type == pygame.QUIT:
            finish = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            colorBlue = not colorBlue


        if colorBlue: color = (0,128,255)
        else: color = (255,255,255)

        #draw할 대상스크린,color,rect
        pygame.draw.rect(ourScreen,color,pygame.Rect(20,20,60,60))


        # pygame.display.update()
        pygame.display.flip()