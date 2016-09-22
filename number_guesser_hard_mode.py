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
        print(self.number)

    def guess(self):
        self.guess = int(input("PICK A NUMBER BETWIXT 1 & 100: "))
        self.initial_guess()

    def initial_guess(self):
        if self.number == self.guess:
            self.counter += 1
            print("You guessed correctly on the first try.  Good job, Cheater.")
            print("It took you " + str(self.counter) + " guesses to guess the number.  Cheater.")
            self.playagain()
        else:
            self.game_play()

    def game_play(self):
        while self.guess != self.number:
            if self.guess > self.number:
                print("Your guess was too high. Guess again.")
                if (self.guess - self.number) <= 5:
                    print("But your guess is very close... you must be cheating. Cheater.")
                self.counter += 1
                self.guess = int(input("PICK ANOTHER NUMBER BETWIXT 1 & 100: "))
                continue

            elif self.guess < self.number:
                print("Your guess was too low. Guess again.")
                if (self.number - self.guess) <= 5:
                    print("But your guess is very close... you must be cheating.  Cheater.")
                self.counter += 1
                self.guess = int(input("PICK ANOTHER NUMBER BETWIXT 1 & 100: "))
                continue

            else:
                break

        if self.guess == self.number:
            print("Your guess was correct. You must have cheated. Cheater.")
            print("It took you " + str(self.counter) + " guesses to guess the number.  Cheater.")
            self.playagain()

    def playagain(self):
        playagain = input("Would you like to play again?: ").lower()

        if playagain == "y":
            os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
        else:
            print("Fine!!! Cheater.")
            exit()

game = NumberGuesser()
game.guess()
game.initial_guess()
game.game_play()
game.playagain()
