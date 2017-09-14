import datetime
name = input("Jake je tve jmeno")
print("Your name is " + name)
age = int(input("Jaky je tvuj vek"))
repeat = int(input("How many times should the output be repeated"))
future_age = int(datetime.date.today().strftime("%Y")) + (100-age)
for i in range(repeat):
    print("Your age is " + str(age) + " and you'll be 100 in " + str(future_age))
