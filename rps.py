import random

# 1= Rock, 2= Paper, 3= Scissors
# add above to a dict so you can replace number with words in the sentence
moves = {1: "Rock", 2: "Paper", 3: "Scissors"}

print(dict(moves))
print()
user = int(input("Please make a choice. 1= Rock, 2= Paper, 3= Scissors: "))
print()
print("You have selected " + moves[user])
bot = random.randrange(1,3)
print()
print("The computer has chosen: " + moves[bot])
print()
if (user == bot):
    print("It's a draw!")
elif (user == 1) & (bot == 2):
    print("Paper covers Rock.\n Computer wins, unlucky...")
elif (user == 1) & (bot == 3):
    print("Scissors are blunted by Rock.\n You win!")

elif (user == 2) & (bot == 1):
    print("Paper covers Rock.\n You win!")
elif (user == 2) & (bot == 3):
    print("Scissors cut Paper.\n Computer wins, unlucky...")

elif (user == 3) & (bot == 1):
    print("Scissors are blunted by Rock.\n Computer wins, unlucky...")
elif (user == 3) & (bot == 2):
    print("Scissors cut Paper.\n You win!")
    print()