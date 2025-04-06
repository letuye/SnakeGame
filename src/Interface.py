import pygame

from screen.GameOver import GameOver
from screen.MainMenu import MainMenu
from screen.OptionsScreen import OptionsScreen
from screen.PlayScreen import PlayScreen



class Interface:
	def __init__(self):
		pygame.init()
		
		self.screen = pygame.display.set_mode((1000, 600))
		pygame.display.set_caption("Snake Game")
		self.clock = pygame.time.Clock()
		self.running = True
		self.current_screen = MainMenu(self)

	def change_screen(self, new_screen):
		if new_screen == "Play":
			self.current_screen = PlayScreen(self)
		elif new_screen == "Options":
			self.current_screen = OptionsScreen(self)
		elif new_screen == "GameOver":
			self.current_screen = GameOver(self,0,0)
		elif new_screen == "Back_to_menu":
			self.current_screen = MainMenu(self)

	def run(self):
		while self.running:
			self.current_screen.draw()
			action = self.current_screen.handle_events()

			if action == "Play":
				self.change_screen("Play")
			elif action == "Options":
				self.change_screen("Options")
			elif action == "Quit":
				self.running = False
			elif action == "Back_to_menu":
				self.change_screen("Back_to_menu")
			elif action == "Play_Again":
				self.change_screen("Play")
			elif action == "GameOver":
				self.change_screen("GameOver")
		
			pygame.display.flip()  # Cập nhật màn hình
			self.clock.tick(60)  # Giới hạn FPS
		pygame.quit()

if __name__ == "__main__":
	game = Interface()
	game.run()