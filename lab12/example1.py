class Cylinder:
  def __init__(self, radius, height):
    self.set_radius(radius)
    self.set_height(height)
  def set_radius(self, radius):
    self.radius = radius
  def set_height(self, height):
    self.height = height
  def get_radius(self):
    return self.radius
  def get_height(self):
    return self.height
  def base_area(self):
    pi = 3.14
    return pi * (self.radius**2)
  def lateral_area(self):
    pi = 3.14
    return 2 * pi * self.radius * self.height
  def area(self):
    return (self.base_area() * 2) + self.lateral_area()
  def volume(self):
    return self.base_area() * self.height

cylinder = Cylinder(3, 5)
print("area: " + str(cylinder.area()))
print("volume: " + str(cylinder.volume()))