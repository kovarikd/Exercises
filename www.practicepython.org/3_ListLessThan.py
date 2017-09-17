a = [1,1,2,3,5,8,13,21,34,55,89]
output = " "

number = int(input("Selected should be smaller than which number?"))
for element in a:
    if element < number:
        output = output + " " + str(element)

print(output)
