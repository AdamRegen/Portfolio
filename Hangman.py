#Hungman

print('This is Hangman, a game for those who seeks advanture.Guess the word and if you dont, you will be hang')
print('Rules')


Word = input('What is your word of choice for players')
ans = ''
for i in range(len(Word)):
    ans = '_' + ans

lives = len(Word)//2
Guessed = False

while lives > 0 and Guessed == False:
    guess = input('Choose your letters wisely')
    if Word.find(guess) != -1:
        num = Word.index(guess)
        temp = ans[:num] + guess + ans[num+1:]
        ans = temp
        print(temp)
        
    else:
        lives - 1
        print('Incorrect. Your closer to death')

    if Guessed == True and lives > 0:
        print('Chicken Dinner')

    elif lives == 0 and Guessed == False:
        print('You Lose.Ripper takes you')

    
