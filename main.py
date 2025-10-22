import pygame
import time
import os
import sys
import commands
import constants

#from constants import *
from cli import CLI
from commands import *
from saving import save_game, load_game, get_default_building_info
from shop import draw_pizza_count, draw_store

def main():
	pygame.init()

	total_pizzas, loaded_building_info = load_game()
	constants.building_info.update(loaded_building_info)

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption("Number Increment Game")
	clock = pygame.time.Clock()
	font = pygame.font.Font(None, FONT_SIZE)

	cli = CLI()

	#game state
	last_increment_time = time.time()

	#main loop
	while True:
		current_time = time.time()

		#increments number every second
		if current_time - last_increment_time >= 1:
			total_pizzas += 1
			last_increment_time = current_time

		#increment pizza
		delta_time = clock.tick(60) / 1000.0
		for building_name, info in constants.building_info.items():
			if info["quantity"] > 0:
				production_rate = (info["production"] * info["quantity"]) / info["cycle_time"]
				pizzas_this_frame = production_rate * delta_time
				total_pizzas += pizzas_this_frame

		#calculate pps (pizzas per second)
		pps = 0
		for building_name, info in constants.building_info.items():
			if info["quantity"] > 0:
				production_rate = (info["production"] * info["quantity"]) / info["cycle_time"]
				pps += production_rate

		#handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				save_game(total_pizzas, constants.building_info)
				print("Thank you for playing!")
				sys.exit(0)
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					save_game(total_pizzas, constants.building_info)
					print("Thank you for playing!")
					sys.exit(0)

			pizzas_to_add = cli.handle_event(event, total_pizzas) #pass state to cli
			total_pizzas += pizzas_to_add

		#draw everything
		screen.fill(BLACK)

		#draw pizza count and store
		draw_pizza_count(screen, font, total_pizzas, constants.building_info, pps)
		draw_store(screen, font, constants.building_info, get_building_cost)

		#draw cli
		cli.draw(screen)

		pygame.display.flip()
		clock.tick(60)

if __name__ == "__main__":
	main()
