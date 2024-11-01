from src.ezshapes.renderer import *

setup(700, 500)

ufox = 350
ufoy = 200
speed = 5

while True:

  set_background("skyblue")

  # Draw the ground
  rect(0, 300, get_screen_width(), 200, "lightgreen")

  # Test Beam
  triangle(ufox, ufoy, ufox-30, 300, ufox+30, 300, "yellow")

  # Draw the UFO pieces
  ellipse(ufox, ufoy, 80, 40, "grey50")
  ellipse(ufox, ufoy-10, 40, 30, "lightblue")

  #Draw the sun
  circle(get_screen_width(), 0, 75, "yellow", 1, "orange")

  #Singular sun ray
  line(get_screen_width() - 60, 60, get_screen_width() - 100, 100)

  # Have the ufo bounce on hitting a wall
  if ufox > get_screen_width() or ufox < 0:
    speed *= -1
  
  if key_pressed("UP"):
    ufoy -= 3
  if key_pressed("down"):
    ufoy += 3
  
  ufox += speed

  update_screen()
