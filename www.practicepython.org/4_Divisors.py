number = int(input("For which number are you looking divisors for?"))
x = range(2,number)
output = []

for element in x:
    if number % element == 0:
        output.append(element)

for element in output:
    print(element)