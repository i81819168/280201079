def even_nums(lst):
  return get_evens(lst, 0)

def get_evens(lst, c=0):
  if len(lst) == 0:
    return c
  else:
    cur = lst.pop()
    if cur >= 0 and cur % 2 == 0:
      c += 1
    return get_evens(lst, c)
    
lstt = [0, 1, 2, 3, 4, 5, 6]

print(even_nums(lstt))