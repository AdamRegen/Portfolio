import random
import os

class Grid():
    
    def __init__(self):

        self.board = []

        self.PlayerSpawn = random.randint(0,7)
        
        self.PlayerCor = [0,0]
        
        self.score = 0
        
        self.TC = {}
        
        self.B = []
        
        self.BC = {}
        
        self.coins = 0
        
    def buildBoard(self):

        for i in range(8):
            
            self.board.append([])
            
            for j in range(8):
                
                self.board[i].append(' ')
                
        self.board[self.PlayerSpawn][self.PlayerSpawn] = 'P'


    def Treasure(self):
        
        count = 1
        
        while count < 11 :
            
            x = random.randint(0,7)
            
            y = random.randint(0,7)
            
            if self.board[x][y] == ' ':
                
                temp = str(x) + str(y)
                
                self.TC.update({temp:3})
                
                self.board[x][y] = 'T'
                
                count += 1
            

    def Bandit(self):
        
        count = 1
        
        while count < 6 :
            
            x = random.randint(0,7)
            
            y = random.randint(0,7)
            
            if self.board[x][y] == ' ':
                
                temp = str(x) + str(y)
                
                self.BC.update({temp:1})
                
                self.board[x][y] = 'B'
                
                count += 1

    def display(self):

        tempstr = ' |'

        for i in range(8):

            tempstr += str(i) + '|'

        print(tempstr)
        tempstr = ''
        for i in range(9):

            tempstr += ' -'

        print(tempstr)
        
        for i in range(8):
            
            tempstr = str(i) + '|'
                          
            for j in range(8):
                
                tempstr = tempstr + self.board[i][j] + '|'
                

            print (tempstr)
            
            tempstr = ''

            for i in range(9):
                
                tempstr += ' -'

            print(tempstr)

    def getPlayerCor(self):
        
        massage = ['Enter y coordiante','Enter x Coordinate']

        self.board[self.PlayerCor[0]][self.PlayerCor[1]] = ' '
        
        for i in range(2):
            
            valid = False
            
            while not valid:
                
                tempval = int(input(massage[i]))
                
                if tempval >= 0 and tempval <= 7:
                    
                    self.PlayerCor[i] = tempval
                    
                    valid = True

                else:
                    
                    print('Error...Only in range(0 - 7)')

        print(self.PlayerCor)
        
    def UpTrea(self):

        amountOfBandits = 5

        amountOfTreasure = 10
        
        DictKey = str(self.PlayerCor[0]) + str(self.PlayerCor[1])
        
        self.TC[DictKey] = self.TC[DictKey] - 1

        self.coins += 10
        
        print(self.coins)
        
        print('Number of Treasure in location:' + str(self.TC[DictKey]))

        if self.TC[DictKey] == 0:
            
            del(self.TC[DictKey])
            
            self.BC.update({DictKey:1})

            amountOfBandits = amountOfBandits + 1

            amountOfTreasure = amountOfTreasure - 1

            print('Bandits :' + str(amountOfBandits))

            print('Tresure :' + str(amountOfTreasure))

        else:

            print('Bandits :' + str(amountOfBandits))

            print('Tresure :' + str(amountOfTreasure))

    def EndGame(self):

        chance = True
        
        available = 0

        for coins in self.TC:
            
            available += self.TC[coins] * 10
            
        if available < 100:

            chance = False
                
            print('You have Lost')

        else:
                
            print('Proceed')
            

def MainMenu():
    
    print("1. Start")

    print("2. Quit")
    
    choice = ''
    
    while choice != '2':
        
        choice = input('Enter Your Choice')
        if choice == '1':
            
            print('Bandits : 5 , Treasures : 10')
            Main()

        else:
            
            print('Goodbye')


def Main():
    my_game = Grid()
    
    my_game.buildBoard()
    
    my_game.Treasure()
    
    my_game.Bandit()
    
    coins = 0

    game = True
    while game == True:

        #os.system('cls')
        
        print()

        # Developer Coordinates to test game
        #print(my_game.TC)
        #print(my_game.BC)
        
        my_game.display()
        my_game.getPlayerCor()
        
        DictKey = str(my_game.PlayerCor[0]) + str(my_game.PlayerCor[1])

        #my_game.getBandits()
        
        my_game.EndGame()
        
        if DictKey in my_game.TC:
            my_game.UpTrea()

        elif DictKey in my_game.BC:
            my_game.coins = 0
            print('Ahh!Bandit has stole all my coins')

MainMenu()







