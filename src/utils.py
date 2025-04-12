import pygame
import os

# khai báo thư mục chứa tài nguyên assets
ASSET_DIR = "asserts"
SOUND_DIR = os.path.join(ASSET_DIR, "sounds")
FONT_DIR = os.path.join(ASSET_DIR, "fonts")
IMAGE_DIR = os.path.join(ASSET_DIR, "images")

# Hàm tải hình ảnh
def load_image(filename):
    """Load ảnh từ thư mục assets/images"""
    path = os.path.join(IMAGE_DIR, filename)
    return pygame.image.load(path)

# Hàm tải âm thanh
def load_sound(filename):
    """Load âm thanh từ thư mục assets/sounds"""
    path = os.path.join(SOUND_DIR, filename)
    return pygame.mixer.Sound(path)

# Hàm tải font chữ
def load_font(filename, size):
    """Load font từ thư mục assets/fonts"""
    path = os.path.join(FONT_DIR, filename)
    return pygame.font.Font(path, size)

# Hàm vẽ nút bấm với hiệu ứng hover
def draw_button(screen, text, center_x, center_y, width, height, font_size=30, color = (), hover_color = ()):
    mouse_x, mouse_y = pygame.mouse.get_pos() #Lấy vị trí chuột 
    x = center_x - width // 2
    y = center_y - height // 2
    
    button_rect = pygame.Rect(x, y, width, height) 
    font = load_font("Dinosaur.ttf", font_size)
    # Đổi màu khi hover chuột (vẽ nút)
    if button_rect.collidepoint(mouse_x, mouse_y): 
        pygame.draw.rect(screen, hover_color, button_rect,3, 10)
        text_surface = font.render(text, True, "#00cccc")
    else:
        pygame.draw.rect(screen, color, button_rect,3,10)
        text_surface = font.render(text, True, "#33ffff")
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)
    return button_rect


