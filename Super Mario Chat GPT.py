import pygame

# Initialize pygame
pygame.init()

# Set up the game window
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Super Mario")

# Load the player character sprite
player_image = pygame.image.load("mario.png")
player_position = (400, 500)

# Define platforms
platforms = [
    pygame.Rect(0, 550, 800, 50),
    pygame.Rect(150, 450, 500, 50),
    pygame.Rect(300, 300, 300, 50),
]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_position[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_position[0] += 5
    
    # Update game state
    player_rect = pygame.Rect(player_position[0], player_position[1], player_image.get_width(), player_image.get_height())
    
    # Check for collisions with platforms
    player_on_ground = False
    for platform in platforms:
        if player_rect.colliderect(platform):
            player_on_ground = True
            player_rect.bottom = platform.top
    
    # Update player position
    if not player_on_
