import random
import time
from random import randint

# Welcome text

print('####### ANAGRAM #######')
print('Enter !hint to reveal first letter, !solve to reveal the word, and !exit to close the program')

# Opening file and picking random word
with open("words.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))

play = True 

while play:

    # Print random string
    word = random.choice(words)

    # Shuffling it
    str_var = list(word)
    random.shuffle(str_var)
    s_word = ''.join(str_var)

    # Length of asterick
    ast = len(word) * '*'

    print("TASK:", s_word, ast)

    x = True    
    while x:
        u_in = input("Guess the word: ")

   
        if u_in == word:
            print('Correct!')
            x = False

        elif u_in == '!hint':
            print('Hint: ' + word[0] + (len(word)-1) * '*')

        elif u_in == '!solve':
            print('The word was:', word)
            time.sleep(2)
            x = False

        elif u_in == '!exit':
            play = False

        else:
            print('Wrong!')

file.close()