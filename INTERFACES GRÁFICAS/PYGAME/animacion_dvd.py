import pygame, sys
pygame.init()

BLACK   =   (0, 0, 0)
RED     =   (255, 0, 0)
GREEN   =   (0, 255, 0)
BLUE    =   (0, 0, 255)

colores = [RED, GREEN, BLUE]
color_index = 0

size = (800, 500)

# Crear ventana
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

cord_x = 400
cord_y = 250

speed_x = 1
speed_y = 1


# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if cord_x > 750 or cord_x < 50:
        speed_x *= -1
        color_index = (color_index + 1) % len(colores)
    if cord_y > 450 or cord_y < 50:
        speed_y *= -1
        color_index = (color_index + 1) % len(colores)

    cord_x += speed_x
    cord_y += speed_y

    screen.fill(BLACK)

    circulo = pygame.draw.circle(screen, colores[color_index], (cord_x, cord_y), 50)



    pygame.display.flip()
    clock.tick(60)