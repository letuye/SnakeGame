import pygame
from utils import draw_button, load_font

class GameOver:
	def __init__(self, interface, score):
		self.interface = interface
		self.screen = interface.screen
		self.width, self.height = self.screen.get_size()
		self.score = score
		self.font = load_font("Dinosaur.ttf", 40)

	def draw(self):
		self.screen.fill((37, 43, 141))
		self.play_again_button = draw_button(self.screen, "Play Again", self.width //2, self.height //2 , 200, 50, 30, "#27E7C9","#22bda5")
		self.quit_button = draw_button(self.screen, "Quit", self.width //2, self.height //2 +150, 200, 50, 30, "#27E7C9","#22bda5")
		#hien thi diem so
		score_txt = self.font.render(f"Socre: {self.score}", True, ("#27E7C9"))
		self.screen.blit(score_txt, (self.width // 2 - score_txt.get_width() // 2, self.height // 2 - 100))

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				mouse_pos = pygame.mouse.get_pos()
				if self.play_again_button.collidepoint(mouse_pos):
					return "Play_Again"	
				if self.quit_button.collidepoint(mouse_pos):
					return "Quit"
		return None