def resolve


def picking():

    list = ["ROCK","SCISSORS","PAPER"]

    while True:
        pick = str(input("Player 1: Please pick from Rock, Paper or Scissors"))
        pick.upper()
        if any(pick in s for s in list ):
            return pick
        else:
            print("Incorrect value, try again...")

def main():

    name1 = str(input("Please provide us your name:"))
    pick1 = picking()
    print("Player %s picked %s" % (name1,pick1))
    name2 = str(input("Please provide us your name:"))
    pick2 = picking()
    print("Player %s picked %s" % (name2,pick2))
    dict = {name1:pick1,name2:pick2}
a








if __name__ == '__main__':
    main()
