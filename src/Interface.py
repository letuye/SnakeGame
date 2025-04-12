import pygame

from screen.GameOver import GameOver
from screen.MainMenu import MainMenu
from screen.OptionsScreen import OptionsScreen
from screen.PlayScreen import PlayScreen
from utils import load_image


class Interface:
	def __init__(self):
		pygame.init()
		
		pygame.display.set_icon(load_image("icon1.png"))
		self.screen = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
		self.width, self.height = self.screen.get_size()
		
		pygame.display.set_caption("Snake Game")
		self.clock = pygame.time.Clock()
		self.running = True
		self.current_screen = MainMenu(self)

		self.screens = {
			"Play" : PlayScreen(self),
			"Play_Again" : PlayScreen(self),
			"Options" : OptionsScreen(self),
			"GameOver" : GameOver(self, 100),
			"Back_to_menu" : MainMenu(self)
		}

	def change_screen(self, new_screen):
		if new_screen in self.screens:
			self.current_screen = self.screens[new_screen]
		else:
			print(f"Screen {new_screen} không tìm thấythấy")
		
	def run(self):
		while self.running:
			
			self.current_screen.draw()
			action = self.current_screen.handle_events()

			if action == "Quit":
				self.running = False
			elif action in self.screens:
				self.change_screen(action)
		
			pygame.display.flip()  # Cập nhật màn hình
			self.clock.tick(60)  # Giới hạn FPS --> toc do tro choi
		pygame.quit()

if __name__ == "__main__":
	game = Interface()
	game.run()