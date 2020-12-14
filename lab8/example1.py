def sum_square(lst):
  sum = 0
  for i in lst:
    sum += i
  sol = sum**2
  return sol

a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]

print(sum_square(a_list))
