def sum_of_list(lst):
  if not isinstance(lst, list):
    return lst
  else:
    sum = 0
    for x in lst:
      sum += sum_of_list(x)
    return sum

a_list = [3,12,76,[4,56,43],[2,8],81,75]
print(sum_of_list(a_list))