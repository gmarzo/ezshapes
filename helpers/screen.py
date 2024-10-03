import pygame

pygame.init()

class Screen:
  def __init__(self, height, width, name="Flying A UFO!"):
    self.height = height
    self.width = width
    self.display = pygame.display.set_mode((self.width, self.height))
    pygame.display.set_caption(name)
  
  def __get_screen__(self):
    return self.display

  def get_width(self):
    return self.width

  def get_height(self):
    return self.height
