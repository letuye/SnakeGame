import pygame
from utils import draw_button, load_font, load_image
class MainMenu:
	def __init__(self, interface):
		self.interface = interface
		self.screen = interface.screen
		#self.width, self.height = self.screen.get_size()
		#self.font = load_font("jabjai_heavy.TTF", 100)
		self.background = load_image("bg.png")
		
	def draw(self):
		self.width, self.height = self.screen.get_size()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.screen.blit(self.background, (0,0))
		
		self.play_button = draw_button(self.screen, "Play", self.width //2 , self.height //2 - self.height //12 , self.width //5, self.height //12, self.height //20,"#33ffff","#00cccc")
		self.options_button = draw_button(self.screen, "Options", self.width //2, self.height //2 + self.height //12, self.width //5, self.height //12, self.height //20,"#33ffff","#00cccc")
		self.quit_button = draw_button(self.screen, "Quit", self.width //2, self.height //2 + self.height //4, self.width //5, self.height //12, self.height //20,"#33ffff","#00cccc")

		self.font = load_font("jabjai_heavy.TTF", self.width //10)

		text = self.font.render("SNAKE", True, ("#00e6b8"))
		text_rect = text.get_rect(center = (self.width *(2/5), self.height // 8))
		self.screen.blit(text, text_rect)

		text1 = self.font.render("GAME", True, ("#00ffcc"))
		text_rect = text1.get_rect(center = (self.width *(3/5), self.height // 5))
		self.screen.blit(text1, text_rect)

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.interface.running = False
				
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				mouse_pos = pygame.mouse.get_pos()
				if self.play_button.collidepoint(mouse_pos):
					return "Play"
				elif self.options_button.collidepoint(mouse_pos):
					return "Options"
				elif self.quit_button.collidepoint(mouse_pos):
					return "Quit"
				
		return None
	
	

		