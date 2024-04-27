import pygame
import sys


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball parameters
ball_radius = 25
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed = 20

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    screen.fill(WHITE)  # Fill the screen with white

    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - ball_speed >= ball_radius:
                    ball_y -= ball_speed
            elif event.key == pygame.K_DOWN:
                if ball_y + ball_speed <= screen_height - ball_radius:
                    ball_y += ball_speed
            elif event.key == pygame.K_LEFT:
                if ball_x - ball_speed >= ball_radius:
                    ball_x -= ball_speed
            elif event.key == pygame.K_RIGHT:
                if ball_x + ball_speed <= screen_width - ball_radius:
                    ball_x += ball_speed

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
