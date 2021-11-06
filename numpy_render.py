from PIL import Image, ImageDraw
import sys

from datetime import datetime
import time

class NumpyRender:
  _complex_precision = 100
  _max_color_value = 240

  def __init__(self, _progress_function, _process_image, mode):
    self._progress_function = _progress_function
    self._process_image = _process_image

  def init_np_array(self, resolution, center_x, center_y, scale, framework):
    if (framework == 'cupy'):
      import cupy as np
    else:
      import numpy as np
    
    array = np.zeros((resolution, resolution), dtype=np.complex256)
    array[:, :].imag = np.arange(0, resolution)
    array = array.T
    array[:, :].real = np.arange(0, resolution)
    array.real = ((array.real / (resolution - 1)) - 0.5) / scale + center_x
    array.imag = ((array.imag / (resolution - 1)) - 0.5) / scale + center_y

    return array

  def render(self, resolution, center_x, center_y, 
            scale, threshold, max_iterations, 
            filename, framework, print_time=True):

    if (framework == 'cupy'):
      import cupy as np
    else:
      import numpy as np

    a = self.init_np_array(resolution, center_x, center_y, scale, framework)[:][:]
    z = np.zeros((resolution, resolution), dtype=np.complex256)
    iterations = np.zeros((resolution, resolution), dtype=np.int64)

    in_set = (iterations == 0)

    for i in range(max_iterations):
      self._progress_function(i, max_iterations)

      z[in_set] = z[in_set] * z[in_set] + a[in_set]
      z[in_set].imag = np.around(z[in_set].imag, 30)
      z[in_set] = np.around(z[in_set], 30)
      r = z.imag * z.imag + z.real * z.real
      bad_points = (r <= threshold)
      in_set = in_set * bad_points
      
      iterations[in_set] = iterations[in_set] + np.int64(1)
    
    iterations *= np.int64(240)
    iterations //= max_iterations

    image = Image.fromarray(iterations.astype(np.int8))

    self._process_image(image)
