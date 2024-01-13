import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Green Circle")

# Set up colors
green = (0, 255, 0)

# Set up the circle position and speed
circle_radius = 50
circle_x, circle_y = width // 2, height // 2
speed = 1.0
velocity = [0, 0]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Key pressed
            if event.key == pygame.K_RIGHT:
                velocity[0] = speed
            elif event.key == pygame.K_LEFT:
                velocity[0] = -speed
            elif event.key == pygame.K_DOWN:
                velocity[1] = speed
            elif event.key == pygame.K_UP:
                velocity[1] = -speed
        elif event.type == pygame.KEYUP:  # Key released
            if (event.key == pygame.K_RIGHT and velocity[0] > 0) or \
               (event.key == pygame.K_LEFT and velocity[0] < 0):
                velocity[0] = 0
            elif (event.key == pygame.K_DOWN and velocity[1] > 0) or \
                 (event.key == pygame.K_UP and velocity[1] < 0):
                velocity[1] = 0

    # Update the circle position
    circle_x += velocity[0]
    circle_y += velocity[1]

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the moving green circle
    pygame.draw.circle(screen, green, (int(circle_x), int(circle_y)), circle_radius)

    # Update the display
    pygame.display.flip()

    # Add a small delay to control the speed of the ball
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()
sys.exit()
