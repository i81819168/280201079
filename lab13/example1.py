def selection_sort(listt):
  for i in range(len(listt)-1):
    min = i
    for k in range(i+1, len(listt)):
      if listt[k] < listt[min]:
        min = k
    listt[i], listt[min] = listt[min], listt[i]


sort_list = [55,25,78,2,17,98,13,5]
selection_sort(sort_list)
print(sort_list)