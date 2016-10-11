from hand import Hand
import os
import sys

class BlackJack:

    def __init__(self):
        self.player = []
        self.dealer = []
        self.player_score = []
        self.dealer_score = []
        self.numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.faces = ['1', 'J', 'Q', 'K', 'j', 'q', 'k']
        self.ace = ['a', 'A']
        self.max_hand = 2
        self.dealer_max_hand = 2

    def dealer_hand(self):
        dealer_card_1 = Hand().deal_card()
        dealer_card_2 = Hand().deal_card()
        self.dealer.append(dealer_card_1)
        self.dealer.append(dealer_card_2)
        return self.dealer

    def player_hand(self):
        player_card_1 = Hand().deal_card()
        player_card_2 = Hand().deal_card()
        self.player.append(player_card_1)
        self.player.append(player_card_2)
        return self.player

    def single_card(self):
        single = Hand().deal_card()
        # print(single)
        return single

    def p_score(self):
        for card in self.player:
            if card[0] in self.numbers:
                self.player_score.append(int(card[0]))
            elif card[0] in self.faces:
                self.player_score.append(10)
            elif card[0] in self.ace:
                if sum(self.player_score) <= 10:
                    self.player_score.append(11)
                else:
                    self.player_score.append(1)
        self.player_score = sum(self.player_score)
        print("Your Score Is: " + str(self.player_score))
        if self.player_score > 21:
            print("Busted!")
            self.play_again()
        else:
            self.game_score()
            return self.player_score

    def d_score(self):
        for card in self.dealer:
            if card[0] in self.numbers:
                self.dealer_score.append(int(card[0]))
            elif card[0] in self.faces:
                self.dealer_score.append(10)
            elif card[0] in self.ace:
                if sum(self.dealer_score) <= 10:
                    self.dealer_score.append(11)
                else:
                    self.dealer_score.append(1)
        self.dealer_score = sum(self.dealer_score)
        while self.dealer_max_hand < 5:
            self.dealer_max_hand += 1
            if self.dealer_score <= 17:
                new_card = self.single_card()
                self.dealer.append(new_card)
                print(str(self.dealer))
                continue
            else:
                break
        # else:
        #     self.p_score()
        print("The Dealer's Score is: " + str(self.dealer_score))
        if self.dealer_score > 21:
            print("Dealer busted! You win!")
            self.play_again()
        else:
            self.p_score()
            return self.dealer_score

    # # Here is the dealer's hand play.
    # def dealer_play(self):
    #     while self.dealer_max_hand < 5:
    #         self.dealer_max_hand += 1
    #         if self.dealer_score <= 17:
    #             new_card = self.single_card()
    #             self.dealer.append(new_card)
    #             print(str(self.dealer))
    #             continue
    #         else:
    #             self.p_score()
    #             break
    #     else:
    #         self.p_score()

    def game_score(self):
        if self.player_score == self.dealer_score:
            print("Huh.  It's a tie.")
        elif self.player_score > self.dealer_score:
            print("Congratulation!  You've Won!")
        elif self.dealer_score > self.player_score:
            print("Well shoot.  Ya've done went and lost.")
        self.play_again()

    def game_play(self):
        self.dealer = self.dealer_hand()
        self.player = self.player_hand()
        print("Welcome to Marginally Awesome Blackjack!")
        print("Dealer Hand: " + str(self.dealer))
        print("Player Hand: " + str(self.player))
        # if self.player[0] = Ace and 10 "Blackjack" Player Wins.
        # Here is the player hand play.
        while self.max_hand < 5:
            hit_stand = input("Do you want to [H]it or [S]tand?").lower()
            self.max_hand += 1
            if hit_stand == "h":
                new_card = self.single_card()
                self.player.append(new_card)
                print(str(self.player))
                continue
            elif hit_stand == "s":
                self.d_score()
                break
        else:
            self.d_score()

    def play_again(self):
        answer = input("Would you like to play again? Y or N").lower()
        if answer == 'y':
            os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
        else:
            print('Goodbye!')
            exit()

blackjack = BlackJack().game_play()
