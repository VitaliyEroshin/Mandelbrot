from PIL import Image, ImageDraw
import numpy as np
from datetime import datetime
import time

def progress_bar_unix(x, y):
  TERMINAL_WIDTH = 78
  print('\033[F' * 2)
  progress = int((x / (y-1)) * (TERMINAL_WIDTH))
  print("["+ ('█' * progress) + ('.'* (TERMINAL_WIDTH - progress)) + "]")

def init_np_array(resolution, center_x, center_y, scale):
  a = np.zeros((resolution, resolution), dtype=np.complex256)
  a[:, :].imag = np.arange(0, resolution)
  a = a.T
  a[:, :].real = np.arange(0, resolution)
  a.real /= resolution - 1
  a.imag /= resolution - 1
  a.real -= 0.5
  a.imag -= 0.5
  a.real /= np.float64(scale)
  a.imag /= np.float64(scale)
  a.real += center_x
  a.imag += center_y
  return a

def render(resolution=640, center_x=-0.75, center_y=0.25, 
           scale=3, threshold=2, max_iterations=255, 
           filename="", print_time=True):
  
  a = init_np_array(resolution, center_x, center_y, scale)

  z = np.zeros((resolution, resolution), dtype=np.complex256)
  it = np.zeros((resolution, resolution), dtype=np.int64)

  timer_start = time.time()

  m1 = (it == 0)

  for i in range(max_iterations):
    progress_bar_unix(i, max_iterations)

    z[m1] = z[m1] * z[m1] + a[m1]
    z[m1].imag = np.around(z[m1].imag, 100)
    z[m1] = np.around(z[m1], 100)
    r = z.imag * z.imag + z.real * z.real
    m2 = (r <= threshold)
    m1 = m1 * m2
    
    it[m1] = it[m1] + np.int64(1)
  
  it *= np.int64(240)
  it //= max_iterations

  im = Image.fromarray(it.astype(np.int8))
  im.show()

  print("Render finished")
  timer_end = time.time()
  if print_time:
    print(f"Total time: {timer_end - timer_start}")

  _save = input("Save? (y/n) ")
  if _save == "y":
    filename = "./archive/" + filename + '.png'
    im.convert('RGB').save(filename)
  
