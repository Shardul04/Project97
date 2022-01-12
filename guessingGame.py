import random


number = random.randrange(1, 9)

chance=0

print("Number Gussing Game")
print("Guess a number between 1 to 9")

while chance < 5:
    guess = int(input("Enter your guess: "))
    chance = chance + 1

    if guess < number:
        print("Too low. Guess a number higher than ", guess)
        
    if guess > number:
        print("Too high. Guess a number lower than ", guess)

    if guess == number:
        print("Congratulation You Won!!!")
        break

    if not chance < 5:
        print("You Lose! The Number is ", number)