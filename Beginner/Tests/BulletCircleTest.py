import pygame
import math

pygame.init()

ourScreen = pygame.display.set_mode((500,500), pygame.DOUBLEBUF)

pygame.display.set_caption('원형탄 테스트')

TARGET_FPS = 30

clock = pygame.time.Clock()
finish = False
center = (250,250)
radius = 200
count = 1
pivot = (math.pi * 2) * 0.75

score = 82349
num = score
numbers = []


while num > 0:
    numbers.insert(0,num % 10)
    print(numbers[0])
    num = int(num / 10)

print(numbers)


while not finish:



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finish = True

        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     count = count + 1


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_z]:pivot += 0.05
    if pressed[pygame.K_SPACE]:count += 1


    ourScreen.fill((0,0,0))

    x = 0
    y = 0
    pygame.draw.circle(ourScreen, (255, 255, 255, 0.5), center, 5)

    for i in range(count):
        x = int(center[0] + math.cos(((math.pi * 2) * (i / count)) + pivot) * radius)
        y = int(center[1] + -math.sin(((math.pi * 2) * (i / count)) + pivot) * radius)
        pygame.draw.circle(ourScreen, (255, 255, 255, 127), (x, y), 5)

    pygame.display.flip()

    clock.tick(TARGET_FPS)


pygame.quit()
quit()