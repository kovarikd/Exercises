delenec = int(input("Input the dividend"))
delitel = int(input("Input the factor number"))

if delenec % 4 == 0:
    print("This number is divisible by 4")
elif delenec % 2 == 0:
    print("This number is divisible by 2")
else:
    nmb = delenec % delitel
    print("This isn't divisible by 2 nor 4, remainder when divided by " + str(delitel) + " is " + str(nmb))
