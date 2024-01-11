import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE
from pygame.gfxdraw import filled_circle

pygame.init()

# Create a Pygame window
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Dynamic Drawing')

clock = pygame.time.Clock()

drawing = False
radius = 20
color = (255, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            drawing = not drawing  # Toggle drawing on Space key press

    if drawing:
        # Get mouse position
        x, y = pygame.mouse.get_pos()
        # Draw a filled circle at the mouse position
        filled_circle(screen, x, y, radius, color)

    pygame.display.flip()
    screen.fill((0, 0, 0))  # Clear the screen

    clock.tick(60)
