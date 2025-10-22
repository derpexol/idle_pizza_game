import pygame
from constants import *

def draw_store(screen, font, buildings_data, get_price):
	store_title = font.render("STORE", True, WHITE)
	title_width = store_title.get_width()
	store_x = SCREEN_WIDTH - title_width - 25
	store_y = 10

	screen.blit(store_title, (store_x, store_y))
	#print(f"DEBUG draw_store: received {len(building_info)} buildings: {list(building_info.keys())}")
	#print(f"DEBUG draw_store: received {len(buildings_data)} buildings: {list(buildings_data.keys())}")
	y_offset = store_y + 40
	for building_name, info in buildings_data.items():
		cost = get_price(building_name)
		display_name = building_name.replace('_', ' ' ).title()
		building_text = font.render(f"{display_name}: {cost} pizzas", True, WHITE)

		text_width = building_text.get_width()
		item_x = SCREEN_WIDTH - text_width - 25

		screen.blit(building_text, (item_x, y_offset))
		y_offset += 30

def draw_pizza_count(screen, font, total_pizzas, building_info, pps):
	display_text = f"Pizzas: {total_pizzas:.2f} | {pps:.2f} pizzas per second"
	number_text = font.render(display_text, True, WHITE)
	screen.blit(number_text, (10, 10))

	y_offset = 50
	for building_name, info in building_info.items():
		if info["quantity"] > 0:
			display_name = building_name.replace('_', ' ').title()
			building_text = font.render(f"{display_name}: {info['quantity']}", True, WHITE)
			screen.blit(building_text, (10, y_offset))
			y_offset += 30
