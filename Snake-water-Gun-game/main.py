import random


def game(ply1, ply2):
    if ply1 == ply2:
        return None

    if ply1 == 's':
        if ply2 == 'w':
            return False
        elif ply2 == 'g':
            return True

    if ply1 == 'w':
        if ply2 == 'g':
            return False
        elif ply2 == 's':
            return True

    if ply1 == 'g':
        if ply2 == 's':
            return False
        elif ply2 == 'w':
            return True

    else:
        return "Invalid"


choice = True

while choice:
    randNo = random.randint(1, 3)
    if randNo == 1:
        ply1 = 's'
    elif randNo == 2:
        ply1 = 'w'
    else:
        ply1 = 'g'

    print("Computer's Turn to choose Snake(s), Water(w) or Gun(g).\nComputer has chosen.\n")
    ply2 = input("Player's Turn: Snake(s), Water(w) or Gun(g)? : ")
    res = game(ply1, ply2)
    print(f"Computer chose {ply1} and Player chose {ply2}.\n")
    if res == None:
        print("The game is a tie!")
    elif res:
        print("You Win!")
    elif not res:
        print("You Lose!")
    else:
        print("Invalid Input")
    choice = input("Do you want to play again? (y/n) : ")
    if choice == 'y':
        choice = True
    else:
        choice = False
        print("Thank you for playing!")
