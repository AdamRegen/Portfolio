Options = {'main': ['1. Add Client Details','2. Search for client','3. Generate Quote','4. Turf','5. Quit'],'TurfData':['1. View/Update','2. Add New Turf','3. Go to Main Menu']}

import csv

def getQuote(ClientList,TurfList):
    #DisplayClientDetails
    #DisplayTurfDetails
    #getsizeoflawn
    #calculatetotalprice
    #DisplayTotal
    #append_to_QuoteList_details

    ClientDetails = findClientID(ClientList)
    print(ClientDetails)
    input()

    TurfDetails = findTurfID(TurfList)

def getArea():
    Calc = False
    DFill = ["Width","Length/Height"]
    Dimension = []
    Area = 0

    while Calc == False:
        print("Please enter the dimension of your lawn in meters squared")

        for i in range(2):
            count = i - 1
            dvalue = input("Enter the"+DFill[count]+"of your Lawn >")
            Dimension.append(d.value)

        Area = Dimension[0]*Dimension[1]
        Calc = True

    return(Area)

def findClientID(ClientList):
    Found = False
    C_id = input("Enter Client ID > ")
    count = 0

    while Found == False:
        if ClientList[count][0] == C_id:
            Found = True
            return(ClientList[count])

        else:
            count += 1
    
    print("Not found in Data Base > ")
            #Leave = getRequestToLeave()
    
    

def findTurfID(TurfList):
    Found = False 
    T_id = input("Enter Turf ID > ")
    count = 0

    while Found == False:
        if TurfList[count][0] == T_id:
            Found = True
            return(TurfList[count])

        else:
            count += 1
    
    print("Not found in Data Base > ")
            #Leave = getRequestToLeave()
    

def getRequestToLeave():
    Request = False

    while Request == False:
        print("1.Yes")
        print("2.No")
        choice = input("Would you like to leave and retry later? >")
        
        #if choice == "1":

def GetClient(ClientList):
    #ClientID
    #clientName
    #ClientPostCode

    ClientID = GetClientID()

    ClientName = GetClientName()

    ClientPostCode = GetPostCode()

    ClientList.append([ClientID,ClientName,ClientPostCode])

    return(ClientList)

def GetClientID():
    ClientID = ""

    while ClientID == "":
        ClientID = input("ClientID > ")

        if ClientID == "":
            print("Attention : ID MUST be filled in")

    return(ClientID)

def GetClientName():
    ClientName = ""

    while ClientName == "" :
        ClientName = input("Name > ")

        if ClientName == "":
            print("Attention : Name MUST be filled in")

    return(ClientName)

def GetPostCode():
    postCode = ""
    PostC = []

    while postCode == "":
        postCode = input("PostCode > ")
        #PostC.append(postCode)

    #postalValidation(PostC)
    #return(PostC)
    return(postCode)

def postalValidate(PostC):
    pass
    
def openfile(FileName):
    DataList = [] 

    with open(FileName , 'r') as Temp_file:
        reader = csv.reader(Temp_file, delimiter=',')
        DataList = list(reader)
    
    print(DataList)
    return(DataList)

def DisplayMenu(Options):
    for i in range(len(Options)):
        print(Options[i])

def saveData(FileName,aData):

    with open(FileName, 'w' , newline='' ) as csvfile:
        FileHandle = csv.writer(csvfile, delimiter= ',', quotechar= '|')

        for i in range(len(aData)):
            temp = []
            for j in range(len(aData[i])):
                temp.append(aData[i][j])

            FileHandle.writerow(temp)

def AddTurf(TurfList):

    price = GetPrice()

    Describtion = GetDescri()

    TurfID = GetTurfID()
    
    TurfList.append([TurfID,Describtion,price])

    return(TurfList)

def GetTurfID():
    TurfID = ""

    while TurfID == "" :
        TurfID= input("TurfID > ")

        if TurfID == "":
            print("Attention : ID MUST be filled in")

    return(TurfID)

def GetDescri():
    Describtion = ""

    while Describtion == "" :
        Describtion = input("Describtion > ")

        if Describtion == "":
            print("Attention : Describtion MUST be filled in")

    return(Describtion)

def GetPrice():
    price = 0

    while price <= 1 or price > 10 :
        price = float(input('Price > £'))

        if price <= 1 or price > 10:
            print('error')

    return(price)

def TurfData(TurfList):
    Quit = False

    while Quit == False:
        DisplayMenu(Options['TurfData'])

        choice = input("Enter the number of the chosen action ")

        if choice  == "1":
            print("Action 1 working...")

            print(TurfList)

        elif choice == "2":

            TurfList = AddTurf(TurfList)

        else:
            Quit = True
            print("Action 3 working...")
            print("Going back to main menu...")

    return(TurfList)

def main(Options):
    Quit = False
    TurfList = openfile("d:\Turf.txt")
    ClientList = openfile("d:\Client.txt")

    while Quit == False:
        DisplayMenu(Options['main'])

        choice = input("Enter the number of the chosen action ")
        if choice  == "1":
            ClientList = GetClient(ClientList)

        elif choice == "2":
            print("Action 2 working...")

        elif choice == "3":
            getQuote(ClientList,TurfList)

        elif choice == "4":
            
            TurfList = TurfData(TurfList)
            print(TurfList)

        else:
        
            print("Saving Data")
            Quit = True

    saveData("d:\Turf.txt",TurfList)
    saveData("d:\Client.txt",ClientList)

main(Options)
