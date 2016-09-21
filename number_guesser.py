# Number Guesser v 2.0
# September 21, 2016
# Bill Gardner
import random
import os
import sys

class NumberGuesser:

    def __init__(self):
        self.number = random.randint(1, 100)
        self.counter = 0

        print("""    *****************************
            *****************************
            *****************************
            ****RANDOM NUMBER GUESSER****
            *****************************
            *****************************
            *****************************""")

    def playagain():
        playagain = input("Would you like to play again?: ").lower()

        if playagain == "y":
            os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
        else:
            print("Fine!!! Cheater.")
            exit()

    def game_play(self):
        while self.guess != self.number:
            if self.guess > self.number:
                print("Your guess was too high. Guess again.")
                self.counter += 1
                guess = int(input("PICK ANOTHER NUMBER BETWIXT 1 & 100: "))

            elif self.guess < self.number:
                print("Your guess was too low. Guess again.")
                self.counter += 1
                guess = int(input("PICK ANOTHER NUMBER BETWIXT 1 & 100: "))

            else:
                break

        if guess == number:
            print("Your guess was correct. You must have cheated. Cheater.")
            print("It took you " + str(counter) + " guesses to guess the number.  Cheater.")
            playagain()

    def initial_guess(self):
        if self.number == self.guess:
            self.counter += 1
            print("You guessed correctly on the first try.  Good job, Cheater.")
            print("It took you " + str(self.counter) + " guesses to guess the number.  Cheater.")
            playagain()
        else:
            game_play()

    def guess(self):
        self.guess = int(input("PICK A NUMBER BETWIXT 1 & 100: "))
        initial_guess()

game = NumberGuesser()
game.guess()
