import pygame
import sys

pygame.init()

# Constants
ASPECT_RATIO = (21, 9)
WIDTH = 1366
HEIGHT = int(WIDTH / ASPECT_RATIO[0] * ASPECT_RATIO[1])
FPS = 60


# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player Deck Dimensions
DECK_WIDTH = WIDTH // 8
DECK_HEIGHT = HEIGHT

# Player Positions
PLAYER1_X = 0
PLAYER2_X = WIDTH - DECK_WIDTH

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Player Cannon Game")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the background (simple white screen)
    screen.fill(WHITE)

    # Draw player decks (red and blue rectangles)
    pygame.draw.rect(screen, RED, (PLAYER1_X, 0, DECK_WIDTH, DECK_HEIGHT))
    pygame.draw.rect(screen, BLUE, (PLAYER2_X, 0, DECK_WIDTH, DECK_HEIGHT))

    # Draw additional game elements here

    pygame.display.flip()
    clock.tick(FPS)