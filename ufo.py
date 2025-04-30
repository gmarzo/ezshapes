from src.ezshapes.renderer import *

setup(700, 500)

ufox = 350
ufoy = 200
speed = 5

nighttime = False

while True:

  if not nighttime:
    set_background("skyblue")
  else:
    set_background("indigo")

  # Draw the ground
  rect(0, 300, get_screen_width(), get_screen_height()-200, "lightgreen", 2, "darkgreen")

  # Test Beam
  triangle(ufox, ufoy, ufox-30, get_screen_height()-200, ufox+30, get_screen_height()-200, "yellow", 1, "orange")

  # Draw the UFO pieces
  ellipse(ufox, ufoy, 80, 40, "grey50", 1, "black")
  ellipse(ufox, ufoy-10, 40, 30, "lightblue", 1, "black")

  #Draw the sun
  circle(get_screen_width(), 0, 75, "yellow", 2, "oragne")

  #Singular sun ray
  # line(get_screen_width() - 60, 60, get_screen_width() - 100, 100)

  # Have the ufo bounce on hitting a wall
  if ufox > get_screen_width() or ufox < 0:
    speed *= -1
  
  if key_pressed("UP"):
    ufoy -= 10
  if key_pressed("down"):
    ufoy += 10
  
  if key_pressed("space"):
    nighttime = not nighttime

  ufox += speed

  update_screen()
