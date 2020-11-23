grades = []
n = int(input("number of students: "))
for i in range(n):
  print("student" + str(i+1))
  mid1 = int(input("midterm 1: "))
  mid2 = int(input("midterm 2: "))
  fin = int(input("final: "))
  grades.append([mid1, mid2, fin])

print("grades: ", grades)

average = []
for x in grades:
  avg = x[0]*0.3 + x[1]*0.3 + x[2]*0.4
  average.append(avg)

print("average grades: ",average)
