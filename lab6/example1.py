mail = str(input("enter your email: "))
reference = "ceng113@example.com"

if "@" in mail:
  mail = mail.lower()
  part1 = mail.split("@")[0]
  part1 = part1.replace(".", "")
  part2 = mail.split("@")[1]
  mail = part1 + "@" + part2

  if mail == reference:
    print("it is a match")
  else:
    print("not a match")

else:
  print("not a match")