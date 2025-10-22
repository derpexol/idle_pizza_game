import pygame

from constants import *
from commands import execute_command

class CLI:
	def __init__(self):
		self.active = True
		self.input_text = ""
		self.font = pygame.font.Font(CLI_FONT, CLI_FONT_SIZE)
		self.history = []
		self.padding = 10
		self.height = 300

	def handle_event(self, event, current_pizzas):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				#execute the command
				command = self.input_text.strip()
				if command:
					self.history.append(f"> {command}")
					from commands import execute_command
					message, pizzas_to_add = execute_command(command, current_pizzas)
					if message:
						self.history.append(message)
					self.input_text = ""
					return pizzas_to_add
			elif event.key == pygame.K_BACKSPACE:
				self.input_text = self.input_text[:-1]
			else:
				self.input_text += event.unicode
		return 0

	def execute_command(self, command):
		#command parsing
		parts = command.split()
		if not parts:
			return

		cmd = parts[0].lower()
		args = parts[1:]

		#fishy line
		from commands import execute_command
		result = execute_command(cmd, args)

		if result:
			self.history.append(result)

	def draw(self, screen):
		cli_rect = pygame.Rect(
			self.padding,
			SCREEN_HEIGHT - self.height + self.padding,
			SCREEN_WIDTH - (2 * self.padding),
			self.height - (2 * self.padding)
		)
		pygame.draw.rect(screen, (50, 50, 50), cli_rect)
		pygame.draw.rect(screen, WHITE, cli_rect, 2)

		#draw input line
		input_surface = self.font.render(f"> {self.input_text}", True, WHITE)
		screen.blit(input_surface, (cli_rect.x + 5, cli_rect.y + 5))

		#draw command history
		y_offset = cli_rect.y + 35
		for i, line in enumerate(reversed(self.history[-COMMAND_HISTORY_NUM:])): #show last COMMAND_HISTORY_NUM commands
			history_surface = self.font.render(line, True, (150, 150, 150))
			screen.blit(history_surface, (cli_rect.x + 5, y_offset + i * 25))
