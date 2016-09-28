from hand import Hand

class BlackJack:

    def __init__(self):
        self.single = []
        self.player = []
        self.dealer = []
        self.max_hand = 2

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
        self.single = Hand().deal_card()
        print(self.single)
        return self.single

    def score(self):
        print("you're now in the score function")

    def game_play(self):
        dealer = self.dealer_hand()
        player = self.player_hand()
        print("Welcome to Marginally Awesome Blackjack!")
        print("Dealer Hand: " + str(dealer))
        print("Player Hand: " + str(player))
        while self.max_hand < 5:
            hit_stand = input("Do you want to [H]it or [S]tand?").lower()
            self.max_hand += 1
            if hit_stand == "h":
                new_card = self.single_card()
                player.append(new_card)
                print(str(player))
                continue
            elif hit_stand == "s":
                self.score()
                break
        else:
            self.score()

    def play_again(self):
        answer = input("Would you like to play again? Y or N").lower()
        if answer == 'y':
            os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
        else:
            print('Goodbye!')
            exit()

blackjack = BlackJack().game_play()
# single = BlackJack().single_card()
# player = BlackJack().player_hand()
# dealer = BlackJack().dealer_hand()
# print(single_card())
# blackjack.player
# blackjack.dealer_hand
# blackjack.single
