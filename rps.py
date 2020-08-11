import random

# 1= Rock, 2= Paper, 3= Scissors
# add above to a dict so you can replace number with words in the sentence
moves = {1: "Rock", 2: "Paper", 3: "Scissors"}

#print(dict(moves)) debugging
#print()

user = int(input("Please make a choice. 1= Rock, 2= Paper, 3= Scissors: "))
print("\nYou have selected " + moves[user])
bot = random.randrange(1,3)
print("\nThe computer has chosen: " + moves[bot])
if (user == bot):
    print("\nIt's a draw!")
elif (user == 1) & (bot == 2):
    print("\nPaper covers Rock.\n Computer wins, unlucky...")
elif (user == 1) & (bot == 3):
    print("\nScissors are blunted by Rock.\n You win!")

elif (user == 2) & (bot == 1):
    print("\nPaper covers Rock.\n You win!")
elif (user == 2) & (bot == 3):
    print("\nScissors cut Paper.\n Computer wins, unlucky...")

elif (user == 3) & (bot == 1):
    print("\nScissors are blunted by Rock.\n Computer wins, unlucky...")
elif (user == 3) & (bot == 2):
    print("\nScissors cut Paper.\n You win!")
print()
