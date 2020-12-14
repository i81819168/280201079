import random
def get_rand_list(b, e, N):
  rand_list = random.sample(range(b, e), N)
  return rand_list

def get_overlap(list1, list2):
  list3 = []
  for i in list1:
    if i in list2:
      list3.append(i)
  return list3

def main():
  b = 0
  e = 10
  N = 5
  list1 = get_rand_list(b, e ,N)
  list2 = get_rand_list(b, e ,N)
  list3 = get_overlap(list1, list2)
  print(list1)
  print(list2)
  print(list3)

main()