import mandelbrot
import time
from decimal import Decimal
from PIL import Image, ImageDraw

def render(resolution=640, center_x=-0.75, center_y=0.25, 
           scale=3, threshold=2, max_iterations=255, 
           filename="", print_time=True):
  
  center = (Decimal(center_x), Decimal(center_y))
  scale = Decimal(scale)
  threshold = Decimal(threshold)

  image = Image.new("RGBA", (resolution, resolution), (0,0,0))
  draw = ImageDraw.Draw(image)

  timer_start = time.time()
  mandelbrot_set = mandelbrot.Mandelbrot(resolution, center, scale, threshold, max_iterations)
  print("rendering...")

  TERMINAL_WIDTH = 78
  for x in range(resolution):
    # output progress
    print('\033[F' * 2)
    progress = int((x / (resolution-1)) * (TERMINAL_WIDTH))
    print("["+ ('█' * progress) + ('.'* (TERMINAL_WIDTH - progress)) + "]")
    for y in range(resolution):
      value = mandelbrot_set.get_point_value(x, y)
      draw.point((x, y), (int(value * 255), int(value * 255), int(value * 255)))
  
  filename = "./archive/" + filename + '.png'
  image.save(filename)
  print("Render finished. File saved: " + filename)
  timer_end = time.time()
  if print_time:
    print(f"Total time: {timer_end - timer_start}")
