import os
import platform
from PIL import Image

class IO:
  _system = ''
  _terminal_width = 80
  _terminal_height = 41

  def __init__(self):
    self._system = platform.system()

    if (self._system == 'Windows'):
      print("Windows system detected")

      # Terminal resize
      os.system('$host.UI.RawUI.WindowSize.Width = ' + str(self._terminal_width))
      os.system('$host.UI.RawUI.WindowSize.Height = ' + str(self._terminal_height))

    else:
      print("Unix system detected")

      # Terminal resize
      os.system('resize -s ' + str(self._terminal_height) + ' ' + str(self._terminal_width))

  def progress_bar_unix(self, it, max_it):
    print('\033[F' * 2)
    progress = int((it / (max_it - 1)) * (self._terminal_width - 2))
    print("["+ ('█' * progress) + ('.' * (self._terminal_width - 2 - progress)) + "]")

  def progress_bar_windows(self, it, max_it):
    percentage = it * 100 // max_it

    if (percentage % 5 == 0):
      print(percentage + "%")
    
  def get_progress(self):
    if (self._system == "Windows"):
      return self.progress_bar_windows
    else:
      return self.progress_bar_unix

  def process_image(self, im):
    im.show()
    save = input("Save? (y/n) ")
    
    if save == "y":
      filename = "./archive/" + filename + '.png'
      im.convert('RGB').save(filename)
    
  def ask(self, question, default):
    variable = input(question)
    if (variable == ""):
      variable = default
    else:
      variable = int(variable)
      
    if self._system != "Windows":
      print('\033[F' + ' ' * self._terminal_width + '\033[F')
    
    return variable
    
