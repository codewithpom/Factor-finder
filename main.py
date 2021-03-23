factors = []
i = 0
number = int(input("Enter the number"))
while i <= number:
    i = i+1
    if number % i == 0:
        factors.append(i)


print(factors)


