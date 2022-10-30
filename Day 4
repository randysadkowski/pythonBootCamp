import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

RPSMoves = [Rock, Paper, Scissors]

userChoice = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors. "))
if userChoice < 0 or userChoice >= 3:
    print("You chose an invalid option, you lose!")
    exit()
userChoiceInteger = int(userChoice)
computerChoice = random.randint(0, 2)

print(f"You chose: {RPSMoves[userChoiceInteger]}")
print(f"Computer chose: {RPSMoves[computerChoice]}")

if RPSMoves[userChoiceInteger] == Rock and RPSMoves[computerChoice] == Rock:
    print("Tie!")
elif RPSMoves[userChoiceInteger] == Rock and RPSMoves[computerChoice] == Paper:
    print("You Lose!")
elif RPSMoves[userChoiceInteger] == Rock and RPSMoves[computerChoice] == Scissors:
    print("You Win!")

if RPSMoves[userChoiceInteger] == Paper and RPSMoves[computerChoice] == Paper:
    print("Tie!")
elif RPSMoves[userChoiceInteger] == Paper and RPSMoves[computerChoice] == Scissors:
    print("You Lose!")
elif RPSMoves[userChoiceInteger] == Paper and RPSMoves[computerChoice] == Rock:
    print("You Win!")

if RPSMoves[userChoiceInteger] == Scissors and RPSMoves[computerChoice] == Scissors:
    print("Tie!")
elif RPSMoves[userChoiceInteger] == Scissors and RPSMoves[computerChoice] == Rock:
    print("You Lose!")
elif RPSMoves[userChoiceInteger] == Scissors and RPSMoves[computerChoice] == Paper:
    print("You Win!")


