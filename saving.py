import json
from constants import *
import constants
SAVE_FILE = "savefile.json"


def save_game(total_pizzas, building_info):
	print(f"DEBUG save_game: constants.building_info has {len(constants.building_info)} buildings: {list(constants.building_info.keys())}")
	save_data = {
		"total_pizzas": total_pizzas,
		"building_info": constants.building_info
	}

	try:
		with open(SAVE_FILE, 'w') as file:
			json.dump(save_data, file)
		return True
	except Exception as e:
		print(f"Error saving game: {e}")
		return False

def load_game():
	print(f"DEBUG load_game: returning {len(building_info)} buildings: {list(building_info.keys())}")
	try :
		with open(SAVE_FILE, 'r') as file:
			save_data = json.load(file)
			if not save_data or "building_info" not in save_data:
				return 0, get_default_building_info()
			return save_data["total_pizzas"], save_data["building_info"]
	except FileNotFoundError:
		print("No save file found, starting new game")
		return 0, get_default_building_info()
	except Exception as e:
		print(f"Error loading save file: {e}")
		return 0, get_default_building_info()

def get_default_building_info():
	return {
		"italian_chef": {
			"cost": 5,
			"production": 1,
			"cycle_time": 10,
			"quantity": 0
		}
	}
