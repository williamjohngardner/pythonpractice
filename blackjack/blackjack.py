from hand import Hand

class BlackJack:

    def __init__(self):
        self.player = []
        self.dealer = []
        self.player_score = []
        self.dealer_score = []
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
        single = Hand().deal_card()
        print(single)
        return single

    def p_score(self):
        numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
        faces = ['J', 'Q', 'K', 'j', 'q', 'k']
        ace = ['a', 'A']
        for card in self.player:
            if card[0] in numbers:
                self.player_score.append(int(card[0]))
            elif card[0] in faces:
                self.player_score.append(10)
            elif card[0] in ace:
                if sum(self.player_score) <= 10:
                    self.player_score.append(11)
                else:
                    self.player_score.append(1)
        sum(self.player_score)
        print(sum(self.player_score))

    def d_score(self):
        numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
        faces = ['J', 'Q', 'K', 'j', 'q', 'k']
        ace = ['a', 'A']
        for card in self.dealer:
            if card[0] in numbers:
                self.dealer_score.append(int(card[0]))
            elif card[0] in faces:
                self.dealer_score.append(10)
            elif card[0] in ace:
                if sum(self.dealer_score) <= 10:
                    self.dealer_score.append(11)
                else:
                    self.dealer_score.append(1)
        sum(self.dealer_score)
        print(sum(self.dealer_score))

    def game_play(self):
        self.dealer = self.dealer_hand()
        self.player = self.player_hand()
        print("Welcome to Marginally Awesome Blackjack!")
        print("Dealer Hand: " + str(self.dealer))
        print("Player Hand: " + str(self.player))
        while self.max_hand < 5:
            hit_stand = input("Do you want to [H]it or [S]tand?").lower()
            self.max_hand += 1
            if hit_stand == "h":
                new_card = self.single_card()
                self.player.append(new_card)
                print(str(self.player))
                continue
            elif hit_stand == "s":
                self.p_score()
                break
        else:
            self.p_score()

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
