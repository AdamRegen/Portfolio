#Barcode Scanner
choice = 0
while choice != '2':
    print('To continue press 1')
    print('To Halt press 2')
    choice = input('Enter')
    if choice == '1':
        barcode = int(input('Enter Barcode number:'))
    
        bar = [int(i) for i in str(barcode)]
        print(bar)
    
        a = bar[0] + bar[2] + bar[4] + bar[6] + bar[8] + bar[10]
        print(a)
        a = a*3
        print(a)
        b = bar[1] + bar[3] + bar[5] + bar[7] + bar[9]
        print(b)
        total = a + b
        print(total)

        cdo = total%10
        print(cdo)

        cdc = 10 - cdo
        print(cdc)

    else:
        print('goodbye')
    
