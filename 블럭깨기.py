import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Game levels
def init_level(level):
    ball_speed_x, ball_speed_y = 5 + level, -5 - level
    blocks = [pygame.Rect(x * 52, y * 22, 50, 20) for x in range(10) for y in range(3 + level)]
    return ball_speed_x, ball_speed_y, blocks

# Initial game setup
level = 1
paddle_width, paddle_height = 100, 10
ball_diameter = 10
paddle_speed = 0
paddle = pygame.Rect((screen_width - paddle_width) / 2, screen_height - paddle_height - 20, paddle_width, paddle_height)
ball_speed_x, ball_speed_y, blocks = init_level(level)
ball = pygame.Rect(paddle.x + paddle_width / 2, paddle.y - ball_diameter, ball_diameter, ball_diameter)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_speed = -6
            if event.key == pygame.K_RIGHT:
                paddle_speed = 6
        if event.type == pygame.KEYUP:
            paddle_speed = 0
    
    # Move paddle
    paddle.x += paddle_speed
    if paddle.left < 0:
        paddle.left = 0
    if paddle.right > screen_width:
        paddle.right = screen_width
    
    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y
    if ball.colliderect(paddle):
        ball_speed_y = -ball_speed_y
    
    # Block collision
    for block in blocks[:]:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y
            break
    
    # Level progression
    if not blocks:
        level += 1
        if level > 10:
            print("You've completed the game!")
            running = False
        ball_speed_x, ball_speed_y, blocks = init_level(level)
        ball.x, ball.y = paddle.x + paddle_width / 2, paddle.y - ball_diameter
    
    # Game over
    if ball.bottom >= screen_height:
        print("Game Over")
        running = False

    # Drawing
    screen.fill(black)
    for block in blocks:
        pygame.draw.rect(screen, red, block)
    pygame.draw.rect(screen, white, paddle)
    pygame.draw.ellipse(screen, white, ball)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
