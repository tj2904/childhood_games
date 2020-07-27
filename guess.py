import random

# Get random number to be guessed
number = random.randrange(1,1001)
# print(number) # For debugging

# Set guess counter & initial guess value
guess_count = 0
guess = 0

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

if (guess == number):
    print("\nGood work, you've guessed it!")
    print("You took " + str(guess_count) + " goes to get it.\n")