class Gardeners_Program():
    pass

def TurfData():
    QuitTurfData = False
    print("1. Update")
    print("2. Add New Turf")
    print("3. Go Back to Main Menu")

    while QuitTurfData == False:
        choice = input("Enter the number of the chosen action ")

        if choice  == "1":
            print("Action 1 working...")

        elif choice == "2":
            print("Action 2 working...")

        else:
            print("Action 3 working...")
            print("Going back to main menu...")
            main()



def main():
    Quit = False
    print("1. Add Client Details")
    print("2 Search for Client")
    print("3. Generate Quote")
    print("4. Turf")
    print("5. Quit")

    while Quit == False:
        choice = input("Enter the number of the chosen action ")
        if choice  == "1":
            print("Action 1 working...")

        elif choice == "2":
            print("Action 2 working...")

        elif choice == "3":
            print("Action 3 working...")

        elif choice == "4":
            print("Action 4 working...")
            TurfData()

        else:
            print("Action 5 working...")
            print("Leaving Now...")
            Quit = True

main()
