class Code_Pazzle:
    def __init__(self):
        self.Solved = []
        self.Sol = 0
        self.Clues = []
        self.answer = {'+':'C','/':'Q',0:'U',8:'I',4:'R','"':'D',3:'L',2:'S',':':'T',1:'O','$':'K','!':'H','-':'Y','.':'G',7:'Z',6:'B',"'":'W',')':'F',5:'X',9:'V'}
        self.Words = []

    def loadWords(self):
        with open('words.txt') as file:
            for i in file:
                i = i.strip()
                self.Words.append(i)

        return(self.Words)

    def loadClues(self):
        with open('clues.txt') as file:
            for i in file:
                i = i.strip()
                self.Words.append(i)

    def loadsolved(self):
        with open("solved.txt") as file:
            for i in file:
                i = i.strip()
                self.Solved.append(i)

        return(self.Solved)


    def guesses(self):
        guesses = 3

        while guesses != 0:
            s = input("What do you want to guess? > ")
            g1 = input("Your guess for that symbol/Number > ")

            if s in self.answer:
                print("Updating")
                Update(s,g)

            else:
                guesses -= 3
                print(guesses + "More Guesses Till you will be prompt to Help")

    def Update(self):
        


def main():
    choice = '' 
    print('Start Puzzle > Yes or No')
    print('Sneek Peek > Sure')
    print('Quit > Press "0"')

    while choice != '0':
        if choice == 'Yes' or 'yes':
            pass

        elif choice == 'Sure' or 'sure':
            pass

        elif choice == '0':
            print('GoodBye')


import sys
main()

