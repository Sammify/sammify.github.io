import pygame
import sys
import math
import random

pygame.init()

game_over = False

height = 500
width = 1000

CHANCE_OF_MOVE = 25

BLACK = pygame.Color("black")
WHITE = pygame.Color("white")

LINE_WIDTH = 4

BALL_SIZE = 20
ball_pos = [(width - BALL_SIZE)/2, (height- BALL_SIZE)/2]
ball_speed = 10
ball_direction = random.uniform(0-math.pi, math.pi)

PLAYER_DISTANCE = 15
PLAYER_WIDTH = 10
PLAYER_LENGTH = 75
SENSITIVITY = 25

player1_pos = [PLAYER_DISTANCE, (height - PLAYER_LENGTH)/2]
player2_pos = [width - PLAYER_DISTANCE - PLAYER_WIDTH, (height - PLAYER_LENGTH)/2]

SMOOTHNESS = 10

score = [0, 0]

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

SPACE_BETWEEN_SCORES = 20
DISTANCE_FROM_TOP = 10
FONT = 'monospace'
FONT_SIZE = 35

MyFont = pygame.font.SysFont(FONT, FONT_SIZE)

def ball_out_of_bounds(ball_direction):
	global score, ball_pos

	if ball_pos[0] <= 0:
		score[1] += 1
		ball_pos = [(width - BALL_SIZE)/2, (height- BALL_SIZE)/2]
		ball_direction = random.uniform(0-math.pi, math.pi)
		clock.tick(500)

	elif ball_pos[1] <= 0:
		ball_direction = 0 - ball_direction

	elif ball_pos[0] >= width - BALL_SIZE:
		score[0] += 1
		ball_pos = [(width - BALL_SIZE)/2, (height- BALL_SIZE)/2]
		ball_direction = random.uniform(0-math.pi, math.pi)
		clock.tick(500)

	elif ball_pos[1] >= height - BALL_SIZE:
		ball_direction = 0 - ball_direction

	return ball_direction

def ball_hiting_player(ball_direction):

	xb = ball_pos[0]
	yb = ball_pos[1]
	x1 = player1_pos[0]
	y1 = player1_pos[1]
	x2 = player2_pos[0]
	y2 = player2_pos[1]

	if ((x1 > xb and x1 < (xb + BALL_SIZE)) or (xb >= x1 and xb < (x1 + PLAYER_WIDTH))) and ((y1 >= yb and y1 < (yb + BALL_SIZE)) or (yb >= y1 and yb < (y1 + PLAYER_LENGTH))):
		ball_direction = random.uniform(0-math.pi/2, math.pi/2)

	elif ((x2 > xb and x2 < (xb + BALL_SIZE)) or (xb >= x2 and xb < (x2 + PLAYER_WIDTH))) and ((y2 >= yb and y2 < (yb + BALL_SIZE)) or (yb >= y2 and yb < (y2 + PLAYER_LENGTH))):
		ball_direction = random.uniform(math.pi/2, 3*math.pi/2)

	return ball_direction

def draw_image():
	global ball_pos, ball_direction, screen
	screen.fill(BLACK)

	ball_pos[0] += BALL_SIZE * math.cos(ball_direction) / SMOOTHNESS
	ball_pos[1] -= BALL_SIZE * math.sin(ball_direction) / SMOOTHNESS

	pygame.draw.rect(screen, WHITE, (ball_pos[0], ball_pos[1], BALL_SIZE, BALL_SIZE))

	pygame.draw.rect(screen, WHITE, (PLAYER_DISTANCE, player1_pos[1], PLAYER_WIDTH, PLAYER_LENGTH))
	pygame.draw.rect(screen, WHITE, (width - PLAYER_DISTANCE - PLAYER_WIDTH, player2_pos[1], PLAYER_WIDTH, PLAYER_LENGTH))

	pygame.draw.rect(screen, WHITE, ((width - LINE_WIDTH)/2, 0, LINE_WIDTH, height))

	score1_text = str(score[0])
	label = MyFont.render(score1_text, 1, WHITE)
	screen.blit(label, (width/2 - label.get_width() - SPACE_BETWEEN_SCORES/2, DISTANCE_FROM_TOP))

	score2_text = str(score[1])
	label = MyFont.render(score2_text, 1, WHITE)
	screen.blit(label, (width/2 + SPACE_BETWEEN_SCORES/2, DISTANCE_FROM_TOP))

	pygame.display.update()

	ball_direction = ball_out_of_bounds(ball_direction)
	ball_direction = ball_hiting_player(ball_direction)

while not game_over:
	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:

			y1 = player1_pos[1]

			if event.key == pygame.K_UP:
				if y1 >= SENSITIVITY:
					y1 -= SENSITIVITY

			if event.key == pygame.K_DOWN:
				if y1 <= height - SENSITIVITY - PLAYER_LENGTH:
					y1 += SENSITIVITY

			player1_pos[1] = y1

	if player2_pos[1]+PLAYER_LENGTH/2 > ball_pos[1] and random.choice([False if i != CHANCE_OF_MOVE-1 else True for i in range(CHANCE_OF_MOVE)]) and ball_pos[0]>width/3:
		if player2_pos[1] >= SENSITIVITY:
			player2_pos[1] -= SENSITIVITY

	if player2_pos[1]+PLAYER_LENGTH/2 < ball_pos[1] and random.choice([False if i != CHANCE_OF_MOVE-1 else True for i in range(CHANCE_OF_MOVE)]) and ball_pos[0]>width/3:
		if player2_pos[1] <= height - SENSITIVITY - PLAYER_LENGTH:
			player2_pos[1] += SENSITIVITY

	draw_image()

	clock.tick(1000*ball_speed/SMOOTHNESS)