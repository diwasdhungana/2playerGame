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
GRAY = (128, 128, 128)


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




class Ball:
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.moving = False

    def draw(self):
        pygame.draw.circle(screen, BLACK, (self.x, self.y), self.radius + self.radius // 3)
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius + self.radius // 5)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        pygame.draw.circle(screen, DARK_GREEN, (self.x, self.y), self.radius, 2)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def destroy(self):
        self.radius = 0
        if self.color == RED:
            self.x = WIDTH // 16
        if self.color == BLUE:
            self.x = WIDTH - WIDTH // 16
        if self.color == GREEN:
            self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.direction = 0
        self.moving = False


# Create a ball at the center of the screen
mainBall = Ball(WIDTH //2, HEIGHT // 2, 40, GREEN , 0)

redBall = Ball(WIDTH//16, HEIGHT //2 , 0 , RED , 0)
redBallIndicator = Ball(WIDTH//64, HEIGHT //2 , 10 , GREEN , 0)
blueBall = Ball(WIDTH - WIDTH//16, HEIGHT //2 , 0 , BLUE  , 0)
blueBallIndicator = Ball(WIDTH - WIDTH//64, HEIGHT //2 , 10 , GREEN , 0)



class Tank:
    def __init__(self, x, y, base_radius, turret_length, turret_width, color, light_color, dark_color, rotation):
        self.x = x
        self.y = y
        self.base_radius = base_radius
        self.turret_length = turret_length
        self.turret_width = turret_width
        self.color = color
        self.light_color = light_color
        self.dark_color = dark_color
        self.rotation = rotation
        self.deck_center_x = x
        self.deck_center_y = y

    def draw(self):
        # Calculate turret position
        turret_x = int(self.x + (self.base_radius + self.turret_length / 2) * math.cos(math.radians(self.rotation)))
        turret_y = int(self.y + (self.base_radius + self.turret_length / 2) * math.sin(math.radians(self.rotation)))

        # Draw circular tank base
        draw_circle(self.x, self.y, self.base_radius + 5, BLACK)
        draw_circle(self.x, self.y, self.base_radius, self.dark_color)

        # Draw tank turret
        rotated_turret = pygame.Surface((self.turret_length + 5, self.turret_width + 10), pygame.SRCALPHA)
        pygame.draw.rect(rotated_turret, BLACK, (0, 0, self.turret_length + 5, self.turret_width + 10))
        rotated_turret = pygame.transform.rotate(rotated_turret, -self.rotation)
        rect = rotated_turret.get_rect(center=(turret_x, turret_y))
        screen.blit(rotated_turret, rect.topleft)

        rotated_turret = pygame.Surface((self.turret_length + 5, self.turret_width), pygame.SRCALPHA)
        pygame.draw.rect(rotated_turret, self.dark_color, (0, 0, self.turret_length + 5, self.turret_width))
        rotated_turret = pygame.transform.rotate(rotated_turret, -self.rotation)
        rect = rotated_turret.get_rect(center=(turret_x, turret_y))
        screen.blit(rotated_turret, rect.topleft)



def main():
    rotation_speed_left = 360 / (4 * FPS)  # One rotation every 4 seconds
    rotation_speed_right = -360 / (4 * FPS)  # Opposite direction
    rotation_right_halt = [False , 0]
    rotation_left_halt = [False, 0] 
    red_button_hold = [False, 0]
    blue_button_hold = [False, 0]

    rotation_left = -90
    rotation_right = -90
    ball_speed = 6  # Adjust the speed as needed
    mainBall_speed = 0
    mainBall_speed_left = 0
    mainBall_speed_right = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    # Left Shift key is pressed, create a ball at the left player's deck center
                    if red_button_hold[0] == False:
                        redBall.moving = True
                        rotation_left_halt[0] = True
                        redBall.direction = rotation_left
                        red_button_hold[0] = True
                        redBallIndicator.color = GRAY
                if event.key == pygame.K_1:
                    redBall.destroy()

                if event.key == pygame.K_RSHIFT:
                    # Right Shift key is pressed, create a ball at the right player's deck center
                    if blue_button_hold[0] == False:
                        blueBall.moving = True
                        rotation_right_halt[0] = True
                        blueBall.direction = rotation_right
                        blue_button_hold[0] = True
                        blueBallIndicator.color = GRAY
                if event.key == pygame.K_2:
                    blueBall.destroy()

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


        redBallIndicator.draw()
        blueBallIndicator.draw()
        left_player_tank = Tank(WIDTH // 16, HEIGHT // 2, 25, 40, 20, RED, LIGHT_RED, DARK_RED, rotation_left)
        right_player_tank = Tank(WIDTH - WIDTH // 16, HEIGHT // 2, 25, 40, 20, BLUE, LIGHT_BLUE, DARK_BLUE, rotation_right)
        left_player_tank.draw()
        right_player_tank.draw()
        mainBall.draw()

        # Move the red ball if the flag is set
        if redBall.moving:
            redBall.move(ball_speed * math.cos(math.radians(redBall.direction)),
                         ball_speed * math.sin(math.radians(redBall.direction)))
            redBall.draw()

        # Move the blue ball if the flag is set
        if blueBall.moving:
            blueBall.move(ball_speed * math.cos(math.radians(blueBall.direction)),
                          ball_speed * math.sin(math.radians(blueBall.direction)))
            blueBall.draw()


        # check for the collision of red ball and main ball
        if math.sqrt((redBall.x - mainBall.x) ** 2 + (redBall.y - mainBall.y) ** 2) <= redBall.radius + mainBall.radius:
            mainBall.moving = True;
            # calculate the direction of main ball after collision
            mainBall.direction =  math.degrees(math.atan2(redBall.y - mainBall.y, redBall.x - mainBall.x)) + 180
            # check to see which is greater speed right or left and assign it to main ball speed minus the other
            if mainBall_speed_left > mainBall_speed_right:
                mainBall_speed = mainBall_speed_left - mainBall_speed_right
            elif mainBall_speed_left < mainBall_speed_right:
                mainBall_speed = mainBall_speed_right - mainBall_speed_left
            else:
                mainBall_speed = 0

            # calculate main ball speed after collision
            mainBall_speed =  mainBall_speed + math.sqrt((redBall.x - mainBall.x) ** 2 + (redBall.y - mainBall.y) ** 2) / 100
            redBall.destroy()


        # check for the collision of blue ball and main ball
        if math.sqrt((blueBall.x - mainBall.x) ** 2 + (blueBall.y - mainBall.y) ** 2) <= blueBall.radius + mainBall.radius:
            mainBall.moving = True;
            # calculate the direction of main ball after collision
            mainBall.direction =  math.degrees(math.atan2(blueBall.y - mainBall.y, blueBall.x - mainBall.x)) + 180
            # check to see which is greater speed right or left and assign it to main ball speed minus the other
            if mainBall_speed_left > mainBall_speed_right:
                mainBall_speed = mainBall_speed_left - mainBall_speed_right
            elif mainBall_speed_left < mainBall_speed_right:
                mainBall_speed = mainBall_speed_right - mainBall_speed_left
            else:
                mainBall_speed = 0
            # calculate main ball speed after collision
            mainBall_speed =  mainBall_speed + math.sqrt((blueBall.x - mainBall.x) ** 2 + (blueBall.y - mainBall.y) ** 2) / 100
            blueBall.destroy()


        if mainBall.moving:
            mainBall.move( mainBall_speed * math.cos(math.radians(mainBall.direction)),
                            mainBall_speed * math.sin(math.radians(mainBall.direction)))
            if mainBall_speed > 0:
                mainBall_speed = mainBall_speed - 0.0007
            else:
                mainBall_speed = 0
                mainBall.moving = False
            
        
        # destroy and reset the main ball if it goes out of the screen
        if mainBall.x < 0 or mainBall.x > WIDTH or mainBall.y < 0 or mainBall.y > HEIGHT:
            mainBall.destroy()
            mainBall_speed = 0
            mainBall.moving = False
            mainBall.x = WIDTH // 2
            mainBall.y = HEIGHT // 2
            mainBall.direction = 0

        # destroy the ball if it goes out of the screen
        if redBall.x < 0 or redBall.x > WIDTH or redBall.y < 0 or redBall.y > HEIGHT:
            redBall.destroy()
        if blueBall.x < 0 or blueBall.x > WIDTH or blueBall.y < 0 or blueBall.y > HEIGHT:
            blueBall.destroy()
        
        # checking for red button hold
        if red_button_hold[0] == True:
            red_button_hold[1] += 1
            if red_button_hold[1] == 150:
                red_button_hold[0] = False
                red_button_hold[1] = 0
                redBallIndicator.color = GREEN
        # checking for blue button hold
        if blue_button_hold[0] == True:
            blue_button_hold[1] += 1
            if blue_button_hold[1] == 150:
                blue_button_hold[0] = False
                blue_button_hold[1] = 0
                blueBallIndicator.color = GREEN


        if rotation_left_halt[0] == True:
            rotation_left_halt[1] += 1
            rotation_left -= rotation_speed_left
            redBall.radius = redBall.radius + 0.5
            if rotation_left_halt[1] == 29:
                rotation_left_halt[0] = False
                rotation_left_halt[1] = 0
        if rotation_right_halt[0] == True:
            rotation_right_halt[1] += 1
            blueBall.radius = blueBall.radius + 0.5
            rotation_right -= rotation_speed_right
            if rotation_right_halt[1] == 29:
                rotation_right_halt[0] = False
                rotation_right_halt[1] = 0

        # Update rotation for the next frame
        rotation_left += rotation_speed_left
        rotation_right += rotation_speed_right


        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

