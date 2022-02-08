import mandelbrot
import time
from PIL import Image, ImageDraw

class Render:
  def __init__(self, _progress_function, _process_image):
    self._progress_function = _progress_function
    self._process_image = _process_image
      
  def render(self, resolution, center_x, center_y, 
            scale, threshold, max_iterations, 
            filename, framework, print_time=True):

    image = Image.new("RGBA", (resolution, resolution), (0,0,0))
    draw = ImageDraw.Draw(image)

    mandelbrot_set = mandelbrot.Mandelbrot(resolution, (center_x, center_y), scale, threshold, max_iterations)
    
    for x in range(resolution):
      self._progress_function(x, resolution)
      for y in range(resolution):
        value = mandelbrot_set.get_point_value(x, y)
        draw.point((x, y), (int(value * 255), int(value * 255), int(value * 255)))
    
    self._process_image(image)