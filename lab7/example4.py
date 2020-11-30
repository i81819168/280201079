employees = {}
name = []
salary = []

for i in range(5):
  emp = str(input("name of employee: "))
  sal = int(input("salary of employee: "))
  name.append(emp)
  salary.append(sal)

z = zip(name, salary)
for x, y in z:
  employees[x] = y

sorted_sal = sorted(employees.values())


