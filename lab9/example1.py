def harmonic_sum(a):
  if a == 1:
    return 1
  return 1/a + harmonic_sum(a-1)

a = 5
print(harmonic_sum(a))