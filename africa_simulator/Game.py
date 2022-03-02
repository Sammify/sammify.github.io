import pygame
import random
from math import sqrt

pygame.init()

#Colours
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
LIGHT_BLUE = (164,211,238)

#Loading images and textures
BACKGROUND = pygame.image.load("images/poor city.png")
PLUS = pygame.image.load("images/Plus sign.png")
MINUS = pygame.image.load("images/Minus sign.png")
UNICEF = pygame.image.load("images/UNICEF.png")

#Object representing a mouse
class Mouse:

	def __init__(self, pos=(0,0), down=False):
		self.pos = pos
		self.down = down

#Defining the width and the height
WIDTH = 1024
HEIGHT = 512

LIST_OF_NAMES = ['Maria', 'Nushi', 'Mohammed', 'Jose', 'Muhammad', 'Mohamed', 'Wei', 'Mohammad', 'Ahmed', 'Yan', 'Ali', 'John', 'David', 'Li', 'Abdul', 'Ana', 'Ying', 'Michael', 'Juan', 'Anna', 'Mary', 'Jean', 'Robert', 'Daniel', 'Luis', 'Carlos', 'James', 'Antonio', 'Joseph', 'Hui', 'Elena', 'Francisco', 'Hong', 'Marie', 'Min', 'Lei', 'Yu', 'Ibrahim', 'Peter', 'Fatima', 'Aleksandr', 'Richard', 'Xin', 'Bin', 'Paul', 'Ping', 'Lin', 'Olga', 'Sri', 'Pedro', 'William', 'Rosa', 'Thomas', 'Jorge', 'Yong', 'Elizabeth', 'Sergey', 'Ram', 'Patricia', 'Hassan', 'Anita', 'Manuel', 'Victor', 'Sandra', 'Ming', 'Siti', 'Miguel', 'Emmanuel', 'Samuel', 'Ling', 'Charles', 'Sarah', 'Mario', 'Joao', 'Tatyana', 'Mark', 'Rita', 'Martin', 'Svetlana', 'Patrick', 'Natalya', 'Qing', 'Ahmad', 'Martha', 'Andrey', 'Sunita', 'Andrea', 'Christine', 'Irina', 'Laura', 'Linda', 'Marina', 'Carmen', 'Ghulam', 'Vladimir', 'Barbara', 'Angela', 'George', 'Roberto', 'Peng', 'Ivan', 'Alexander', 'Ekaterina', 'Qiang', 'Yun', 'Jesus', 'Susan', 'Sara', 'Noor', 'Mariam', 'Dmitriy', 'Eric', 'Zahra', 'Fatma', 'Fernando', 'Esther', 'Jin', 'Diana', 'Mahmoud', 'Chao', 'Rong', 'Santosh', 'Nancy', 'Musa', 'Anh', 'Omar', 'Jennifer', 'Gang', 'Yue', 'Claudia', 'Maryam', 'Gloria', 'Ruth', 'Teresa', 'Sanjay', 'Na', 'Nur', 'Kyaw', 'Francis', 'Amina', 'Denis', 'Stephen', 'Sunil', 'Gabriel', 'Andrew', 'Eduardo', 'Abdullah', 'Grace', 'Anastasiya', 'Mei', 'Rafael', 'Ricardo', 'Christian', 'Aleksey', 'Steven', 'Gita', 'Frank', 'Jianhua', 'Mo', 'Karen', 'Masmaat', 'Brian', 'Christopher', 'Xiaoyan', 'Rajesh', 'Mustafa', 'Eva', 'Bibi', 'Monica', 'Oscar', 'Andre', 'Catherine', 'Kai', 'Ramesh', 'Liping', 'Sonia', 'Anthony', 'Mina', 'Manoj', 'Ashok', 'Rose', 'Alberto', 'Ning', 'Rekha', 'Chen', 'Lan', 'Aung', 'Alex', 'Suresh', 'Anil', 'Fatemeh', 'Julio']#eval(open("names.txt").read())

#Setting player stats
day = 1
budget = 200
water_investments = 0
food_investments = 0
saved_kids = 0

game_on = True

#Setting up environment
water_needs = [0, ""]
food_needs = [0, ""]

#Setting up keyboard tracking
keyboard = {pygame.K_a:False, pygame.K_b:False, pygame.K_c:False, pygame.K_d:False, pygame.K_e:False, pygame.K_f:False, pygame.K_g:False, pygame.K_h:False, pygame.K_i:False, pygame.K_j:False, pygame.K_k:False, pygame.K_l:False, pygame.K_m:False, pygame.K_n:False, pygame.K_o:False, pygame.K_p:False, pygame.K_q:False, pygame.K_r:False, pygame.K_s:False, pygame.K_t:False, pygame.K_u:False, pygame.K_v:False, pygame.K_w:False, pygame.K_x:False, pygame.K_y:False, pygame.K_z:False}
translate = {'a':pygame.K_a, 'b':pygame.K_b, 'c':pygame.K_c, 'd':pygame.K_d, 'e':pygame.K_e, 'f':pygame.K_f, 'g':pygame.K_g, 'h':pygame.K_h, 'i':pygame.K_i, 'j':pygame.K_j, 'k':pygame.K_k, 'l':pygame.K_l, 'm':pygame.K_m, 'n':pygame.K_n, 'o':pygame.K_o, 'p':pygame.K_p, 'q':pygame.K_q, 'r':pygame.K_r, 's':pygame.K_s, 't':pygame.K_t, 'u':pygame.K_u, 'v':pygame.K_v, 'w':pygame.K_w, 'x':pygame.K_x, 'y':pygame.K_y, 'z':pygame.K_z}

#Know if a letter is pressed
def pressed(letter):
	return keyboard[translate[letter]]

# pygame.display.set_caption("UNICEF game")

FONT = pygame.font.Font("Arial.ttf", 20)

clock = pygame.time.Clock()

fps = 10

mouse = Mouse()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

current_time = 0

start_of_day = 0

#Write text to the screen
def write_text(string, pos=(0, 0), font=FONT, colour=BLACK):
	label = font.render(string, 1, colour)
	screen.blit(label, pos)

#write text with back colour
def write_text_with_back(text, outline, pos):
	written_text = text[0]
	font = text[1]
	text_colour = text[2]

	outline_width = outline[0]
	outline_colour = outline[1]

	label = font.render(written_text, 1, BLACK)
	text_width, text_height = label.get_width(), label.get_height()
	pygame.draw.rect(screen, outline_colour, (pos[0], pos[1], text_width + 2 * outline_width, text_height + 2 * outline_width))
	write_text(written_text, (pos[0] + outline_width, pos[1] + outline_width), font, text_colour)

#place plus or minus
def place_plus(pos):
	screen.blit(PLUS, (pos[0] - PLUS.get_width()/2, pos[1] - PLUS.get_height()/2))

def place_minus(pos):
	screen.blit(MINUS, (pos[0] - MINUS.get_width()/2, pos[1] - MINUS.get_height()/2))

def circle_col(center, radius, point):
	return sqrt((center[0] - point[0])**2 + (center[1] - point[1])**2) < radius

#draws the image on screen
def draw_image():

	global start_of_day, water_needs, food_needs, day, game_on, budget, water_investments, food_investments, win, saved_kids

	#######LOGIC#######
	if game_on:

		if (current_time - start_of_day < 25000 or day == 5) and not water_needs[0] and random.uniform(0, 150/day) < 1:
			value = int(random.uniform(10, 100))
			water_needs = [value, "     "+random.choice(LIST_OF_NAMES)+" needs "+str(value)+"$ of water"]

		if (current_time - start_of_day < 25000 or day == 5) and not food_needs[0] and random.uniform(0, 150/day) < 1:
			value = int(random.uniform(10, 100))
			food_needs = [value, "     "+random.choice(LIST_OF_NAMES)+" needs "+str(value)+"$ of food"]

		if current_time - start_of_day > 30000:
			day += 1
			start_of_day = current_time
			budget += 150 + (50 * saved_kids)
			if water_needs[0] or food_needs[0]:
				game_on = False
				win = False

			elif day > 5:
				game_on = False
				win = True

		if water_investments >= water_needs[0] and water_needs[0]:
			water_investments -= water_needs[0]
			water_needs = [0, ""]
			saved_kids += 1

		if food_investments >= food_needs[0] and food_needs[0]:
			food_investments -= food_needs[0]
			food_needs = [0, ""]
			saved_kids += 1

	#######ANIMATION#######

	if game_on:

		screen.blit(BACKGROUND, (0, 0))
		screen.blit(UNICEF, ((WIDTH - UNICEF.get_width())/2, 50))

		write_text_with_back(("Budget: $"+str(budget), FONT, BLACK), (10, LIGHT_BLUE), (0, 0))
		write_text_with_back(("Day: "+str(day), FONT, BLACK), (10, LIGHT_BLUE), (250, 0))
		write_text_with_back(("Time: "+str(int((current_time - start_of_day)/1000))+" s", FONT, BLACK), (10, LIGHT_BLUE), (500, 0))
		write_text_with_back(("Kids saved: "+str(saved_kids), FONT, BLACK), (10, LIGHT_BLUE), (750, 0))

		write_text_with_back(("Water spendings: "+str(water_investments)+" $"+water_needs[1], FONT, BLACK), (10, LIGHT_BLUE), (200, 350))
		place_plus((180, 360))
		place_minus((180, 390))

		write_text_with_back(("Food spendings: "+str(food_investments)+" $"+food_needs[1], FONT, BLACK), (10, LIGHT_BLUE), (200, 225))
		place_plus((180, 235))
		place_minus((180, 265))

		pygame.display.update()

	else:
		if win:
			screen.blit(BACKGROUND, (0, 0))
			screen.blit(UNICEF, ((WIDTH - UNICEF.get_width())/2, 50))
			write_text_with_back(("Game Over! Kids saved: "+str(saved_kids), FONT, BLACK), (10, LIGHT_BLUE), (0, 0))
			pygame.display.update()

		else:
			screen.blit(BACKGROUND, (0, 0))
			screen.blit(UNICEF, ((WIDTH - UNICEF.get_width())/2, 50))
			write_text_with_back(("Game Over! You let a kid die!", FONT, BLACK), (10, LIGHT_BLUE), (0, 0))
			pygame.display.update()

	clock.tick(100/fps)

def click():

	global food_investments, water_investments, budget

	if circle_col(mouse.pos, 15, (180, 235)) and budget >= 10:
		food_investments += 10
		budget -= 10
	if circle_col(mouse.pos, 15, (180, 265)) and food_investments >= 10:
		food_investments -= 10
		budget += 10
	if circle_col(mouse.pos, 15, (180, 360)) and budget >= 10:
		water_investments += 10
		budget -= 10
	if circle_col(mouse.pos, 15, (180, 390)) and water_investments >= 10:
		water_investments -= 10
		budget += 10

while True:

	for event in pygame.event.get():

		#quits the game
		if event.type == pygame.QUIT:
			pygame.quit()
			break

		#Keeps track of the keyboard
		if event.type == pygame.KEYDOWN:
			keyboard[event.key] = True

		if event.type == pygame.KEYUP:
			keyboard[event.key] = False

		#Keeps track of mouse
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse.down = True
			click()

		if event.type == pygame.MOUSEBUTTONUP:
			mouse.down = False

		if event.type == pygame.MOUSEMOTION:
			mouse.pos = event.pos

	draw_image()
	current_time = pygame.time.get_ticks()