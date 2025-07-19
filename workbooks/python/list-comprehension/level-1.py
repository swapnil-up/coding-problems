celsius_temps = [0, 20, 25, 30, 37, 100]
print([((C * 9/5) + 32) for C in celsius_temps])

print([i*i for i in range(1, 11)])

prices = [19.99, 4.95, 129.99, 15.00, 3.50]
print([p*1.08 for p in prices])

names = ['alice', 'bob', 'charlie', 'diana']
print([name.upper() for name in names])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print([n for n in numbers if n%2==0])

grades = [85, 92, 78, 65, 90, 88, 76, 95, 67, 82]
print([pas for pas in grades if pas>=70])

emails = ['user@example.com', 'invalid-email', 'test@gmail.com', 'bad.email']
print([email for email in emails if "@" in email])

numbers = [-5, 3, -2, 8, -1, 0, 7, -9, 4]
print([number for number in numbers if number>0 ])

prices = [25.99, 75.00, 12.50, 199.99, 45.00, 89.99]
print([price*0.8 if price>50 else price for price in prices])

words = ['apple', 'banana', 'cat', 'elephant', 'dog', 'computer', 'book']
print([len(word) for word in words if len(word)>5])

numbers = [4, 7, 9, 15, 16, 20, 25, 30, 36]
print([number for number in numbers if number])