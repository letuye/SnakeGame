import pygame
from utils import load_image
import random

class Food:
	def __init__(self, interface):
		self.interface = interface
		self.interface = interface.board
		self.screen = interface.screen
		self.foods = [
			load_image("apple.png"),
			load_image("banana.png"),
			load_image("grape.png"),
			load_image("cherry.png")
		]
		self.position = None
		self.food = None

		self.generate_food()

	def generate_food(self):
		#chon moi ngau nhien trong foods va vi tri ngau nhien tren board
		self.food = random.choice(self.foods)
		self.position = self.position.generate_random_position()
		self.board[self.position].value = self.food


	def draw(self):
		#ve food len man hinh tai vi tri hien tai
		if self.position is not None:
			x, y = self.position
			self.screen.blit(self.food, (x*self.board.cell_size, y*self.board.cell_size))
			#cell_size: kich thuoc cua 1 o

	def update(self):
		#cap nhat vi tri va hinh anh food
		self.board[self.position].value = None #xoa vi tri cu
		self.generate_food() # tao vi tri moi