age=int(input("enter age:"))
price=3
free=0
discount=price*1/2
if age>=6 and age<=60:
  if age>=6 and age<=18:
    print("price:", discount)
  else:
    print("price:",price)
else:
  print("price:",free)