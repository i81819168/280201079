def pascal_tri(n):
  if n == 0:
    return []
  elif n == 1:
    return [[1]]
  else:
    new_line = [1]
    final = pascal_tri(n - 1)
    last_line = final[-1]
    for i in range(len(final) - 1):
      new_line.append(last_line[i] + last_line[i + 1])
    new_line += [1]
    final.append(new_line)
  return final

print(pascal_tri(4))