a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

d=b**2-4*a*c

root1=(-b-d**0.5)/2*a
root2=(-b+d**0.5)/2*a

if d>0:
  print("there are two real roots:", root1,root2)
elif d==0:
  print("there is one root:", root1)
elif d<0:
  print("there are two complex roots:", root1,root2)