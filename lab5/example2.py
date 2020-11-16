N=int(input("how many integers?:"))
even_nums=0
for i in range(0,N):
  num=int(input("enter an integer:"))
  if num%2==0:
    even_nums+=1
print(even_nums/N*100,"%")
