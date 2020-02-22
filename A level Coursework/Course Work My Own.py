TurfList = []

def initDL():
    pass


def AddTurf(TurfList):
    price = GetPrice()

    Describtion = GetDescri()

    TurfID = GetTurfID()
    
    TurfList.append([TurfID,Describtion,price])

    return(TurfList)



def GetTurfID():
    TurfID = ""

    while TurfID == "" :
        TurfID= input("Enter TurfID")

        if TurfID == "":
            print("Attention : ID MUST be filled in")

    return(TurfID)



def GetDescri():
    Describtion = ""

    while Describtion == "" :
        Describtion = input("Enter Describtion")

        if Describtion == "":
            print("Attention : Describtion MUST be filled in")

    return(Describtion)

def GetPrice():
    price = 0

    while price <= 1 or price > 10 :
        price = float(input('Enter Price'))

        if price <= 1 or price > 10:
            print('error')

    return(price)

def TurfData(TurfList):
    QuitTurfData = False

    while QuitTurfData == False:
        print("1. View/Update")
        print("2. Add New Turf")
        print("3. Go Back to Main Menu")

        choice = input("Enter the number of the chosen action ")

        if choice  == "1":
            print("Action 1 working...")

            print(TurfList)

        elif choice == "2":

            TurfList = AddTurf(TurfList)

        else:
            QuitTurfData = True
            print("Action 3 working...")
            print("Going back to main menu...")

    return(TurfList)


def main():
    Quit = False
    TurfList = []

    while Quit == False:
        print("1. Add Client Details")
        print("2 Search for Client")
        print("3. Generate Quote")
        print("4. Turf")
        print("5. Quit")


        choice = input("Enter the number of the chosen action ")
        if choice  == "1":
            print("Action 1 working...")

        elif choice == "2":
            print("Action 2 working...")

        elif choice == "3":
            print("Action 3 working...")

        elif choice == "4":
            print("Action 4 working...")
            TurfList = TurfData(TurfList)
            print(TurfList)

        else:
            print("Action 5 working...")
            print("Leaving Now...")
            Quit = True

main()
