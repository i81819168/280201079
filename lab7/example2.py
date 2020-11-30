books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}

for i in books:
  length = len(i)
  unique = len(set(list(i)))
  value = (length, unique)
  book_dict[i] = value

print(book_dict)