# Write your code here :-)
import random
secretNumber = random.randint(1, 100)

print("I am thinking of a number between 1 and 100.")

for guessesTaken in range(1,5):
    print("Take a guess!")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low. Try again.")
    elif guess > secretNumber:
        print("Your guess is too high. Try again")
    else:
        break

if guess == secretNumber:
    print("Congratulations!! You guessed the number in: " + str(guessesTaken) + "guesses!")
else:
    print("Nope. The number I was thinking of was: " + str(secretNumber))
