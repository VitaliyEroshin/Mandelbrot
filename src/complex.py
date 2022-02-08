class Complex:
  re = 0
  im = 0

  def __init__(self, re, im):
    self.re = re
    self.im = im

  def __add__(self, other):
    self.im += other.im
    self.re += other.re
    return self

  def __mul__(self, other):
    re = self.re * other.re - self.im * other.im
    im = self.re * other.im + self.im * other.re
    self.re, self.im = re, im
    return self

  def __abs__(self):
    return self.re * self.re + self.im * self.im
