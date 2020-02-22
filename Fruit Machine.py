import random
Symbol = ["Cherry","Bell","Lemon","Orange","Star","Skull"]


def spin(Symbol):
    temp = []
    for i in range(4):
        temp.append(random.choice(Symbol))
    
    print(temp)

    check(Symbol,temp)

def check(Symbol,temp):
    print("Checking")
    counter = {"Skull": 0 , "Cherry": 0 , "Bell": 0 , "Star": 0 , "Lemon": 0 , "Orange": 0}

    for item in temp:
        if item in counter.keys():
            counter[item] += 1

    if 3 in counter.keys():
        print("Winner")


    print(counter)

def main():

    choice = ""

    while choice != "3":
        print("1. Start a Spin!")
        print("2. Rules")
        print("3. Quit")

        choice = input(">>")
        if choice == "1":
            for x in range(5):
                spin(Symbol)
                

        elif choice == "2":
            print("Action 2 active")

        elif choice == "3":
            print("Quiting")

        else:
            print("Error : INPUT ONLY IN RANGE 1 - 3.. Retry")
            

main()
