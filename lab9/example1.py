def harmonic_sum(a):
  if a != 0:
    sum = 0
    for i in range(1, a+1):
      sum += 1/i
  return sum

a = 5
print(harmonic_sum(a))