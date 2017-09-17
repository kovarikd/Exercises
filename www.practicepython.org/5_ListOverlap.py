import random

def gen_random_list(length,value):
    list_result = []
    for x in range(1,length + 1):
        list_result.append(random.randint(1,value))
    return list_result

def main():
    length_1 = int(input("Length of field one?"))
    val_1 = int(input("Max value in field one?"))
    length_2 = int(input("Length of field two?"))
    val_2 = int(input("Max value in field two?"))
    list_1 = gen_random_list(length_1,val_1)
    list_2 = gen_random_list(length_2,val_2)

    print("List 1: {}".format(list_1))
    print("List 2: {}".format(list_2))
    output = []

    for element in list_1:
        if element in list_2:
           output.append(element)
    if not output:
        print("No common numbers")
    else:
        print("Common numbers: {}".format(output))




if __name__ == '__main__':
    main()
