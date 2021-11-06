import mandelbrot
from decimal import Decimal
from datetime import datetime
import nprender
import render
import os
import platform

_system = ""

def init():
  _system = platform.system()
  if (_system == 'Darwin' or _system == 'Linux'):
    os.system('resize -s 41 80')

  elif (_system == 'Windows'):
    os.system('$host.UI.RawUI.WindowSize.Width = 80')
    os.system('$host.UI.RawUI.WindowSize.Height = 41')
    

init()

resolution = 80
cx = Decimal(0)
cy = Decimal(0)
scale = Decimal(0.5)
mandelbrot_set = mandelbrot.Mandelbrot(resolution=resolution, center=(cx, cy), scale=scale, max_iterations=80)
threshold = 2
max_iterations = 80

def render_terminal(mandelbrot_set, resolution):
  for y in range(resolution):
    s = ""
    for x in range(resolution):
      c = mandelbrot_set.get_point_value(x, y)
      if (c > 0.9):
        s += "#"
      else:
        s += "."
    if (y % 2 == 0):
      print(s)

render_terminal(mandelbrot_set, resolution)

while (True):
  query = input().split()
  if (len(query) == 0):
    continue
  command = query[0]
  if (len(query) == 1):
    if (command == "q"):
        exit(0)

    delta = Decimal(0.25) / scale
    if (command == "+"):
      if (scale <= 1):
        scale *= Decimal(2)
      else:
        scale **= Decimal(1.2)

      delta = Decimal(0.25) / scale

    elif (command == "-"):
      if (scale <= 2):
        scale *= Decimal(0.5)
      else:
        scale **= Decimal(1 / 1.2)
    elif (command == "a"):
      cx -= delta
    elif (command == "d"):
      cx += delta
    elif (command == "w"):
      cy -= delta
    elif (command == "s"):
      cy += delta

  else:
    value = Decimal(query[1])
    if (command == "s"):
      scale = value
    elif (command == "th"):
      threshold = value
    elif (command == "it"):
      max_iterations = int(value)
    elif (command == "a"):
      cx -= value
    elif (command == "d"):
      cx += value
    elif (command == "w"):
      cy += value
    elif (command == "s"):
      cy -= value
    elif (command == "render"):
      filename = datetime.today().strftime('%Y%m%d%H%M%S')
      nprender.render(resolution=int(value), center_x=float(cx), center_y=float(cy), scale=float(scale), threshold=float(threshold), max_iterations=max_iterations, filename=filename, print_time=True)

    elif (command == "q"):
      break
  
  mandelbrot_set = mandelbrot.Mandelbrot(resolution=resolution, center=(cx, cy), scale=scale, max_iterations=80)
  render_terminal(mandelbrot_set, resolution)
  print(f"scale: {scale} | ({cx}, {cy})")