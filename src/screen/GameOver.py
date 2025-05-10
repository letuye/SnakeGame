import pygame
from utils import draw_button, load_font, load_image
import high_score
class GameOver:
	def __init__(self, interface, score):
		self.interface = interface
		self.screen = interface.screen
		self.width, self.height = self.screen.get_size()
		self.score = score
		self.high_score = 0
		self.background = load_image("bg.png")

	def draw(self):
		self.width, self.height = self.screen.get_size()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.screen.blit(self.background, (0,0))

		#Hien thi ten man hinh game overover
		self.fontG = load_font("jabjai_heavy.TTF", self.height // 6)
		text = self.fontG.render("GAME OVER", True, ("#00e6b8"))
		text_rect = text.get_rect(center = (self.width // 2 , self.height // 6))
		self.screen.blit(text, text_rect)

		#hien thi diem so
		self.font = load_font("Dinosaur.ttf", self.height // 15)
		score_txt = self.font.render(f"Score: {self.score}", True, ("#27E7C9"))
		self.screen.blit(score_txt, (self.width // 2 - score_txt.get_width() // 2, self.height // 4))

		#lay diem cao nhat
		high_score_file = "D:/python/SnakeGame/data/high_score.txt"
		self.high_score = high_score.read_highscore(high_score_file)
		if self.score > self.high_score:
			high_score.write_highscore(high_score_file, self.score)
			self.high_score = self.score
		#hien thi diem so cao nhat
		high_score_txt = self.font.render(f"High Score: {self.high_score}", True, ("#27E7C9"))
		self.screen.blit(high_score_txt, (self.width // 2 - high_score_txt.get_width() // 2 , self.height // 3))

		#Ve cac button
		self.play_again_button = draw_button(self.screen, "Play Again", self.width //2, self.height //2 , self.width //5, self.height //12, self.height //20)
		self.back_button = draw_button(self.screen, "Home", self.width //2, self.height //2 + self.height //6 , self.width //5, self.height //12, self.height //20)
		self.quit_button = draw_button(self.screen, "Quit", self.width //2, self.height //2 + self.height //3, self.width //5, self.height //12, self.height //20)
		
		
	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.interface.running = False
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				mouse_pos = pygame.mouse.get_pos()
				if self.play_again_button.collidepoint(mouse_pos):
					return "PlayAgain"	
				if self.quit_button.collidepoint(mouse_pos):
					return "Quit"
				if self.back_button.collidepoint(mouse_pos):
					return "Back"
		return None
	
	def update(self):
		pass	