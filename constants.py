SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36

SAVE_FILE = "game_save.txt"

CLI_FONT = None
CLI_FONT_SIZE = 32
COMMAND_HISTORY_NUM = 10

#buildings
building_info = {
        "italian_chef": {
                "cost": 5,
                "production": 1, #pizzas per cycle
                "cycle_time": 10, #seconds
                "quantity": 0
        },
	"frozen_pizza": {
		"cost": 20,
		"production": 5,
		"cycle_time": 15,
		"quantity": 0
	},
	"pizza_river": {
		"cost": 100,
		"production": 20,
		"cycle_time": 30,
		"quantity": 0
	}
}
