class Students:
  def __init__(self, name, grades):
    self.name = name
    self.set_grades(grades)
  def set_grades(self, grades):
    self.grades = grades
  def calc_average(self):
    mid1 = self.grades[0] * 0.2
    mid2 = self.grades[1] * 0.2
    final = self.grades[2] * 0.4
    hw1 = self.grades[3] * 0.1
    hw2 = self.grades[4] * 0.1
    result = mid1 + mid2 + final + hw1 + hw2
    return result

stud1 = Students("elif", [80, 100, 60, 75, 55])
print(stud1.calc_average())