import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Ball properties
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

# Paddles
player = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 60, 10, 120)
opponent = pygame.Rect(10, HEIGHT // 2 - 60, 10, 120)

# Game variables
player_speed = 0
opponent_speed = 7

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            elif event.key == pygame.K_UP:
                player_speed -= 7
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            elif event.key == pygame.K_UP:
                player_speed += 7

    # Game logic
    player.y += player_speed

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # AI opponent movement
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    # Drawing the elements
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Updating the display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
