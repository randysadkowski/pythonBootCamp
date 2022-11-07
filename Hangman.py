import random
from hangmanExtras import stages
from hangmanExtras import wordList
from hangmanExtras import logo
gameOver = False
chosenWord = random.choice(wordList)
wordLength = len(chosenWord)
lives = 6

display = []
for _ in range(len(chosenWord)):
    display += "_"

print(logo)
while not gameOver:
    guess = input("Guess a letter: ").lower()
    print()

    if guess in display:
        print(f"You already guessed {guess}")

    for position in range(wordLength):
        letter = chosenWord[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosenWord:
        lives = lives - 1
        print(f"You guessed {guess}, which is not in the word. You lose a life.")

    print(' '.join(display))
    print(stages[lives])

    if "_" not in display:
        gameOver = True
        print("You win!")
    if lives == 0:
        gameOver = True
        print("You lose!")