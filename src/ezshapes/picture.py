import pygame, os

pygame.init()

class Picture():
  def __init__(self, path:str=".", x=0, y=0):
    self.path = path
    try:
      self.surface = pygame.image.load(path)
    except:
      print(f"File at path: \"{self.path}\" could not be found, check relative path.")
    self.x = x
    self.y = y

  def rescale(self, factor:float):
    self.surface = pygame.transform.scale_by(self.surface, factor)
  
  def set_scale(self, width, height):
    self.surface = pygame.transform.scale(self.surface, (width, height))