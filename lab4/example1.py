x=int(input("enter an integer(e.g:05,120):"))
if x<10:
  total=x
else:
  digits=x%10
  tens=(x//10)%10
  total=digits+tens
print(total)