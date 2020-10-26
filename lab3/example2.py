num1=float(input("write the first number:"))
num2=float(input("write the second number:"))
num3=float(input("write the third number:"))
if num1<num2 and num1<num3:
  print("minimum:",num1)
if num2<num1 and num2<num3:
  print("minimum:",num2)
if num3<num1 and num3<num2:
  print("minimum:",num3)