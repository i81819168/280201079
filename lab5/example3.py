x=input("enter a positive integer:")
y=input("enter a positive integer:")

x=int(x)
y=int(y)

first=0

while x>0 and y>0:
  if x%10==y%10:
    first+=1
  x=x//10
  y=y//10
print(first)


