import pygame
import random

# Initialize pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set snake and food dimensions
BLOCK_SIZE = 20

# Initialize screen
logo = pygame.image.load("Rishi Developer.png")  # Replace "logo.png" with the path to your logo image
logo = pygame.transform.scale(logo, (100, 100))  # Resize the logo if needed

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling the game's FPS
clock = pygame.time.Clock()

# Function to display score
def display_score(score):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (10, 10))

# Function to draw snake
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

# Function to generate random food position
def generate_food():
    food_x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    return food_x, food_y

# Function to display message
def display_message(msg, color):
    font = pygame.font.SysFont(None, 50)
    text = font.render(msg, True, color)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(2000)

# Function to handle collision with walls
def check_wall_collision(snake_head):
    if snake_head[0] < 0 or snake_head[0] >= SCREEN_WIDTH or snake_head[1] < 0 or snake_head[1] >= SCREEN_HEIGHT:
        return True
    return False

# Main function for the game
def game_loop():
    # Initialize snake
    snake_list = []
    snake_length = 1
    snake_head = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
    snake_speed_x = 0
    snake_speed_y = 0

    # Initialize food
    food_x, food_y = generate_food()

    # Initialize game variables
    game_over = False
    score = 0

    # Game loop
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_speed_x = -BLOCK_SIZE
                    snake_speed_y = 0
                elif event.key == pygame.K_RIGHT:
                    snake_speed_x = BLOCK_SIZE
                    snake_speed_y = 0
                elif event.key == pygame.K_UP:
                    snake_speed_y = -BLOCK_SIZE
                    snake_speed_x = 0
                elif event.key == pygame.K_DOWN:
                    snake_speed_y = BLOCK_SIZE
                    snake_speed_x = 0

        # Update snake position
        snake_head[0] += snake_speed_x
        snake_head[1] += snake_speed_y

        # Check collision with walls
        if check_wall_collision(snake_head):
            game_over = True
            display_message("Game Over!", RED)
            continue

        # Add snake's head to snake_list
        snake_list.append(list(snake_head))
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check collision with food
        if snake_head[0] == food_x and snake_head[1] == food_y:
            food_x, food_y = generate_food()
            snake_length += 1
            score += 1

        # Clear screen
        screen.fill(WHITE)

        # Draw food
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Draw snake
        draw_snake(snake_list)

        # Display score
        display_score(score)

        # Update display
        pygame.display.update()

        # Set game speed
        clock.tick(10)

# Start the game loop
game_loop()