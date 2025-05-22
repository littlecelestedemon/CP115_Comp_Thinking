import pygame
import time
import random

# establishing color with pygame
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

red = pygame.Color(244, 113, 116)
blue = pygame.Color(147, 202, 237)
green = pygame.Color(172, 209, 175)

# frames per second with pygame and also time
fps = pygame.time.Clock()

# creating a display "game" window
game_window = pygame.display.set_mode((500, 500))

# theoretically drawing a rectangle
pygame.draw.rect(game_window, blue, pygame.Rect(100, 200, 100, 100))
