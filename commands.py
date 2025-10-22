from constants import *

def validate_args(args, min_args=0, max_args=None):
	if len(args) < min_args:
		return f"Error: Too few arguments. Expected at least {min_args}"
	if max_args is not None and len(args) > max_args:
		return f"Error: Too many arguments. Expected at most {max_args}"
	return None

def execute_command(full_command, current_pizzas):
	parts = full_command.split()
	if not parts:
		return None, 0

	cmd = parts[0].lower()
	args = parts[1:]

	match cmd:
		case "pizza":
			error = validate_args(args, 0, 0)
			if error: return error, 0
			return bake_pizza()
		case "buy":
			error = validate_args(args, 1, 2)
			if error: return error, 0

			if len(args) >= 2 and args[0].isdigit():
				amount = int(args[0])
				building_name = args[1]
			else:
				amount = 1
				building_name = args[0]

			return buy_building(building_name, current_pizzas, amount)
		case _:
			return f"Unknown command: {cmd}", 0

def set_building_info(new_building_info):
	global building_info
	building_info = new_building_info

def get_building_cost(building_name):
	base_cost = building_info[building_name]["cost"]
	current_quantity = building_info[building_name]["quantity"]
	return int((base_cost) * (1.15 ** current_quantity)) #price increases by 15%

def bake_pizza():
	return "Baked one delicious pizza.", 1

def buy_building(building_name, current_pizzas, amount=1):
	if building_name not in building_info:
		return f"Unknown building: {building_name}", 0

	total_cost = 0
	current_quantity = building_info[building_name]["quantity"]

	for i in range(amount):
		cost = int(building_info[building_name]["cost"] * (1.15 ** (current_quantity + i)))
		total_cost += cost

	if current_pizzas < total_cost:
		return f"Not enough pizzas! need {total_cost}.", 0

	for i in range(amount):
		building_info[building_name]["quantity"] += 1

	next_cost = get_building_cost(building_name)
	building_display_name = building_name.replace('_', ' ').title()
	return f"Bought {amount} {building_display_name} for {total_cost} pizzas! (Next cost: {next_cost})", -cost
