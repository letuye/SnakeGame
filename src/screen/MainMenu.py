import pygame
import os
from utils import *
class MainMenu:
	def __init__(self, interface):
		self.interface = interface
		self.screen = interface.screen
		self.width, self.height = self.screen.get_size()
		self.background = load_image("bg.png")

		# Cài đặt âm thanh
		self.sound_on_img = pygame.transform.scale(pygame.image.load("assets/images/sound_on.png"), (60, 60))
		self.sound_off_img = pygame.transform.scale(pygame.image.load("assets/images/sound_off.png"), (60, 60))
		self.sound_button_rect = self.sound_on_img.get_rect()

        # Phát nhạc nền
		try:
			pygame.mixer.music.load("assets/sounds/bg_music.wav")
			pygame.mixer.music.play(-1)
		except pygame.error as e:
			print(f"Không thể tải nhạc nền: {e}")
			self.music_on = False

	def draw(self):
		self.width, self.height = self.screen.get_size()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.screen.blit(self.background, (0,0))

		# Vẽ nút âm thanh ở góc phải trên
		self.sound_button_rect.topright = (self.width - 10, 10)
		icon = self.sound_on_img if self.interface.music_on else self.sound_off_img
		self.screen.blit(icon, self.sound_button_rect)

		#Vẽ tiêu đề game
		self.font = load_font("jabjai_heavy.TTF", self.width //10)
		text = self.font.render("SNAKE", True, ("#00e6b8"))
		text_rect = text.get_rect(center = (self.width *(2/5), self.height // 8))
		self.screen.blit(text, text_rect)

		text1 = self.font.render("GAME", True, ("#00ffcc"))
		text_rect = text1.get_rect(center = (self.width *(3/5), self.height // 5))
		self.screen.blit(text1, text_rect)

		#Các button
		self.play_button = draw_button(self.screen, "Play", self.width //2 , self.height //2 - self.height //12 , self.width //5, self.height //12, self.height //20)
		self.help_button = draw_button(self.screen, "Help", self.width //2, self.height //2 + self.height //12, self.width //5, self.height //12, self.height //20)
		self.quit_button = draw_button(self.screen, "Quit", self.width //2, self.height //2 + self.height //4, self.width //5, self.height //12, self.height //20)


	def toggle_music(self):
		self.interface.music_on = not self.interface.music_on
		if self.interface.music_on:
			self.interface.play_background_music("assets/sounds/bg_music.wav")
		else:
			self.interface.stop_background_music()
		self.interface.music_on = self.interface.bg_music_playing
		
	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.interface.running = False

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				mouse_pos = pygame.mouse.get_pos()
				# Kiểm tra nút âm thanh
				if self.sound_button_rect.collidepoint(mouse_pos):
					print("Click vào nút âm thanh")
					self.toggle_music()
					
				elif self.play_button.collidepoint(mouse_pos):
					return "Play"
				elif self.help_button.collidepoint(mouse_pos):
					return "Help"
				elif self.quit_button.collidepoint(mouse_pos):
					return "Quit"			
		return None
	
	def update(self):
		pass	

		