import pygame, random, time, sys
from utils import load_font, load_image_size
class Snake:
    def __init__(self, screen, food, grid_size ):
        self.screen = screen
        self.food = food
        self.grid_size = grid_size
        self.score = 0
        self.reset()
        self.load_images()
        self.black = pygame.Color(0, 0, 0)
        self.eat_sound = pygame.mixer.Sound("assets\sounds\eat.wav")
        self.death_sound = pygame.mixer.Sound("assets\sounds\death.wav")
        

    def load_images(self):
        self.head_imgs = {
            "UP": load_image_size("head_up.png"),
            "DOWN": load_image_size("head_down.png"),
            "LEFT": load_image_size("head_left.png"),
            "RIGHT": load_image_size("head_right.png")
        }

        self.tail_imgs = {
            "UP": load_image_size("tail_up.png"),
            "DOWN": load_image_size("tail_down.png"),
            "LEFT": load_image_size("tail_left.png"),
            "RIGHT": load_image_size("tail_right.png")
        }

        self.body_straight = {
            "VERTICAL": load_image_size("body_vertical.png"),
            "HORIZONTAL": load_image_size("body_horizontal.png")
        }

        self.body_turn = {
            ("UP", "LEFT"): load_image_size("body_bottomleft.png"),
            ("LEFT", "UP"): load_image_size("body_topright.png"),
            ("UP", "RIGHT"): load_image_size("body_bottomright.png"),
            ("RIGHT", "UP"): load_image_size("body_topleft.png"),
            ("DOWN", "LEFT"): load_image_size("body_topleft.png"),
            ("LEFT", "DOWN"): load_image_size("body_bottomright.png"),
            ("DOWN", "RIGHT"): load_image_size("body_topright.png"),
            ("RIGHT", "DOWN"): load_image_size("body_bottomleft.png")
        }

    def spawn_food_not_on_snake(self):
                while True:
                    self.food.spawn()
                    if list(self.food.rect.topleft) not in self.snakebody:
                        break

    def reset(self):
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.changeto = self.direction
        self.score = 0

        self.screen_width, self.screen_height = self.screen.get_size()
        grid_x = self.screen_width // self.grid_size
        grid_y = self.screen_height // self.grid_size

        #Chọn vị trí ngẫu nhiên ở vùng giữa màn hình (1/3 giữa)
        start_x = random.randint(grid_x // 3, (2 * grid_x) // 3) *self.grid_size
        start_y = random.randint(grid_y // 3, (2 * grid_y) // 3) *self.grid_size
        self.snake_pos = [start_x, start_y]

        #Tạo thân ban đầu dựa trên hướng
        self.snakebody = [list(self.snake_pos)]
        if self.direction == "RIGHT":
            self.snakebody.append([start_x - self.grid_size, start_y])
            self.snakebody.append([start_x - 2*self.grid_size, start_y])
        elif self.direction == "LEFT":
            self.snakebody.append([start_x + self.grid_size, start_y])
            self.snakebody.append([start_x + 2*self.grid_size, start_y])
        elif self.direction == "UP":
            self.snakebody.append([start_x, start_y + self.grid_size])
            self.snakebody.append([start_x, start_y + 2*self.grid_size])
        elif self.direction == "DOWN":
            self.snakebody.append([start_x, start_y - self.grid_size])
            self.snakebody.append([start_x, start_y - 2*self.grid_size])

    def get_direction(self, p1, p2):
        if p1[0] == p2[0]:
            return "UP" if p1[1] > p2[1] else "DOWN"
        elif p1[1] == p2[1]:
            return "LEFT" if p1[0] > p2[0] else "RIGHT"
        return None  

    def handle_events(self, event):
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != "DOWN":
                        self.changeto = "UP"
                    elif event.key == pygame.K_DOWN and self.direction != "UP":
                        self.changeto = "DOWN"
                    elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                        self.changeto = "LEFT"
                    elif event.key == pygame.K_RIGHT and self.direction != "LEFT":
                        self.changeto = "RIGHT"

    def update(self):
        self.direction = self.changeto

        if self.direction == "UP":
                self.snake_pos[1] -= self.grid_size
        elif self.direction == "DOWN":
            self.snake_pos[1] += self.grid_size
        elif self.direction == "LEFT":
            self.snake_pos[0] -= self.grid_size
        elif self.direction == "RIGHT":
            self.snake_pos[0] += self.grid_size

        self.snakebody.insert(0, list(self.snake_pos))

        # Kiểm tra rắn ăn mồi
        if self.snake_pos == list(self.food.rect.topleft):
            self.eat_sound.play()
            self.score += self.food.score
            self.spawn_food_not_on_snake()
        else:
            self.snakebody.pop()   

    def draw_snake(self):
        for i in range(1, len(self.snakebody) - 1):
            prev = self.snakebody[i + 1]
            curr = self.snakebody[i]
            nxt = self.snakebody[i - 1]
            dir1 = self.get_direction(prev, curr)
            dir2 = self.get_direction(curr, nxt)

            if dir1 == dir2:
                if dir1 in ("UP", "DOWN"):
                    self.screen.blit(self.body_straight["VERTICAL"], pygame.Rect(curr[0], curr[1], self.grid_size, self.grid_size))
                else:
                    self.screen.blit(self.body_straight["HORIZONTAL"], pygame.Rect(curr[0], curr[1], self.grid_size, self.grid_size))
            else:
                self.screen.blit(self.body_turn[(dir1, dir2)], pygame.Rect(curr[0], curr[1], self.grid_size, self.grid_size))

        head_dir = self.get_direction(self.snakebody[1], self.snakebody[0])
        self.screen.blit(self.head_imgs[head_dir], pygame.Rect(self.snakebody[0][0], self.snakebody[0][1], self.grid_size, self.grid_size))

        tail_dir = self.get_direction(self.snakebody[-2], self.snakebody[-1])
        self.screen.blit(self.tail_imgs[tail_dir], pygame.Rect(self.snakebody[-1][0], self.snakebody[-1][1], self.grid_size, self.grid_size))
    
    def check_game_over(self):
            x, y = self.snake_pos
            if x < 0 or x >= self.screen.get_width() or y < 0 or y >= self.screen.get_height() or self.snake_pos in self.snakebody[1:]:
                self.death_sound.play()      
                return True
            return False
    
    def show_score(self):
        font = load_font("Dinosaur.ttf",20)
        score_screen = font.render(f'Score: {self.score}', True, self.black)
        self.screen.blit(score_screen, (10,10))
    
    def get_speed_by_level(self):
        if self.score < 100:
            return 10
        elif self.score < 300:
            return 15
        elif self.score < 600:
            return 20
        else:
            return 25
        
    def render(self):
        self.draw_snake()
        self.food.draw(self.screen)
        self.show_score()
        pygame.display.flip()