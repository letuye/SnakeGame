import pygame
import os

CYAN = (51, 255, 255)
CYAN_HOVER = (0, 204, 204)

ASSET_DIR = "assets"
SOUND_DIR = os.path.join(ASSET_DIR, "sounds")
FONT_DIR = os.path.join(ASSET_DIR, "fonts")
IMAGE_DIR = os.path.join(ASSET_DIR, "images")

def load_image(filename):
    path = os.path.join(IMAGE_DIR, filename)
    return pygame.image.load(path)

def load_image_size(filename):
    path = os.path.join(IMAGE_DIR, filename)
    return pygame.transform.scale(pygame.image.load(path), (20,20))  

def load_font(filename, size):
    path = os.path.join(FONT_DIR, filename)
    return pygame.font.Font(path, size)

def draw_button(screen, text, center_x, center_y, width, height, font_size=30, color = CYAN, hover_color = CYAN_HOVER):
    mouse_x, mouse_y = pygame.mouse.get_pos() 
    x = center_x - width // 2
    y = center_y - height // 2
    
    button_rect = pygame.Rect(x, y, width, height) 
    font = load_font("Dinosaur.ttf", font_size)
    if button_rect.collidepoint(mouse_x, mouse_y): 
        pygame.draw.rect(screen, hover_color, button_rect,3, 10)
        text_surface = font.render(text, True, hover_color)
    else:
        pygame.draw.rect(screen, color, button_rect,3,10)
        text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)
    return button_rect


