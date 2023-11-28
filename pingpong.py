import pygame

pygame.init()
HEIGHT, WIDTH = 600, 1000
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PingPong Game By Emil Dawood")
ball_x = (WIDTH * .5) - 15
ball_y = (HEIGHT * .5) - 15
radius = 20
# colors
RED = (255, 0, 0)
BLUE = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# paddle details
paddle_width = 30
paddle_height = 150
left_paddle_x, left_paddle_y = WIDTH - paddle_width, ball_y - (paddle_height / 2)
right_paddle_x, right_paddle_y = 0, ball_y - (paddle_height / 2)
run = True
# incrementaion
increment_ball_x, increment_ball_y = .2, .2
#gadget
gadget_right = gadget_left = 0
gadget_right_remain = gadget_left_remain = 5
while run:
    wn.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_DOWN:
                if left_paddle_y < HEIGHT - paddle_height:
                    left_paddle_y += 30
            elif i.key == pygame.K_UP:
                if (left_paddle_y > 0):
                    left_paddle_y -= 30
            elif i.key == pygame.K_RIGHT:
                gadget_left = 1
            elif i.key == pygame.K_d:
                gadget_right = 1
            elif i.key == pygame.K_a:
                gadget_right = 2
            elif i.key == pygame.K_LEFT:
                gadget_left = 2
            elif i.key == pygame.K_w:
                if right_paddle_y > 0:
                    right_paddle_y -= 30
            elif i.key == pygame.K_s:
                if right_paddle_y < HEIGHT - paddle_height:
                    right_paddle_y += 30
    if (gadget_left == 1 and gadget_left_remain > 0):
        if (ball_x >= left_paddle_x - radius and ball_y >= left_paddle_y  and ball_y <= left_paddle_y + paddle_height):
            increment_ball_x *= 3.5
            gadget_left = 0
            gadget_left_remain -= 1
    elif (gadget_left == 2 and gadget_left_remain  > 0):
        left_paddle_y = ball_y
        gadget_left = 0
        gadget_left_remain -= 1
    if (gadget_right == 1 and gadget_right_remain > 0):    
        if (ball_x <= paddle_width + radius and ball_y >= right_paddle_y  and ball_y <= right_paddle_y + paddle_height):
            increment_ball_x *= 3.5
            gadget_right = 0
            gadget_right_remain -= 1
    elif (gadget_right == 2 and gadget_left_remain > 0):
        right_paddle_y = ball_y
        gadget_right = 0
        gadget_right_remain -= 1
    if (ball_x >= left_paddle_x - radius and ball_y >= left_paddle_y  and ball_y <= left_paddle_y + paddle_height) or (ball_x <= paddle_width + radius and ball_y >= right_paddle_y  and ball_y <= right_paddle_y + paddle_height):
        increment_ball_x *=-1

    elif (ball_y >= HEIGHT - radius or ball_y <= radius):
        increment_ball_y *= -1
    elif (ball_x >= WIDTH - radius or ball_x <= radius):
        ball_x = (WIDTH * .5) - 15
        ball_y = (HEIGHT * .5) - 15
        increment_ball_x = .2
        increment_ball_x *= -1
    ball_x += increment_ball_x
    ball_y += increment_ball_y
    pygame.draw.rect(wn, WHITE, pygame.Rect(WIDTH / 2, 0, 5, HEIGHT / 2 - (radius / 2)))
    pygame.draw.circle(wn, RED, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, BLUE, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, BLUE, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, WHITE, pygame.Rect(WIDTH / 2, HEIGHT / 2 + radius, 5, HEIGHT / 2 - (radius / 2)))
    if (gadget_left == 1):
        pygame.draw.circle(wn, WHITE, (left_paddle_x + 10, left_paddle_y + 10), 8)
    if (gadget_right == 1):
        pygame.draw.circle(wn, WHITE, (right_paddle_x + 10, right_paddle_y + 10), 8)
    pygame.display.update()  
