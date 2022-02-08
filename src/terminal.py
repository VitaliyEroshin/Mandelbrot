import mandelbrot
from decimal import Decimal
import output

def output(mandelbrot_set, resolution, ratio):
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

def render(configuration, io):
  resolution = int(io._terminal_width)
  center_x = Decimal(configuration['center_x'])
  center_y = Decimal(configuration['center_y'])
  scale = Decimal(configuration['scale'])
  threshold = Decimal(configuration['threshold'])
  max_iterations = int(configuration['max_iterations'])

  mandelbrot_set = mandelbrot.Mandelbrot(resolution=resolution, center=(center_x, center_y), scale=scale)
  output(mandelbrot_set, io._terminal_width, io._terminal_width // io._terminal_height)