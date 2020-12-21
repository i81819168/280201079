def get_reversed(lst):
  if len(lst) == 0:
    return []
  return [lst.pop()] + get_reversed(lst) 
  

lstt = [1, 2, 3, 4]

print(get_reversed(lstt))