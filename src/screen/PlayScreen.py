import pygame, time

from sprites.food import Food
from utils import load_image
from sprites.snake import Snake
class PlayScreen:
    def __init__(self, interface):
        self.interface = interface
        self.screen = interface.screen
        self.width, self.height = self.screen.get_size()
        self.background = load_image("bggrass.png")
        self.grid_size = 20
        self.food = Food(grid_size=self.grid_size, screen_width = self.width, screen_height = self.height)
        self.snake = Snake(self.screen,self.food,self.grid_size)
		
    def draw(self):
        self.width, self.height = self.screen.get_size()
        scaled_bg = pygame.transform.scale(self.background, (self.width, self.height))
        self.screen.blit(scaled_bg, (0, 0))

        self.snake.render()

    def handle_events(self):      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.interface.running = False
            self.snake.handle_events(event)
        return None
    
    def update(self):
        self.snake.update()
        if self.snake.check_game_over():
            score = self.snake.score
            self.interface.change_screen("GameOver", score)
