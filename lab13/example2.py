def binary_search(listt, num, low, high):
  if low > high:
    return -1
  else:
    mid = (low + high) // 2
    if num == listt[mid]:
      return mid
    elif listt[mid] < num:
      return binary_search(listt, num, mid+1, high)
    else:
      return binary_search(listt, num, low, mid-1)

arr = [ 2, 3, 4, 10, 40 ]
x = 10

result = binary_search(arr, x, 0, len(arr)-1)

if result == -1:
  print("number not found.")
else:
  print("number found at index ", str(result))