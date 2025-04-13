import pygame

from sprites.food import Food
from utils import draw_button, load_image

class PlayScreen:
	def __init__(self, interface):
		self.interface = interface
		self.screen = interface.screen
		#self.width, self.height = self.screen.get_size()
		self.background = load_image("bggrass.png")
		self.head = load_image("head_down.png")

		# Tạo mồi ban đầu
		self.food = Food(grid_size=20, screen_width=self.screen.get_width(), screen_height=self.screen.get_height())

	def draw(self):
		self.width, self.height = self.screen.get_size()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.screen.blit(self.background, (0,0))

		#self.back_button = draw_button(self.screen, "Back", self.width //2, self.height //2 , 200, 50, 30, "#27E7C9","#22bda5")
		self.back_button = draw_button(self.screen, "Game Over", self.width //2, self.height //2 , self.width //5, self.height //12, 30, "#27E7C9","#22bda5")

		# ve cac doi tuong tro choi
		self.head = pygame.transform.scale(self.head, (20,20))
		self.screen.blit(self.head, (100,100))
		
		# Vẽ mồi
		self.food.draw(self.screen)
	
	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.interface.running = False

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				mouse_pos = pygame.mouse.get_pos()
				"""if self.back_button.collidepoint(mouse_pos):
					return "Back_to_menu" """
				if self.back_button.collidepoint(mouse_pos):
					return "GameOver"
		return None