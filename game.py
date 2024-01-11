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
LIGHT_RED = (255, 64, 64)
DARK_RED = (128, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 128, 255)
DARK_BLUE = (0, 0, 128)
GREEN = (0, 255, 0)
LIGHT_GREEN = (128, 255, 128)
DARK_GREEN = (0, 128, 0)
BLACK = (0, 0, 0)


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
        pygame.draw.line(screen, color, (x1, y1), (x2, y2), 7)  # 7 is the line thickness

def draw_circle(x, y, radius, color):
    pygame.draw.circle(screen, color, (x, y), radius)

def draw_tank(x, y, base_radius, turret_length, turret_width, color, light_color , dark_color, rotation):
    # Calculate turret position
    turret_x = int(x +(base_radius + turret_length / 2) * math.cos(math.radians(rotation)))
    turret_y = int(y  +(base_radius + turret_length / 2) * math.sin(math.radians(rotation)))

    # Draw circular tank base
    draw_circle(x, y, base_radius+5, BLACK) 
    draw_circle(x, y, base_radius, dark_color) 

    # Draw tank turret
    rotated_turret = pygame.Surface((turret_length+5  , turret_width +10), pygame.SRCALPHA)
    pygame.draw.rect(rotated_turret, BLACK, (0, 0, turret_length+5 , turret_width +10))
    rotated_turret = pygame.transform.rotate(rotated_turret, -rotation)
    rect = rotated_turret.get_rect(center=(turret_x, turret_y))
    screen.blit(rotated_turret, rect.topleft)

    rotated_turret = pygame.Surface((turret_length+5, turret_width), pygame.SRCALPHA)
    pygame.draw.rect(rotated_turret, dark_color, (0, 0, turret_length+5, turret_width))
    rotated_turret = pygame.transform.rotate(rotated_turret, -rotation)
    rect = rotated_turret.get_rect(center=(turret_x, turret_y))
    screen.blit(rotated_turret, rect.topleft)


class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, BLACK, (self.x, self.y), self.radius + 7)
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius + 5)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        pygame.draw.circle(screen, DARK_GREEN, (self.x, self.y), self.radius, 2)

# Create a ball at the center of the screen
ball = Ball(WIDTH //2, HEIGHT // 2, 40, GREEN)



def main():
    rotation_speed_left = 360 / (5 * FPS)  # One rotation every 5 seconds
    rotation_speed_right = -360 / (5 * FPS)  # Opposite direction

    rotation_left = -90
    rotation_right = -90

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the screen with white
        screen.fill(LIGHT_GREEN)

        # Draw red and blue rectangles on each side
        pygame.draw.rect(screen, RED, (0, 0, WIDTH // 8, HEIGHT))
        pygame.draw.rect(screen, BLUE, (WIDTH - WIDTH // 8, 0, WIDTH // 8, HEIGHT))

        # Draw light-colored playing area near the deck of each player
        pygame.draw.rect(screen, LIGHT_RED, (0, HEIGHT // 4, WIDTH // 8, HEIGHT // 2))  # Left side
        pygame.draw.rect(screen, LIGHT_BLUE, (WIDTH - WIDTH // 8, HEIGHT // 4, WIDTH // 8, HEIGHT // 2))  # Right side

        # Draw a thin center black line
        pygame.draw.line(screen, BLACK, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)

        # Draw a line of players at the midpoint of each part of the court
        for i in range(1, 4):
            pygame.draw.circle(screen, RED, (WIDTH // 16, i * HEIGHT // 4), 20)  # Left side
            pygame.draw.circle(screen, BLUE, (WIDTH - WIDTH // 16, i * HEIGHT // 4), 20)  # Right side

        # Draw a line of players at the midpoint of each part of the court
        pygame.draw.line(screen, RED, (WIDTH // 4, 0), (WIDTH // 4, HEIGHT), 2)  # Left side
        pygame.draw.line(screen, BLUE, (3 * WIDTH // 4, 0), (3 * WIDTH // 4, HEIGHT), 2)  # Right side

        # Draw light colored players area near deck
        pygame.draw.rect(screen, LIGHT_RED, (WIDTH // 4 - WIDTH//8 -1 , 0 , WIDTH//8 +1, HEIGHT))  # Left side
        pygame.draw.rect(screen, LIGHT_BLUE, (3 * WIDTH // 4 +1 , 0, WIDTH // 8 +1, HEIGHT)) # Right side
        # Draw a bordered black circle at the center of the screen
        pygame.draw.circle(screen, DARK_GREEN, (WIDTH // 2, HEIGHT // 2), 100, 2)

        # Draw green gear at the center of each rectangle
        draw_gear(WIDTH // 16, HEIGHT // 2, 30, 8, GREEN, rotation_left)  # Left side
        draw_gear(WIDTH - WIDTH // 16, HEIGHT // 2, 30, 8, GREEN, rotation_right)  # Right side

        # Draw a green circle at the center of each rectangle
        draw_circle(WIDTH // 16, HEIGHT // 2, 35, GREEN)  # Left side
        draw_circle(WIDTH - WIDTH // 16, HEIGHT // 2, 35, GREEN)  # Right side

        # Draw tank-like structure on each side
        draw_tank(WIDTH // 16, HEIGHT // 2, 25, 40, 20, RED, LIGHT_RED, DARK_RED, rotation_left)  # Left side
        draw_tank(WIDTH - WIDTH // 16, HEIGHT // 2, 25, 40, 20, BLUE, LIGHT_BLUE, DARK_BLUE, rotation_right)  # Right side
        ball.draw()

        # Update rotation for the next frame
        rotation_left += rotation_speed_left
        rotation_right += rotation_speed_right

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

