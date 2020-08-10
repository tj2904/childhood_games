import random

""""
A simple program that prompts a user to guess a random number and gives clues along the way and a guess countat the end.
""""

# Get random number to be guessed
number = random.randrange(1,1001)
# print(number) # For debugging

# Set guess counter & initial guess value
guess_count = 0
guess = 0

# Prompt the user for a guess and respond with a higher or lower answer while incorrect
while (guess != number):
    if (guess_count == 0):
        guess = int(input("Hi, wanna play a game? \nI've thought of a number between 1 and 1000, can you guess it? "))
        guess_count += 1
    elif (guess < number):
        guess = int(input("Nope, my number is higher...\nTry again: "))
        guess_count += 1
    elif (guess > number):
        guess = int(input("Narh, lower than that...\nTry again: "))
        guess_count += 1

# Congratulate the user when the guess is correct
if (guess == number):
    print("\nGood work, you've guessed it!")
    print("\tYou took " + str(guess_count) + " goes to get it.\n")
