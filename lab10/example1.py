def basic_mult(n):
  if n == 1:
    return 3
  else:
    return 3 + basic_mult(n-1)
    
print(basic_mult(6))