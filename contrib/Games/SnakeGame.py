import pygame
import random

# Initialise pygame
pygame.init()

# Define colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
orange=(255,165,0)
green=(0,255,0)
# Dimensions
width,height=800,600

game_display=pygame.display.set_mode((width,height))
pygame.display.set_caption('Snake Game by DP')

clock=pygame.time.Clock()

snake_size=20
snake_speed=10

message_font=pygame.font.SysFont('ubuntu',30)
score_font=pygame.font.SysFont('ubuntu',25)

def print_score(score):
    score_text=score_font.render("Score: "+str(score),True,green)
    game_display.blit(score_text,[0,0])

# draw a rectangle snake dynamically with size=snake_size
def draw_snake(snake_size,snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [pixel[0],pixel[1],snake_size,snake_size])


def run_game():
    game_over=False
    game_close=False
    # start position of snake
    x=width/2
    y=height/2

    x_speed=0
    y_speed=0

    snake_pixels=[]
    snake_length=1

    target_x = round(random.randrange(0, width - snake_size)/20.0)*20.0
    target_y = round(random.randrange(0, height - snake_size)/20.0)*20.0

    while not game_over:
        while game_close:
            game_display.fill(black)
            game_over_message=message_font.render("Game Over!",True,red)
            game_display.blit(game_over_message,[width/3,height/3])
            print_score(snake_length-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_1:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_2:
                        run_game()
                if event.type==pygame.QUIT:
                    game_over=True
                    game_close=False



        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_speed=-snake_size
                    y_speed=0
                if event.key==pygame.K_RIGHT:
                    x_speed=snake_size
                    y_speed=0
                if event.key==pygame.K_UP:
                    x_speed=0
                    y_speed=-snake_size
                if event.key==pygame.K_DOWN:
                    x_speed=0
                    y_speed=snake_size
        if x>=width or x<0 or y>=height or y<0:
            game_close=True
        x+=x_speed
        y+=y_speed

        game_display.fill(black)
        pygame.draw.rect(game_display,orange,[target_x,target_y,snake_size,snake_size])

        snake_pixels.append([x,y])

        if len(snake_pixels)>snake_length:
            del snake_pixels[0]
        for pixel in snake_pixels[:-1]:
            if pixel == [x,y]:
                game_close=True

        draw_snake(snake_size,snake_pixels)
        print_score(snake_length-1)  # because starting from 1

        pygame.display.update()

        if x==target_x and y==target_y:
            target_x = round(random.randrange(0, width - snake_size) / 20.0) * 20.0
            target_y = round(random.randrange(0, height - snake_size) / 20.0) * 20.0
            snake_length += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()


run_game()
