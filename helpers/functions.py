import pygame
from .screen import Screen

pygame.init()

def setup(width, height):
  global display
  global clock
  display = Screen(height, width)
  clock = pygame.time.Clock()

def update_screen():
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
  pygame.display.update()

def set_background(color):
  display.__get_screen__().fill(color)

def rect(left, top, width, height, color=(70,70,70)):
  pygame.draw.rect(display.__get_screen__(), color, pygame.Rect(left, top, width, height))

def ellipse(x, y, width, height, color=(70,70,70)):
  pygame.draw.ellipse(display.__get_screen__(), color, pygame.Rect(x-(width/2), y-(height/2), width, height))

def circle(x, y, radius, color=(70,70,70)):
  pygame.draw.circle(display.__get_screen__(), color, (x, y), radius)

def triangle(p1x, p1y, p2x, p2y, p3x, p3y, color=(70,70,70)):
  pygame.draw.polygon(display.__get_screen__(), color, [(p1x, p1y),(p2x, p2y),(p3x, p3y)])

def get_screen_width():
  return display.get_width()

def get_screen_height():
  return display.get_height()