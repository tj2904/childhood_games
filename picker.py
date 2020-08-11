# Version 2 - Prompts for a colour, then a number before giving a random direction
import time # To be able to sleep
import random # For number generation

def main():
    # Prompt for a colour - TODO: add validation
    colour = input("Please pick a Colour: ")
    print()
    # Print out the colour a letter per row, slowly
    for c in colour:
        print (str.upper(c) + "...")
        time.sleep(0.5)

    # Prompt for a number - TODO: add validation
    n = get_postive_int()
    print()
    # Count out slowly
    i = 0
    for i in range(1, n+1):
        print (i, end="")
        time.sleep(0.2)
        print(".", end="")
        time.sleep(0.2)
        print(".", end="")
        time.sleep(0.2)
        print(".", end="\n")
        i =+ 1

    # Generate a number at random
    final = random.randrange(1,8,1)
    #print("\nThe random number is: " + str(final))
    time.sleep(0.5)
    # Build suspense
    print ("\nI will now open the flap...", end="\n\n")
    time.sleep(2.0)
    # Return the instruction
    if (final == 1) or (final == 5):
        print(str.center("You must turn left.", 30))
    elif (final == 2) or (final == 6):
        print(str.center("You must turn right.", 30))
    elif (final == 3) or (final == 8):
        print(str.center("You must turn back.", 30))
    else:
        print(str.center("You must continue ahead.", 30))
    print()

# Prompt for a number between 1 and 8
def get_positive_int():
# If not between 1 and 8 ask again
    while True:
        n = get_int("\nNow choose a number between 1 and 8: ")
        if n in range(1, 9):
            break
    return n+1

main()
