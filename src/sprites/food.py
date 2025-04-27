import pygame
import random
from utils import load_image

# Danh sách các loại mồi với điểm và ảnh tương ứng
FOODS = {
    'grape': {'image': 'grape.png', 'score': 5},
    'apple': {'image': 'apple.png', 'score': 10},
    'banana': {'image': 'banana.png', 'score': 15},
    'cherry': {'image': 'cherry.png', 'score': 20}
}

class Food(pygame.sprite.Sprite):
    def __init__(self, grid_size, screen_width, screen_height):
        super().__init__()
        self.grid_size = grid_size
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.type = None
        self.image = None
        self.rect = None
        self.score = 0
        self.spawn()

    def spawn(self):
        # Chọn ngẫu nhiên loại mồi
        self.type = random.choice(list(FOODS.keys()))
        food_info = FOODS[self.type]

        # Load ảnh tương ứng
        self.image = load_image(food_info['image']).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.grid_size, self.grid_size))
        self.rect = self.image.get_rect()

        # Tạo vị trí ngẫu nhiên (theo lưới)
        grid_x = self.screen_width // self.grid_size
        grid_y = self.screen_height // self.grid_size
        self.rect.topleft = (
            random.randint(0, grid_x - 1) * self.grid_size,
            random.randint(0, grid_y - 1) * self.grid_size
        )

        # Lưu điểm số
        self.score = food_info['score']

    def draw(self, screen):
        self.screen_width, self.screen_height = screen.get_size()
        screen.blit(self.image, self.rect)


             
		
        


	    
