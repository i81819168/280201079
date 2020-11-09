year=int(input("enter a year:"))
if year<100:
  if year%4==0:
    print("leap year")
  else:
    print("not leap year")
elif year%400==0:
  print("leap year")
  else:
    print("not leap year")

