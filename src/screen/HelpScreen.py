import pygame
import pygame.freetype
from utils import draw_button , load_image

class HelpScreen:
    def __init__(self, interface):
        self.interface = interface
        self.screen = interface.screen
        self.width, self.height = self.screen.get_size()
        # Font có hỗ trợ tiếng Việt
        self.font = pygame.freetype.Font("assets/fonts/OpenSans-VariableFont_wdth,wght.ttf", 20)
        self.small_font = pygame.freetype.Font("assets/fonts/OpenSans-VariableFont_wdth,wght.ttf", 16)

        self.food_info = {
            'Grape': 5,
            'Apple': 10,
            'Banana': 15,
            'Cherry': 20
        }
        self.background = load_image("bg_help.png")

    def draw(self):
        self.width, self.height = self.screen.get_size()
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.screen.blit(self.background, (0,0))
        
        y = 30
        spacing = 28

        # Tiêu đề
        title, rect = self.font.render("Trò chơi Rắn Săn Mồi", (255, 255, 255))
        self.screen.blit(title, (self.width // 2 - rect.width // 2, y))
        y += spacing * 2

        # Giới thiệu
        lines = [
            "Điều khiển con rắn ăn mồi để ghi điểm và tránh va chạm.",
            "Các loại mồi:"
        ]
        for line in lines:
            text, rect = self.small_font.render(line, (255, 255, 255))
            self.screen.blit(text, (80, y))
            y += spacing

        # Mồi + điểm
        for food, score in self.food_info.items():
            color = (200, 255, 200) if score > 0 else (255, 150, 150)
            text = f"- {food.ljust(8)} ({'+' if score > 0 else ''}{score} điểm{' → tránh nếu có thể!' if score < 0 else ''})"
            rendered, rect = self.small_font.render(text, color)
            self.screen.blit(rendered, (100, y))
            y += spacing

        # Hướng dẫn chơi
        y += spacing
        title, _ = self.small_font.render("Hướng dẫn chơi:", (255, 255, 255))
        self.screen.blit(title, (80, y))
        y += spacing

        controls = [
            "- Dùng phím mũi tên để di chuyển rắn.",
            "- Ăn mồi để ghi điểm.",
            "- Tốc độ chơi tăng dần khi điểm số càng cao.",
            "- Tránh va vào tường hoặc chính mình."
        ]
        for line in controls:
            rendered, rect = self.small_font.render(line, (255, 255, 255))
            self.screen.blit(rendered, (100, y))
            y += spacing

        # Nút back
        self.back_button = draw_button(self.screen,"Back",self.width-self.width //7,self.height-self.height //12,self.width //5, self.height //12,font_size=self.height//20)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.interface.running = False
                return "Quit"
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_ESCAPE, pygame.K_BACKSPACE]:
                    return "Back"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.back_button.collidepoint(pygame.mouse.get_pos()):
                    return "Back"
        return None

    def update(self):
        pass