import numpy as np

values = np.random.randint(1,21)

input("Guess the number between 1 to 20...(Press Enter to start)")
chance = 0
chanceLeft = 3

while chance < 3 :
    guess = int(input("Enter the guessed number :"))

    if guess == values:
        print("Congratulations You Gussed The Right Number 🎉🎉")
        break

    else:
        print("Sorry..., Your guess is wrong.....😕,")
        chance = chance + 1
        chanceLeft = chanceLeft - 1
        print(f"You have Chance {chanceLeft} left")
else:
    print(f"GAME OVER ANSWER IS {values}")