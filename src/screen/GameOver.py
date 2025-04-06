import pygame
from utils import draw_button, load_font, load_image

class GameOver:
	def __init__(self, interface, score, high_score):
		self.interface = interface
		self.screen = interface.screen
		self.width, self.height = self.screen.get_size()
		self.score = score
		self.high_score = high_score
		self.fontG = load_font("jabjai_heavy.TTF", 100)
		self.font = load_font("Dinosaur.ttf", 40)
		self.background = load_image("bg.png")

	def draw(self):
		#self.screen.fill((37, 43, 141))
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.screen.blit(self.background, (0,0))

		text = self.fontG.render("GAME OVER", True, ("#00e6b8"))
		text_rect = text.get_rect(center = (self.width // 2 , self.height // 2 - 220))
		self.screen.blit(text, text_rect)

		#hien thi diem so
		score_txt = self.font.render(f"Socre: {self.score}", True, ("#27E7C9"))
		self.screen.blit(score_txt, (self.width // 2 - score_txt.get_width() // 2, self.height // 2 - 150))

		#hien thi diem so cao nhat
		high_score_txt = self.font.render(f"High Score: {self.high_score}", True, ("#27E7C9"))
		self.screen.blit(high_score_txt, (self.width // 2 - high_score_txt.get_width() // 2 , self.height // 2 - 100))

		self.play_again_button = draw_button(self.screen, "Play Again", self.width //2, self.height //2 , 200, 50, 30, "#27E7C9","#22bda5")
		self.back_button = draw_button(self.screen, "Back", self.width //2, self.height //2 +100 , 200, 50, 30, "#27E7C9","#22bda5")
		self.quit_button = draw_button(self.screen, "Quit", self.width //2, self.height //2 +200, 200, 50, 30, "#27E7C9","#22bda5")
		
		
	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.interface.running = False

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				mouse_pos = pygame.mouse.get_pos()
				if self.play_again_button.collidepoint(mouse_pos):
					return "Play_Again"	
				if self.quit_button.collidepoint(mouse_pos):
					return "Quit"
				if self.back_button.collidepoint(mouse_pos):
					return "Back_to_menu"
		return None