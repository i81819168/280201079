def pascal_line(n):
  if n == 1:
    return [1]
  else:
    cur_line = [1]
    prev_line = pascal_line(n-1)
    for i in range(len(prev_line) - 1):
      cur_line.append(prev_line[i] + prev_line[i+1])
  cur_line += [1]
  return cur_line

print(pascal_line(4))