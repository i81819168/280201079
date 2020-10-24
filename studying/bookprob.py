book=int(input("write the cover price in cents:"))
discount=int(input("write the discount amount:"))/100
ship_1=int(input("write the shipping fee for the first book in cents:"))
ship_rest=int(input("write the shipping fee for the rest of the books in cents:"))
num_books=int(input("write the total nuber of books:"))
ship_total=ship_1+ship_rest*(num_books-1)
book_total=num_books*book*(1-discount)
total=ship_total+book_total
print(total/100)
