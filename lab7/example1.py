lst = [("Jon",15), ("Ned",45), ("Arya",9), ("Catelyn",44), ("Bran",10)]
dicti = {}
for i in lst:
  key, value = i
  dicti[key] = value

for k in dicti.keys():
  if dicti[k] > 18:
    print(k)