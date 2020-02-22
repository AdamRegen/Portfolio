Options = {'main': ['1. Add Client Details','2. Search for client','3. Generate Quote','4. Turf','5. Quit'],'TurfData':['1. View/Update','2. Add New Turf','3. Go to Main Menu']}
TurfList = []

def DisplayMenu(Options):
    for i in range(len(Options)):
        print(Options[i])

def main(Options):
    Quit = False
    TurfList = []

    while Quit == False:
        DisplayMenu(Options['main'])

        choice = input("Enter the number of the chosen action ")
        if choice  == "1":
            print("Action 1 working...")

        elif choice == "2":
            print("Action 2 working...")

        elif choice == "3":
            print("Action 3 working...")

        elif choice == "4":
            
            #TurfList = TurfData(TurfList)
            #print(TurfList)
            print('Action 4 Working....')
            TurfData(Options)

        else:
        
            print("Saving Data")
            Quit = True

    #saveTurf(TurfList)

def TurfData(Options):
    Quit = False
    
    while Quit == False:

        DisplayMenu(Options['TurfData'])

        choice = input("Enter the number of the chosen action ")

        if choice  == "1":
            print("Action 1 working...")

            print(TurfList)

        elif choice == "2":
            print('Action 2 working....')
            #TurfList = AddTurf(TurfList)

        else:
            
            print("Action 3 working...")
            print("Going back to main menu...")
            Quit = True

main(Options)