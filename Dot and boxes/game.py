import pygame
import os
import math
from enum import Enum
from typing import List
from player import Player
from box import Box

"""
red: 255, 255, 255
blue: 44, 79, 182
green: 27, 150, 13
orange: 246, 108, 0
"""

pygame.init()

WIDTH = 1000
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dots and Boxes')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 60)
big_font = pygame.font.Font(None, 120)

images = {}
for filename in os.listdir('images'):
    images[filename.replace('.png', '')] = pygame.image.load('images/' + filename)

player_select_buttons = [
    ['human', 'red', pygame.Rect(0, 0, 48, 48)],
    ['human', 'blue', pygame.Rect(0, 0, 48, 48)],
    ['human', 'green', pygame.Rect(0, 0, 48, 48)],
    ['human', 'orange', pygame.Rect(0, 0, 48, 48)]
]

background = images['wood_background']
icon = images['icon']
title = pygame.transform.smoothscale(images['title'], (800, 100))
arrow_right = images['arrow_right']
arrow_left = images['arrow_left']

pygame.display.set_icon(icon)

start = font.render('Start', True, (50, 50, 50))
start_rect = start.get_rect(center=(WIDTH / 2, 660))
turn = font.render('Turn', True, (89, 82, 69))
turn_rect = turn.get_rect(center=(WIDTH / 2 + 30, 70))
paused_rect = images['paused'].get_rect(center=(WIDTH / 2, 80))
resume = font.render('Resume', True, (255, 255, 255))
resume_rect = resume.get_rect(midtop=(WIDTH / 2, 310))
quit_game = font.render('Quit Game', True, (255, 255, 255))
quit_game_rect = quit_game.get_rect(midtop=(WIDTH / 2, 450))
board_size = font.render('Board Size', True, (89, 82, 69))
board_size_rect = board_size.get_rect(midbottom=(WIDTH / 2, 470))
difficulty_text = font.render('Difficulty:', True, (89, 82, 69))
difficulty_rect = difficulty_text.get_rect(center=(WIDTH / 2 - 80, 585))
diff = font.render('Easy', True, (89, 82, 69))
diff_rect = diff.get_rect(center=(WIDTH / 2 + 105, 585))

menu_rect = pygame.Rect(300, 225, 400, 500)
num_left_arrow_rect = arrow_left.get_rect(left=330, centery=300)
num_right_arrow_rect = arrow_right.get_rect(right=670, centery=300)
left_size_rect = arrow_left.get_rect(center=(400, 510))
right_size_rect = arrow_right.get_rect(center=(600, 510))


class GameStates(Enum):
    menu = 0
    playing = 1
    finish = 2


game_state = GameStates.menu

sizes = [
    (4, 3),
    (6, 5),
    (8, 6),
    (10, 8),
    (12, 9),
]
size_idx = 2
size = 8, 6
num_players = 2
curr_player = 0
player_win = 0
tie = False
paused = False
spacing = 50  # 50
player_select_spacing = 90
score_spacing = 200
fade = 10
alpha = 0
last_line = None
an_cycle = 0
an_time = 10
difficulty = 1

players: List[Player] = []
boxes: List[Box] = []
lines = []
animating = False
animation_line = []
move = ()


def get_diff_type():
    return ('Easy', 'Medium', 'Hard', 'Extreme')[difficulty - 1]


def get_boxes_around(y, x):
    check = {}
    if x > 0:
        check['left'] = boxes[y][x - 1]
    if x < size[0] - 1:
        check['right'] = boxes[y][x + 1]
    if y > 0:
        check['top'] = boxes[y - 1][x]
    if y < size[1] - 1:
        check['bottom'] = boxes[y + 1][x]

    return check


def get_dots_around(y, x):
    check = []
    if x > 0:
        check.append((y, x - 1))
    if x < size[0]:
        check.append((y, x + 1))
    if y > 0:
        check.append((y - 1, x))
    if y < size[1]:
        check.append((y + 1, x))

    return check


def add_vec(p, v):
    return p[0] + v[0], p[1] + v[1]


def idx_pos(y, x):
    left = (WIDTH - size[0] * spacing) / 2
    top = (HEIGHT - size[1] * spacing) / 2
    return left + x * spacing, top + y * spacing


def pos_idx(x, y):
    left = (WIDTH - size[0] * spacing) / 2
    top = (HEIGHT - size[1] * spacing) / 2
    y_idx = int((y - top) / spacing)
    x_idx = int((x - left) / spacing)
    return y_idx, x_idx


def near(a, b, d=20):
    return math.dist(a, b) <= d


def loop_dots():
    width = size[0] * spacing
    height = size[1] * spacing
    left = (WIDTH - width) / 2
    top = (HEIGHT - height) / 2
    for x in range(size[0] + 1):
        x_pos = left + x * spacing
        for y in range(size[1] + 1):
            y_pos = top + y * spacing
            yield x_pos, y_pos


def draw_back():
    width = (size[0] + 2) * spacing
    height = (size[1] + 2) * spacing
    board_rect = pygame.Rect((WIDTH - width) / 2, (HEIGHT - height) / 2, width, height)
    pygame.draw.rect(screen, (224, 187, 122), board_rect, border_radius=25)
    pygame.draw.rect(screen, (50, 50, 50), board_rect, 10, border_radius=25)


def draw_dots():
    for x_pos, y_pos in loop_dots():
        pygame.draw.circle(screen, 'white', (x_pos, y_pos), 10)  # 10
        pygame.draw.circle(screen, 'black', (x_pos, y_pos), 10, 3)  # 3


def draw_boxes():
    for box in Box.ALL_BOXES:
        pos = idx_pos(*box.idx)
        if box.color is not None:
            pygame.draw.rect(screen, box.color, pos + (spacing, spacing))


def draw_lines():
    for idx in range(len(lines)):
        line = lines[idx]
        if idx == len(lines) - 1:
            pygame.draw.line(screen, (100, 100, 100), line[0], line[1], 10)
        else:
            pygame.draw.line(screen, (50, 50, 50), line[0], line[1], 10)


def draw_menu():
    screen.blit(title, title.get_rect(center=(WIDTH / 2, 100)))
    pygame.draw.rect(screen, (224, 187, 122), menu_rect, border_radius=25)
    pygame.draw.rect(screen, (50, 50, 50), menu_rect, 10, border_radius=25)
    text = font.render(str(num_players) + ' Players', True, (89, 82, 69))
    screen.blit(text, text.get_rect(center=(WIDTH / 2, 300)))
    screen.blit(arrow_left, num_left_arrow_rect)
    screen.blit(arrow_right, num_right_arrow_rect)

    width = (num_players - 1) * player_select_spacing
    left = (WIDTH - width) / 2
    for count, player_button in enumerate(player_select_buttons[:num_players]):
        player_button[2].midtop = left + player_select_spacing * count, 350

        screen.blit(images[player_button[0] + '_' + player_button[1]], player_button[2])

    screen.blit(board_size, board_size_rect)
    size_text = font.render(f'{size[0]} x {size[1]}', True, (89, 82, 69))
    screen.blit(size_text, size_text.get_rect(center=(WIDTH / 2, 510)))
    screen.blit(arrow_left, left_size_rect)
    screen.blit(arrow_right, right_size_rect)

    screen.blit(difficulty_text, difficulty_rect)
    screen.blit(diff, diff_rect)

    screen.blit(start, start_rect)


def draw_playing():
    screen.blit(images['hamburger'], (5, 5))
    screen.blit(turn, turn_rect)
    draw_back()
    draw_boxes()
    draw_lines()
    if players[curr_player].start is not None:
        pygame.draw.line(screen, players[curr_player].color, idx_pos(*players[curr_player].start), mouse_pos(), 10)
    if animating:
        pygame.draw.line(screen, players[curr_player].color, animation_line[0], animation_line[1], 10)
    draw_dots()

    left = (WIDTH - score_spacing * (num_players - 1)) / 2
    for count, select_button in enumerate(player_select_buttons[:num_players]):
        if count == curr_player:
            select_button[2].center = WIDTH / 2 - 50, 70
            screen.blit(images[select_button[0] + '_' + select_button[1]], select_button[2])
        select_button[2].midtop = left + score_spacing * count, 700
        screen.blit(images[select_button[0] + '_' + select_button[1]], select_button[2])
        score_ = font.render(str(players[count].score), True, (50, 50, 50))
        screen.blit(score_, score_.get_rect(centery=select_button[2].centery, left=select_button[2].right + 15))

    if paused:
        overlay = pygame.Surface(size=(WIDTH, HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(120)
        screen.blit(overlay, (0, 0))
        screen.blit(images['paused'], paused_rect)
        screen.blit(resume, resume_rect)
        screen.blit(quit_game, quit_game_rect)


def draw_finish():
    global alpha, fade
    if alpha < 255:
        alpha += fade
    elif alpha > 255:
        alpha = 255

    draw_back()
    draw_boxes()
    draw_lines()
    draw_dots()

    left = (WIDTH - score_spacing * (num_players - 1)) / 2
    for count, select_button in enumerate(player_select_buttons[:num_players]):
        select_button[2].midtop = left + score_spacing * count, 700
        screen.blit(images[select_button[0] + '_' + select_button[1]], select_button[2])
        score_ = font.render(str(players[count].score), True, (50, 50, 50))
        screen.blit(score_, score_.get_rect(centery=select_button[2].centery, left=select_button[2].right + 15))

    overlay = pygame.Surface(size=(WIDTH, HEIGHT))
    overlay.fill((0, 0, 0))
    overlay.set_alpha(math.floor(alpha / 2))
    screen.blit(overlay, (0, 0))
    if alpha == 255:
        over = big_font.render('Game Over', True, (50, 50, 50))
        screen.blit(over, over.get_rect(midtop=(WIDTH / 2, 50)))
        if tie:
            win = font.render('Tie', True, (50, 50, 50))
            screen.blit(win, win.get_rect(center=(WIDTH / 2, 200)))
        else:
            win = font.render('Winner:', True, (50, 50, 50))
            screen.blit(win, win.get_rect(midright=(WIDTH / 2 + 40, 200)))
            winner = player_select_buttons[player_win]
            winner[2].midleft = WIDTH / 2 + 55, 200
            screen.blit(images[winner[0] + '_' + winner[1]], winner[2])


def animate_line(pos1, pos2):
    global animating, animation_line, an_cycle, an_time
    if an_time == 0:
        p = 1
    else:
        p = an_cycle / an_time
    nx = pos2[0] * p + pos1[0] * (1 - p)
    ny = pos2[1] * p + pos1[1] * (1 - p)
    animation_line = [pos1, (nx, ny)]
    an_cycle += 1
    if an_cycle > an_time:
        animating = False
        an_cycle = 0


def start_game():
    global game_state, players, curr_player, paused, boxes, animation_line, an_cycle, animating, lines, alpha, difficulty
    game_state = GameStates.playing
    an_cycle = 0
    animation_line = []
    animating = False
    alpha = 0

    paused = False

    players = [
                  Player(player_select_buttons[0][0], (255, 0, 0), difficulty),
                  Player(player_select_buttons[1][0], (44, 79, 182), difficulty),
                  Player(player_select_buttons[2][0], (27, 150, 13), difficulty),
                  Player(player_select_buttons[3][0], (246, 108, 0), difficulty)
              ][:num_players]
    curr_player = 0

    Box.ALL_BOXES.clear()
    Box.BOXES_DONE = 0
    boxes = []
    lines = []
    for y in range(size[1]):
        row = []
        for x in range(size[0]):
            row.append(Box(y, x))
        boxes.append(row)


def mouse_pos():
    return pygame.mouse.get_pos()


def next_turn():
    global curr_player
    curr_player += 1
    if curr_player == num_players:
        curr_player = 0


def add_line(idx_pos1, idx_pos2, color):
    global last_line
    count = 0
    if idx_pos1[0] == idx_pos2[0]:  # horizontal
        pos1 = min(idx_pos1, idx_pos2, key=lambda x: x[1])

        if pos1[0] > 0:
            box_top = boxes[pos1[0] - 1][pos1[1]]
            box_top.bottom = color
            if box_top.color is not None:
                count += 1

        if pos1[0] < size[1]:
            box_bottom = boxes[pos1[0]][pos1[1]]
            box_bottom.top = color
            if box_bottom.color is not None:
                count += 1
    else:
        pos1 = min(idx_pos1, idx_pos2, key=lambda x: x[0])

        if pos1[1] > 0:
            box_left = boxes[pos1[0]][pos1[1] - 1]
            box_left.right = color
            if box_left.color is not None:
                count += 1

        if pos1[1] < size[0]:
            box_right = boxes[pos1[0]][pos1[1]]
            box_right.left = color
            if box_right.color is not None:
                count += 1
    lines.append((idx_pos(*idx_pos1), idx_pos(*idx_pos2)))
    last_line = idx_pos1, idx_pos2
    return count


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == GameStates.menu:
                if num_players > 2 and num_left_arrow_rect.collidepoint(event.pos):  # players -1
                    num_players -= 1
                elif num_players < 4 and num_right_arrow_rect.collidepoint(event.pos):  # players +1
                    num_players += 1
                elif start_rect.collidepoint(event.pos):  # start game
                    start_game()
                elif size_idx > 0 and left_size_rect.collidepoint(event.pos):  # check if user changed board size
                    size_idx -= 1
                    size = sizes[size_idx]
                elif size_idx < len(sizes) - 1 and right_size_rect.collidepoint(event.pos):
                    size_idx += 1
                    size = sizes[size_idx]
                elif diff_rect.collidepoint(event.pos):
                    difficulty = difficulty % 4 + 1
                    diff = font.render(get_diff_type(), True, (89, 82, 69))
                    diff_rect = diff.get_rect(center=(WIDTH / 2 + 105, 585))
                else:  # changed player type
                    for index, button in enumerate(player_select_buttons[:num_players]):
                        if button[2].collidepoint(mouse_pos()):
                            if button[0] == 'human':
                                button[0] = 'computer'
                            else:
                                button[0] = 'human'
                            break
            elif game_state == GameStates.playing:
                if paused:
                    if resume_rect.collidepoint(event.pos):
                        paused = False
                    elif quit_game_rect.collidepoint(event.pos):
                        game_state = GameStates.menu
                else:
                    if images['hamburger'].get_rect(topleft=(5, 5)).collidepoint(event.pos):
                        paused = True
                    elif players[curr_player].player_type == 'human':
                        found = False
                        for dot in loop_dots():
                            if near(event.pos, dot):
                                players[curr_player].start = pos_idx(*dot)
                                found = True
                                break
                        if not found:
                            players[curr_player].start = None
            elif game_state == GameStates.finish:
                game_state = GameStates.menu

        elif event.type == pygame.MOUSEBUTTONUP:
            if game_state == GameStates.playing and not paused:
                if players[curr_player].player_type == 'human' and players[curr_player].start is not None:
                    found = False
                    for dot in get_dots_around(*players[curr_player].start):
                        if near(event.pos, idx_pos(*dot)):
                            found = dot
                            break
                    if found:
                        p1 = idx_pos(*players[curr_player].start)
                        p2 = idx_pos(*found)
                        if ((p1, p2) in lines) or ((p2, p1) in lines):
                            found = False
                        if found:
                            players[curr_player].move = [players[curr_player].start, found]
                    players[curr_player].start = None

    if game_state == GameStates.playing and not paused:
        if players[curr_player].player_type == 'human':
            move = players[curr_player].get_move(boxes, last_line)
            if move is not None:
                score = add_line(*move, players[curr_player].color)
                if score == 0:
                    players[curr_player].move = None
                    next_turn()
                else:
                    players[curr_player].score += score
        else:
            if not animating:
                move = players[curr_player].get_move(boxes, last_line)
            animating = True
            animate_line(idx_pos(*move[0]), idx_pos(*move[1]))
            if not animating:
                score = add_line(*move, players[curr_player].color)
                players[curr_player].move = None
                if score == 0:
                    next_turn()
                else:
                    players[curr_player].score += score

        if Box.BOXES_DONE == size[0] * size[1]:
            game_state = GameStates.finish
            rankings = sorted(players, key=lambda x: x.score, reverse=True)
            tie = rankings[0].score == rankings[1].score
            player_win = players.index(rankings[0])

    screen.blit(background, (0, 0))

    if game_state == GameStates.menu:
        draw_menu()
    elif game_state == GameStates.playing:
        draw_playing()
    elif game_state == GameStates.finish:
        draw_finish()

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
