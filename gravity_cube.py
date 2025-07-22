import pygame

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Cube with Gravity")

# Cube properties
cube_size = 50
x = (WIDTH - cube_size) // 2
# Start at the top
y = 0
velocity_y = 0

gravity = 0.5
bounce_factor = -0.7

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Apply gravity
    velocity_y += gravity
    y += velocity_y

    # Check for collision with the ground
    if y + cube_size > HEIGHT:
        y = HEIGHT - cube_size
        velocity_y *= bounce_factor

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw cube
    pygame.draw.rect(screen, (0, 120, 250), (x, int(y), cube_size, cube_size))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
