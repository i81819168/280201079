def hailstone(x):
  st = str(x)
  if x == 1:
    return st
  elif x % 2 == 0:
    return st + "," + hailstone(x//2)
  else:
    return st + "," + hailstone(3*x + 1)

print(hailstone(5))