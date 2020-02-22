listofcoins = [500,200,100,50,20,10,5,1]

nosofcoin = []

nameofcoins = ('Five Pounds','Two Pounds','one Pound','Fifty Pence','Twenty Pence','Ten Pence','Five Pence','One Pence')

priceofitem = int(input('What is the price in p:'))

moneyputin = int(input('How much in p did you put in'))

change = moneyputin - priceofitem


for i in range(len(listofcoins)):
    nosofcoin.append(0)
    if change > listofcoins[i]:
        coin = change // listofcoins[i]
            
        nosofcoin[i] = coin

        change = change%listofcoins[i]

        print(coin)
    
for i in range(len(listofcoins)):
    print(nameofcoins[i] + ':' + str(nosofcoin[i]))

print(nosofcoin)

