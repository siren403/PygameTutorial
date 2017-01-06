import pygame

pygame.init()

#music
# pygame.mixer.music.load('.mp3')
# pygame.mixer.music.play(0)


WIDTH = 800
HEIGHT = 600

# ourScreen = pygame.display.set_mode((WIDTH,HEIGHT))
ourScreen = pygame.display.set_mode((WIDTH,HEIGHT))

myImg = pygame.image.load('images.jpg')

def myimg(x,y):
    ourScreen.blit(myImg,(x,y))

x = (WIDTH * 0.5)
y = (HEIGHT * 0.5)

finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    ourScreen.fill((255,255,200))
    myimg(x,y)
    pygame.display.flip()


pygame.quit()
quit()