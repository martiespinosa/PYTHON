import pygame, sys
pygame.init()

size = (800, 500)

# Crear ventana
screen = pygame.display.set_mode(size)

# Bucle principal
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

