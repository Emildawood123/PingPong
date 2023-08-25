import pygame
pygame.init()
ball_x, ball_y = 485, 235
HEIGHT, WIDTH = 500, 1000
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ping pong game py")
run = True
while run:
    wn.fill((0, 0, 0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    ball_x += 10
    pygame.draw.circle(wn, (0, 0, 255), (ball_x, 250 - 15), 15)
    pygame.draw.rect(wn, (255, 0, 0), pygame.Rect(10, 250 - 20, 10, 75))
    pygame.draw.rect(wn, (255, 0, 0), pygame.Rect(990, 250 - 20, 10, 75))
    pygame.display.update()
