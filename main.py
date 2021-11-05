import render
from decimal import Decimal
from datetime import datetime

def main():
  delete_line = ('\033[F' + ' ' * 70 + '\033[F')
  resolution = input("resolution: ")
  print(delete_line)
  filename = input("filename: ")
  print(delete_line)
  center_x = input("center x:")
  print(delete_line)
  center_y = input("center y:") 
  print(delete_line)
  scale = input("scale: ")
  print(delete_line)
  threshold = input("threshold: ")
  print(delete_line)
  max_iterations = input("max_iterations x:")
  print(delete_line)
  print_time = input("Do you want to print execution time? (y/n) ")
  print(delete_line)

  if filename == "":
    filename = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

  if resolution == "":
    resolution = 480
  else:
    resolution = int(resolution)

  if center_x == "":
    center_x = 0
  else:
    center_x = Decimal(center_x)

  if center_y == "":
    center_y = 0
  else:
    center_y = Decimal(center_y)

  if scale == "":
    scale = 0.5
  else:
    scale = Decimal(scale)

  if threshold == "":
    threshold = 2
  else:
    threshold = Decimal(threshold)
  
  if max_iterations == "":
    max_iterations = 255
  else:
    max_iterations = int(max_iterations)

  print_time_b = False
  if print_time == "y":
    print_time_b = True

  print("Okay, current settings are: ")
  print(f"   resolution: {resolution}")
  print(f"   center coordinates: ({center_x}, {center_y})")
  print(f"   scale: {scale}")
  print(f"   threshold: {threshold}")
  print(f"   maximal interation: {max_iterations}")
  print(f"   filename: {filename}")
  print(f"   print time: {print_time_b}")
  
  ok = input("Do you want to continue? (y/n) ")

  if (ok != "y"):
    print("Okay, bye")
    return

  
  
  render.render(resolution=resolution, center_x=center_x, center_y=center_y,
                scale=scale, threshold=threshold, max_iterations=max_iterations,
                filename=filename, print_time=print_time_b)


main()