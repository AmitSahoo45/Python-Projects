import random


class SnakeWaterGun:
    def __init__(self):
        self.ply1 = None
        self.ply2 = None
        self.choice = True

    def game(self):
        if self.ply1 == self.ply2:
            return None

        if self.ply1 == 's':
            if self.ply2 == 'w':
                return False
            elif self.ply2 == 'g':
                return True

        if self.ply1 == 'w':
            if self.ply2 == 'g':
                return False
            elif self.ply2 == 's':
                return True

        if self.ply1 == 'g':
            if self.ply2 == 's':
                return False
            elif self.ply2 == 'w':
                return True

        else:
            return "Invalid"

    def play(self):
        while self.choice:
            randNo = random.randint(1, 3)
            if randNo == 1:
                self.ply1 = 's'
            elif randNo == 2:
                self.ply1 = 'w'
            else:
                self.ply1 = 'g'

            print(
                "Computer's Turn to choose Snake(s), Water(w) or Gun(g).\nComputer has chosen.\n")
            self.ply2 = input(
                "Player's Turn: Snake(s), Water(w) or Gun(g)? : ")
            res = self.game()
            print(
                f"Computer chose {self.ply1} and Player chose {self.ply2}.\n")
            if res == None:
                print("The game is a tie!")
            elif res:
                print("You Win!")
            elif not res:
                print("You Lose!")
            else:
                print("Invalid Input")
            self.choice = input("Do you want to play again? (y/n) : ")
            if self.choice == 'y':
                self.choice = True
            else:
                self.choice = False
                print("Thank you for playing!")
