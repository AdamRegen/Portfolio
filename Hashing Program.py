import random

def main():
    Name = []
    Hash = []

    Hash = createHash(Hash)
    Name = createName(Name)

    print(Hash)
    print(Name)

    updateHash(Name,Hash)

def createHash(Hash):
    for i in range(100):

        Hash.append(["",0])

    return(Hash)

def createName(Name):
    for i in range(100):
        namelen = random.randint(2,10)
        temp =""

        for x in range(namelen):

            asciicode= random.randint(65,90)
            
            temp = temp + chr(asciicode)

        Name.append(temp)

    return(Name)

def updateHash(Name,Hash):
    for i in range(1, 100):
        tempcode = ""
        tempName = Name[i]

        for j in range(1, len(tempName)-1):

            asciicode = ord(tempName[i])

            tempcode = tempcode + str(asciicode)
        
        pointer = int(tempcode) % 100

        print(pointer)



main()

