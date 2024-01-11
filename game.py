import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 1366
HEIGHT = 768
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Player Cannon Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

def draw_gear(x, y, radius, num_teeth, color, rotation):
    for i in range(num_teeth):
        angle = math.radians((i * (360 / num_teeth)) + rotation)
        x1 = int(x + radius * math.cos(angle))
        y1 = int(y + radius * math.sin(angle))
        x2 = int(x + (radius + 10) * math.cos(angle))
        y2 = int(y + (radius + 10) * math.sin(angle))
        pygame.draw.line(screen, color, (x1, y1), (x2, y2), 5)  # 5 is the line thickness

def draw_circle(x, y, radius, color):
    pygame.draw.circle(screen, color, (x, y), radius)

def main():
    rotation_speed_left = 360 / (5 * FPS)  # One rotation every 5 seconds
    rotation_speed_right = -360 / (5 * FPS)  # Opposite direction

    rotation_left = 0
    rotation_right = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the screen with white
        screen.fill(WHITE)

        # Draw red and blue rectangles on each side
        pygame.draw.rect(screen, RED, (0, 0, WIDTH // 8, HEIGHT))
        pygame.draw.rect(screen, BLUE, (WIDTH - WIDTH // 8, 0, WIDTH // 8, HEIGHT))

        # Draw green gear at the center of each rectangle
        draw_gear(WIDTH // 16, HEIGHT // 2, 30, 8, GREEN, rotation_left)  # Left side
        draw_gear(WIDTH - WIDTH // 16, HEIGHT // 2, 30, 8, GREEN, rotation_right)  # Right side

        # Draw a green circle at the center of each rectangle
        draw_circle(WIDTH // 16, HEIGHT // 2, 30, GREEN)  # Left side
        draw_circle(WIDTH - WIDTH // 16, HEIGHT // 2, 30, GREEN)  # Right side

        # Update rotation for the next frame
        rotation_left += rotation_speed_left
        rotation_right += rotation_speed_right

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
