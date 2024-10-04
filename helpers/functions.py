import pygame, re
from .screen import Screen
from .colordict import THECOLORS

pygame.init()

def setup(width:int, height:int, name:str=None):
  """
  Creates the pygame display with the given height and width.
  Can optionally include a name to change the window title.

  Parameters:
    - width (int): The width of the screen in pixels
    - height (int): The height of the screen in pixels
    - name (str): The caption of the window
  
  Returns:
    None
  """
  global display
  global clock
  display = Screen(height, width, name)
  clock = pygame.time.Clock()

def update_screen():
  """
  Updates the pygame screen to draw all objects previously made.

  Should be called noce per frame and after all objects have been drawn.
  """
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
  pygame.display.update()

def set_background(color:str):
  """
  Sets the color of the background if the given color is valid.

  Parameters:
    - color (str): the color to change the background to
  
  Returns:
    None
  """
  display.__get_screen__().fill(__is_valid_color__(color))

def rect(left:int, top:int, width:int, height:int, color:str="grey70"):
  """
  Draws a rectangle on screen, with the top-left corner at a
  given coordinate with the specified width and height.

  Parameters:
    - left (int): The x coordinate of the rectangle's top left corner.
    - top (int): The y coordinate of the rectangle's top left corner.
    - width (int): The width of the rectangle, extending right from the top left corner.
    - height (int): The height of the rectangle, extending down from the top left corner.
    - color (str): The fill color of the rectangle.
  
  Returns:
    None
  """
  pygame.draw.rect(display.__get_screen__(), __is_valid_color__(color), pygame.Rect(left, top, width, height))

def ellipse(centerx, centery, width, height, color="grey70"):
  pygame.draw.ellipse(display.__get_screen__(), __is_valid_color__(color), pygame.Rect(centerx-(width/2), centery-(height/2), width, height))

def circle(centerx, centery, radius, color="grey70"):
  pygame.draw.circle(display.__get_screen__(), __is_valid_color__(color), (centerx, centery), radius)

def triangle(p1x, p1y, p2x, p2y, p3x, p3y, color="grey70"):
  pygame.draw.polygon(display.__get_screen__(), __is_valid_color__(color), [(p1x, p1y),(p2x, p2y),(p3x, p3y)])

def get_screen_width():
  return display.get_width()

def get_screen_height():
  return display.get_height()

def __is_valid_color__(color):
  valid_color = re.compile("^#[0-9|a-f]{6}$")
  match = re.search(valid_color, color)
  if match or color in THECOLORS:
    return color
  else:
    return (70, 70, 70)