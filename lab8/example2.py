def is_prime(x):
  if x <= 1:
    return False
  for i in range(2, x):
    if x%i == 0:
      return False
    else:
      return True
  else:
    return True

def print_primes_between(a, b):
  for i in range(a, b):
    if is_prime(i):
      print(i)

first = int(input("first number:"))
second = int(input("second number:"))
print_primes_between(first, second)