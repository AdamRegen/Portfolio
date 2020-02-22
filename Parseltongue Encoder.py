def encode(message):
    cipher = ""
    for i in message:
        cipher = cipher + i + "sss"
    return(cipher)
  
def decode(cipher):
    message = ""
    for i in range(0,len(cipher),4):
        message = message + cipher[i]
    return(message)

def main():
    print('1. Encode to cipher')
    print('1. Decode to message')
    print('3. QUIT')
    choice = input(':')
    while choice != 3:
        if choice == '1':
            message = input("message:")
            encode(message)
            print(encode(message))

        elif choice == '2':
            cipher = input("cipher:")
            decode(cipher)
            print(decode(cipher))
        
main()
