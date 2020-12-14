def sec_level(password):
  alph = 0
  num = 0
  spec = 0
  level = 0
  if len(password) < 8:
    return level
  elif " " in password:
    return level
  
  for i in password:
    if i.isalpha():
      alph +=1
    elif i.isnumeric():
      num += 1
    else:
      spec += 1
    
  if alph > 0:
    level +=1
  if num > 0:
    level +=1
  if spec > 0:
    level +=1

  return level

def main():
  password = input("enter password:")
  print("security level: ", sec_level(password))

main()

