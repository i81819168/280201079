password="abc123"

while True:
  p=input("enter password:")
  if p==password:
    print("welcome")
    break
  elif p=="help":
    print("first character is: ", password[0])
  else:
    print("wrong") 

