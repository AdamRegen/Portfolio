class EventCalendar():
    def __init__(self):
        self.Calendar = []
        self.ToC = 0

    def AddEvent(self):
        for i in range(len(self.Calendar)):
            addDate = input("Enter Date")
            if addDate in self.Calendar:
                for j in range(len(self.Calendar[i])):
                    addEvent = input("Enter Event")
                    if addEvent in self.Calendar[i]:
                        print("Event Already Added")

                    else:
                        self.Calendar[i].append(addEvent)

            else:
                self.Calendar.append(addDate)
                for j in range(len(self.Calendar[i])):
                    addEvent = input("Enter Event")
                    if addEvent in self.Calendar[i]:
                        print("Event Already Added")

                    else:
                        self.Calendar[i].append(addEvent)



    def RemoveEvent(self):
        for i in range(len(self.Calendar)):
            print("1. Remove Date and all event in that date?")
            print("2. Remove Event only")
            choice = input("Choose Either 1 or 2")
            
            if choice == "1":
                for i in range(len(self.Calendar)):
                    date = input("Date")
                    if date in self.Calendar[i]:
                        self.Calendar[i] = " "
                        i = " "

                        
                        i = " "

            else:
                print("Date not in Calendar")



def menu():
    print("1. Show Calendar")
    print("2. Add to Calendar")
    print("3. Remove from Calendar")
    print("4. Quit Event Logger")
    choice = input("___Enter Number of wanted action___:")

    while choice != "4":
        if choice == "1":
            print(myCalendar.Calendar)


        elif choice == "2":
            myCalendar.AddEvent()

        else :
            myCalendar.RemoveEvent()



myCalendar = EventCalendar()
menu()