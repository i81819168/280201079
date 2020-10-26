gpa=float(input("GPA:"))
numLecture=int(input("number of lectures:"))
gpa_control=2.0
numLecture_control=47
if gpa<gpa_control and numLecture<numLecture_control:
  print("not enough number of lectures and GPA!")
elif gpa<gpa_control:
  print("not enough GPA!")
elif numLecture<numLecture_control:
  print("not enough number of lectures!")
else:
  print("GRADUATED!")

