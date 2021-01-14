class Employee:
  def __init__(self, name, salary):
    self.set_name(name)
    self.set_salary(salary)
  def set_name(self, name):
    self.name = name
  def get_name(self):
    return self.name
  def set_salary(self, salary):
    self.salary = salary
  def get_salary(self):
    return self.salary

class Company:
  def __init__(self):
    self.employee_list = []
  def set_employee_list(self, employee_list):
    if type(employee_list) == list:
      self.employee_list = employee_list
  def get_employee_list(self):
    return self.employee_list
  def add_employee(self, new_employee):
    if isinstance(new_employee, Employee):
      if new_employee != "":
        self.employee_list.append(new_employee)
  def average_sal(self):
    total = 0 
    for emp in self.employee_list:
      total += emp.get_salary()
    print(f'average salary: {total / len(self.employee_list)}')
  def display(self):
    for emp in self.employee_list:
      print(f'employee: {emp.get_name()} \nsalary: {emp.get_salary()}')
  
comp = Company()
emp1 = Employee("gina", 10)
emp2 = Employee("jake", 20)
emp3 = Employee("amy", 50)

comp.add_employee(emp1)
comp.add_employee(emp2)
comp.add_employee(emp3)
comp.display()
comp.average_sal()