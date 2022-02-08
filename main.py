import output
import sys
import src.terminal as terminal

from datetime import datetime

def setup_render(io):
  mode = input("Enter mode (cupy, numpy, python - default): ")
  if (mode == 'cupy'):
    import cupy as np
    print("Cupy detected, using cuda for matrix multiplication")
    MODE = "cupy"
  elif (mode == 'numpy'):
    import numpy as np
    print("Numpy detected, using it for matrix multiplication")
    MODE = "numpy"
  else:
    mode = 'python'

  if mode == "python":
    print("Numpy or Cupy are not detected, using slow python")
    import src.pil as pil
    from decimal import Decimal
    render = pil.Render(io.get_progress(), io.process_image)
    return mode, int, Decimal,  render.render
  else:
    import numpy_src.render as numpy_render
    render = numpy_render.NumpyRender(io.get_progress(), io.process_image, mode)
    return mode, np.int16, np.float64, render.render

def main():
  io = output.IO()
  framework, integer_type, float_type, render = setup_render(io)

  configuration = {
    "resolution" : 256,
    "center_x" : 0.0,
    "center_y" : 0.0,
    "scale" : 0.5,
    "threshold" : 2.0,
    "max_iterations" : 80
  }

  for x in configuration:
    print(x, configuration[x])

  terminal.render(configuration, io)

  while (True):
    argv = input().split()
    argc = len(argv)
    if (argc == 0):
      continue
    
    if (argc == 1):
      if (argv[0] == "q"):
          exit(0)

      delta = 0.25 / configuration['scale']

      if (argv[0] == "+"):
        if (configuration['scale'] <= 1):
          configuration['scale'] *= 2
        else:
          configuration['scale'] **= 1.2

        delta = 0.25 / configuration['scale']

      elif (argv[0] == "-"):
        if (configuration['scale'] <= 2):
          configuration['scale'] *= 0.5
        else:
          configuration['scale'] **= 1 / 1.2
      
      elif (argv[0] == "a"):
        configuration['center_x'] -= delta
      elif (argv[0] == "d"):
        configuration['center_x'] += delta
      elif (argv[0] == "w"):
        configuration['center_y'] -= delta
      elif (argv[0] == "s"):
        configuration['center_y'] += delta

    else:
      if (argv[0] == "render"):
        configuration['resolution'] = int(argv[1])

        filename = datetime.today().strftime('%Y%m%d%H%M%S')

        render(integer_type(configuration['resolution']),
              float_type(configuration['center_x']),
              float_type(configuration['center_y']),
              float_type(configuration['scale']),
              float_type(configuration['threshold']),
              integer_type(configuration['max_iterations']),
              filename, framework, True)

    terminal.render(configuration, io)

main()