import random

words = ['python', 'program', 'hangman', 'codealpha', 'developer', 'intenship', 'guess', 'software', 'data', 'computer', 'skills']

word = random.choice(words)
clue = ['_'] * len(word)
incorrect = 0
max_incorrect = 6

while incorrect < max_incorrect:
    print(' '.join(clue))               # it shows number of letters in words
    
    guess = input("Guess the word: ").lower()

    if guess != word:
        incorrect += 1
        print("Wrong!",max_incorrect - incorrect,"guesses left.")

    else:
        print("You win! The word is",guess)
        break

if incorrect == max_incorrect:
    print("Game over! The word is",word)
