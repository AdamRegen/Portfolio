messege = ""
shift = 0
Cipher = ""

def Encrypt(messege,shift,Cipher):
    messege = input("Your Messege ...>")
    shift = int(input("Cipher shift"))

    for i in range(0, len(messege)):
        temp = messege[i]
        print(temp)

        if temp .isalpha():
            
            if temp .islower():
                temp = ord(temp)
                temp = temp + shift
                if temp >= 122:
                    temp = temp - 25

                    Cipher = Cipher + chr(temp)
                else:
                    Cipher = Cipher + chr(temp)

            else:
                temp = ord(temp)
                temp = temp + shift
                if temp >= 90:
                    temp = temp - 25

                    Cipher = Cipher + chr(temp)

                else:
                    Cipher = Cipher + chr(temp)

        elif temp == " ":
            Cipher = Cipher + temp

        else:
            Cipher = Cipher + chr(temp)
        
    print(Cipher)


def Decrypt(messege,shift,Cipher):
    Cipher = input("Enter Cipher code")
    shift = int(input("Enter Cipher Key"))

    for i in range(0, len(Cipher)):
        temp = Cipher[i]
        print(temp)

        if temp .isalpha():
            
            if temp .islower():
                temp = ord(Cipher[i])
                temp = temp - shift
                if temp <= 97:
                    temp = temp + 25

                    messege = messege + chr(temp)
                else:

                    messege = messege + chr(temp)

            else:
                temp = ord(Cipher[i])
                temp = temp - shift
                if temp <= 65:
                    temp = temp + 25

                    messege = messege + chr(temp)

                else:
                    messege = messege + chr(temp)

        elif temp == " ":
            messege = messege + temp


        else:
            messege = messege + chr(temp)
        
    print(messege)

     


def main():
    
    choice = 0

    print("1. Encrypt")

    print("2. Decrypt")

    print("3. Quit")

    while choice != "3":
        choice = input("> ")

        if choice == "1":
            Encrypt(messege,shift,Cipher)

        else :
            Decrypt(messege,shift,Cipher)

main()
