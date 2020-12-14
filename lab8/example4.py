def binary_to_dec(bin):
  bin = str(bin)
  rev_bin = bin[::-1]
  sum = 0
  for i in range(len(rev_bin)):
    sum += 2**i * int(rev_bin[i])
    
  return sum

def dec_to_binary(dec):
  bin = ""
  while dec > 0:
    bin += str(dec%2)
    dec //= 2
  return bin[::-1]

def main():
  bin = "10010"
  dec = 18
  print(binary_to_dec(bin))
  print(dec_to_binary(dec))

main()