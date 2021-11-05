from decimal import Decimal
from complex import Complex
import math 

class Mandelbrot:
  resolution = 640
  center = (Decimal(-0.75), Decimal(0.25))
  scale = 3
  threshold = Decimal(2)
  max_iterations = 255

  def __init__(self, resolution=640, center=(Decimal(-0.75), Decimal(0.25)), 
               scale=Decimal(3), threshold=Decimal(2), max_iterations=255):
    self.resolution = resolution
    self.center = center
    self.scale = scale
    self.threshold = threshold
    self.max_iterations = max_iterations

  def convert_position(self, x, y):
    x = Decimal(x)
    y = Decimal(y)

    cx, cy = self.center

    x -= self.resolution // 2
    y -= self.resolution // 2

    x /= Decimal(self.resolution * self.scale)
    y /= Decimal(self.resolution * self.scale)
    
    x = cx + x
    y = cy + y

    return x, y

  def get_point_value(self, x, y):
    x, y = self.convert_position(x, y)

    if math.sqrt((x - Decimal(0.25)) ** 2 + y ** 2) <= 1/2 - 1/2 * math.cos(math.atan2(y, x - Decimal(0.25))):
      return 1

    c = Complex(x, y)
    z = Complex(Decimal(0), Decimal(0))

    it = 0
    while it < self.max_iterations:
      z = (z * z) + c
      if (abs(z) > self.threshold):
        break
      it += 1
    return it / self.max_iterations

