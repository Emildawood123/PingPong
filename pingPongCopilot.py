import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Ping Pong")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the game variables
ball_x = window_width // 2
ball_y = window_height // 2
ball_radius = 10
ball_speed_x = 3
ball_speed_y = 3

paddle_width = 10
paddle_height = 60
paddle_speed = 5

paddle1_x = 10
paddle1_y = window_height // 2 - paddle_height // 2
paddle2_x = window_width - paddle_width - 10
paddle2_y = window_height // 2 - paddle_height // 2

score1 = 0
score2 = 0

# Get player names
player1_name = input("Enter Player 1 name: ")
player2_name = input("Enter Player 2 name: ")

running = True

# Game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < window_height - paddle_height:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < window_height - paddle_height:
        paddle2_y += paddle_speed

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with paddles
    if ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height:
        ball_speed_x = abs(ball_speed_x)
    if ball_x >= paddle2_x - ball_radius and paddle2_y <= ball_y <= paddle2_y + paddle_height:
        ball_speed_x = -abs(ball_speed_x)

    # Ball collision with walls
    if ball_y <= 0 or ball_y >= window_height - ball_radius:
        ball_speed_y = -ball_speed_y

    # Ball out of bounds
    if ball_x <= 0:
        score2 += 1
        ball_x = window_width // 2
        ball_y = window_height // 2
    elif ball_x >= window_width:
        score1 += 1
        ball_x = window_width // 2
        ball_y = window_height // 2

    # Check for winner
    if score1 == 5 or score2 == 5:
        running = False

    # Clear the window
    window.fill((0, 0, 0))

    # Draw paddles
    pygame.draw.rect(window, (255, 255, 255), (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(window, (255, 255, 255), (paddle2_x, paddle2_y, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.circle(window, (255, 255, 255), (ball_x, ball_y), ball_radius)

    # Draw scores
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"{player1_name}: {score1}  {player2_name}: {score2}", True, (255, 255, 255))
    window.blit(score_text, (window_width // 2 - score_text.get_width() // 2, 10))

    # Update the window
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Determine the winner
winner = player1_name if score1 == 5 else player2_name
print(f"The winner is {winner}!")

# Quit the game
pygame.quit()
