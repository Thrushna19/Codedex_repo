
# A game on random module
import random
'''
high = 100
low = 1

number = random.randint(low, high)
guesses = 0

while True:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guesses = guesses + 1
        guess = int(guess)
        if guess < number:
            print("Think high babe! Your guess is low")
        elif guess < low or guess > high:
            print(f"Babe! the guess should be between {low} and {high}")
        elif guess > number:
            print("Your standards are high babe! Your guess is too high")
        else:
            print("OMG! Your always correct queen!")
            break          
    else:
        print("Type a number babe")
print(f"The number was {number} good job!")
print(f"You took {guesses} to guess the number right")
    '''
'''
# Rock, paper, scissor game!

game = ("rock", "paper", "scissor")
choose = None
playing = True

while playing:

    computer = random.choice(game)
    choose = None
    print("----------------------")
    choose = input("Enter a choice (Rock, paper, scissor game)...(q to quit): ").lower()

    if choose == 'q':
        playing = False

    elif choose == computer:
        print(f"Computers choice: {computer}")
        print("Its a tie queen!")

    elif (choose == "rock" and computer == "scissor") or \
         (choose == "paper" and computer == "rock") or \
         (choose == "scissor" and computer == "paper"):
        print(f"Computers choice: {computer}")
        print("OMG! You won!! 🎉")

    elif choose not in game:
        print("Please choose rock, paper, scissor game")

    elif choose == 'q':
        print("Thanks for playing!")
        playing = False

    else:
        print(f"Computers choice: {computer}")
        print("You lost for now babe! Better luck next time.")
    '''
import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# PRINT VERTICALLY
# for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line)

# PRINT HORIZONTALLY
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    total += die
print(f"total: {total}")    