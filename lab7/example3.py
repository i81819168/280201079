books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}

for i in books:
  length = len(i)
  unique = len(set(list(i)))
  average = (int(length) + int(unique))/2
  value = (length, unique, average)
  book_dict[i] = value



print(book_dict)