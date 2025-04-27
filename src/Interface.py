import pygame

from screen.GameOver import GameOver
from screen.MainMenu import MainMenu
from screen.HelpScreen import HelpScreen
from screen.PlayScreen import PlayScreen
from utils import load_image

WIDTH, HEIGHT = 800, 500
class Interface:
	def __init__(self):
		pygame.init()
		pygame.display.set_icon(load_image("icon1.png"))
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption("Snake Game")
		self.clock = pygame.time.Clock()
		self.running = True
		self.current_screen = MainMenu(self)

		# Các màn hình khác
		self.screens = {
            "Help" : HelpScreen(self),
            "Back" : MainMenu(self)
        }
	
		# Âm thanh nền
		self.music_on = True
		self.bg_music_playing = True 

	def change_screen(self, new_screen, score = None):
		if new_screen in self.screens:
			self.current_screen = self.screens[new_screen]
		elif new_screen == "Play" or new_screen == "PlayAgain":
			self.current_screen = PlayScreen(self)
		elif new_screen == "GameOver":
			self.current_screen = GameOver(self,score)
		else:
			print(f"Screen {new_screen} không tìm thấy")

		# Thay đổi nhạc nền khi chuyển màn hình
		if self.music_on:
			if isinstance(self.current_screen, PlayScreen):
				self.stop_background_music()
			else:
				self.play_background_music("assets/sounds/bg_music.wav")  
		else:
			self.stop_background_music()
		

	def play_background_music(self, music_file):
		if not self.bg_music_playing:  
			pygame.mixer.music.load(music_file)
			pygame.mixer.music.play(-1)  
			self.bg_music_playing = True
			
	def stop_background_music(self):
		if self.bg_music_playing:
			pygame.mixer.music.stop()
			self.bg_music_playing = False

	def run(self):
		while self.running:
			action = self.current_screen.handle_events()
			self.current_screen.update()
			self.current_screen.draw()
			pygame.display.flip()  
			#Thiết lập tốc độ trò chơi
			if isinstance(self.current_screen, PlayScreen):
				self.clock.tick(self.current_screen.snake.get_speed_by_level())
			else:
				self.clock.tick(60)  

			if action == "Quit":
				self.running = False
			elif action is not None:
				self.change_screen(action)					
		pygame.quit()

