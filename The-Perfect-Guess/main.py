import random


class thePerfectGame:
    def __init__(self, name):
        self.name = name
        self.chance = 5
        self.score = 0
        self.choice = True

    def game(self):
        if self.chance == 0:
            print("You have no more chances left.")
            return False
        else:
            self.chance -= 1
            randNo = random.randint(1, 10)
            if randNo == self.number:
                self.score += 1
                print("You guessed it right.")
                return True
            else:
                print("You guessed it wrong.")
                return False

    def play(self):
        print(f"Welcome {self.name} to the Perfect Game. You have 5 chances to guess the number. If you guess it right, you get 1 point. If you guess it wrong, you lose 1 chance. Let's start the game.")
        while self.choice:
            self.number = random.randint(1, 20)
            print(
                f"Guess a number between 1 and 20. You have {self.chance} chances.")
            while self.chance > 0:
                self.guess = int(input("Enter your guess: "))
                if self.guess == self.number:
                    self.score += 1
                    print("You guessed it right.")
                    break
                elif self.guess > self.number:
                    if self.guess - self.number <= 3:
                        print("You are close to the number. Guess a little lower.")
                    else:
                        print("You guessed it wrong. Guess a lower number.")
                elif self.guess < self.number:
                    if self.number - self.guess <= 3:
                        print("You are close to the number. Guess a little higher.")
                    else:
                        print("You guessed it wrong. Guess a higher number.")
                self.chance -= 1
            if self.chance == 0:
                print("You have no more chances left.")
            print(f"Your score is {self.score}.")
            self.choice = input("Do you want to play again? (y/n) : ")
            if self.choice == 'y':
                self.choice = True
                self.chance = 5
                self.score = 0
            else:
                self.choice = False
                print("Thank you for playing the game.")


if __name__ == "__main__":
    name = input("Enter your name: ")
    game = thePerfectGame(name)
    game.play()
