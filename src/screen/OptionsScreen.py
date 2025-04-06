import pygame
from utils import draw_button, load_image
class OptionsScreen:
	def __init__(self, interface):
		self.interface = interface
		self.screen = interface.screen
		self.width, self.height = self.screen.get_size()
		self.background = load_image("bg.png")

	def draw(self):
		#self.screen.fill((37, 43, 141))
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.screen.blit(self.background, (0,0))
		self.back_button = draw_button(self.screen, "Back", self.width //2, self.height //2 , 200, 50, 30, "#27E7C9","#22bda5")

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.interface.running = False

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				mouse_pos = pygame.mouse.get_pos()
				if self.back_button.collidepoint(mouse_pos):
					return "Back_to_menu"	
						
		return None