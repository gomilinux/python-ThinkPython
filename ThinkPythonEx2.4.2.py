#Think Python Exercise 2.4 number 2
#Find the total wholesale cost of 60 books
#Cover price is $24.95, bookstore price is 40% discount
#Shipping is $3 for first copy and $0.75 for each additional copy

print('How many books?')
quantity = input()

sale = 24.95
wholesaleEach = sale * 0.40
subtotal = sale * wholesaleEach
print('Subtotal = ' + str(subtotal))

shipping = 3.00 + (quantity - 1)*0.75

total = subtotal + shipping

print('Shipping will be ' + str(shipping) + '.')

print('Total will be ' + str(total) + '.')


