word = str(input("Insert word which should be tested for palindrome:"))
flag = True

rvs = word[::-1]

print(rvs)
print(word)

if word == rvs :
    print("Word is palindrom")
else:
    print("Word is not palindrom")
