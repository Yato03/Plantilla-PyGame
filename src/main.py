import sys, pygame
pygame.init()

size = (500,500)
fps = 60

#COLORES
BLACK = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #LÓGICA

    #DIBUJO
    screen.fill(BLACK)

    pygame.display.flip()
    clock.tick(fps)