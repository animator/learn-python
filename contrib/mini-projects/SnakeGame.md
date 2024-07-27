Here is the Snake Game code and necessary information in Markdown format:
Snake Game
Overview
A simple implementation of the classic Snake Game using Pygame.
Code
Python
import pygame
import sys
import time
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Set up title
pygame.display.set_caption('Snake Game')

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Set up snake and food
snake = [(200, 200), (220, 200), (240, 200)]
food = (400, 300)
direction = 'RIGHT'

# Set up score
score = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Move snake
    head = snake[-1]
    if direction == 'UP':
        new_head = (head[0], head[1] - 20)
    elif direction == 'DOWN':
        new_head = (head[0], head[1] + 20)
    elif direction == 'LEFT':
        new_head = (head[0] - 20, head[1])
    elif direction == 'RIGHT':
        new_head = (head[0] + 20, head[1])

    snake.append(new_head)

    # Check for collision with food
    if snake[-1] == food:
        score += 1
        food = (random.randint(0, width - 20) // 20 * 20, random.randint(0, height - 20) // 20 * 20)
    else:
        snake.pop(0)

    # Check for collision with wall or self
    if (snake[-1][0] < 0 or snake[-1][0] >= width or
        snake[-1][1] < 0 or snake[-1][1] >= height or
        snake[-1] in snake[:-1]):
        print(f'Game Over! Score: {score}')
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(black)
    for pos in snake:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 20, 20))
    pygame.draw.rect(screen, red, pygame.Rect(food[0], food[1], 20, 20))
    pygame.display.update()

    # Cap framerate
    time.sleep(0.1)
Setup
To run the game, make sure you have Pygame installed. You can install it using pip:
Bash
pip install pygame
Run
Save the code to a file (e.g., snake_game.py) and run it using Python:
Bash
python snake_game.py
Gameplay
Use the arrow keys to control the snake.
Eat the red food pellets to increase your score.
Avoid hitting the wall or yourself.
License
This code is released under the MIT License.