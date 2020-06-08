import random
import time
class Card():
    def __init__(self,rank,value,suit):
        self.rank=rank
        self.value=value
        self.suit=suit

    def display_card(self):
        #show the rank and suit of an individual cards
        print(self.rank +"of"+self.suit)

class Deck():
    #simulate a deck of 52 playing cards

    def __init__(self):
        #initialize deck attrivbutes
        #list to all future cards in the deck        
        self.cards=[]

    def build(self):
        #Build a deck consisting of 52 unique cards
        #info for all the crads in deck
        suits=['Hearts','Diamonds','Spades','Clubs']
        ranks={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
        '10':10,'J':10,'Q':10,'K':10,'A':11,}
        #Building the deck,creating 52 individual cards
        for suit in suits:
            for rank,value in ranks.items():
                card=Card(rank,value,suit)
                self.cards.append(card)

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_card(self):
        "remove a card from the deck"
        card=self.cards.pop()
        return card


class Player():
    def __init__(self):
        self.hand=[] #a ist to hold player card
        self.hand_value=0 #total value of player hand
        self.playing_hand=True# abool to track if the player is playing the hand


    def draw_hand(self,deck):
        for i in range(2):
            #Player must start with 2 cards in hand
            card=deck.deal_card()
            self.hand.append(card)


    def display_hand(self):
        "show the players hand"
        print("\nPlayer's hand")
        for card in self.hand:
            card.display_card()

    def hit(self,deck):
        "Give the player a new card"
        card=deck.deal_card()
        self.hand.append(card)


    def get_hand_value(self):
        "Computer the value of Player hand"
        self.hand_value=0
        ace_in_hand=False

        for card in self.hand:
            self.hand_value+=card.value
            #check for ace
            if card.rank=='A':
                ace_in_hand=True
        if self.hand_value >21 and ace_in_hand:
            self.hand_value-=10

        print("Total value:" +str(self.hand_value))
    
    def update_hand(self,deck):
        if self.hand_value<21:
            choice=input("would you like to hit(y/n)").lower()
            if choice=='y':
                self.hit(deck)
            else:
                self.playing_hand=False
        else:
            self.playing_hand=False

class Dealer():
    "must hit up to 17 and they must reveal first card"
    def __init__(self):
        self.hand=[]
        self.hand_value=0
        self.playing_hand=True

    def draw_hand(self,deck):
        for i in range(2):
            card=deck.deal_card()
            self.hand.append(card)
    
    def display_hand(self):
        "Show dealers hand one hand at a time"
        input("\n Press Enter to reveal dealer's hand.")
        for card in self.hand:
            card.display_card()
            time.sleep(1)

    def hit(self,deck):
        "dealer must hit until they hit 17"
        self.get_hand_value()
        #as long as hand value less gthan 17 dealer must hit
        while self.hand_value<17:
            card=deck.deal_card()
            self.hand.append(card)
            self.get_hand_value()
        print("\n Dealer is set with a total of " +str(len(self.hand))+ "cards")


    def get_hand_value(self):
        "Compute the value of the dealer hand"
         
        self.hand_value=0
        ace_in_hand=False

        for card in self.hand:
            self.hand_value+=card.value
            #check for ace
            if card.rank=='A':
                ace_in_hand=True
        if self.hand_value >21 and ace_in_hand:
            self.hand_value-=10

class Game():
    def __init__(self,money):
        self.money=int(money)
        self.bet=20
        self.winner=""   
    
    def set_bet(self):
        "Get user's bet"
        betting=True
        while betting:
            #Get a user's bet
            bet=int(input("What would you like to bet"))
            #BEt is too small,set to min vaue
            if bet < 20:
                bet=20
            if bet>self.money:
                print("Sorry you can't afford the bet")
            else:
                self.bet=bet
                betting=False

    def scoring(self,p_value,d_value):
        if p_value==21:
            print("You got BLACK JACK!!!! YOU WIN!!")
            self.winner='P'
        elif d_value==21:
            print("Dealer got BLACK JACK")
            self.winner='D'
        #Someone went over
        elif p_value>21:
            print("you went over .... you losoe")
            self.winner='D'    
        elif d_value>21:
            print("you went over .... you win")
            self.winner='P'    

        else:
            if p_value>d_value:
                print("dealer gets" +str(d_value)+ "YOU WIN")
                self.winner='P'
            elif d_value>p_value:
                print("Dealer gets" +str(d_value)+ "YOU LOOSE")
                self.winner='D'

            else:
                print("Dealer gets" +str(d_value)+ "IT'S A TIE")
                self.winner='tie'

    def payout(self):
        if self.winner=='P':
            self.money+=self.bet
        elif self.money=='D':
            self.money-=self.bet

    def display_money(self):
        print("Current Money $" +str(self.money))

    def display_money_and_bet(self):
        print("\nCurrent Money $" +str(self.money)+"\t\tCurrent Money:$" +str(self.bet))


print("WElcome to the Casino Blackjack APP")
print("minimum bet is 20$")

money=int(input("How much money are you willing to plahy today"))
game=Game(money)
playing=True
while playing:
    game_deck=Deck()
    game_deck.build()
    game_deck.shuffle_deck()

    player=Player()
    dealer=Dealer()

    game.display_money()
    game.set_bet()

    player.draw_hand(game_deck)
    dealer.draw_hand(game_deck)

    game.display_money_and_bet()
    print("The dealer is showing a " +dealer.hand[0].rank + "of" +dealer.hand[0].suit + ".")

    while player.playing_hand:
        player.display_hand()
        player.get_hand_value()
        player.update_hand(game_deck)

    dealer.hit(game_deck)
    dealer.display_hand()

    game.scoring(player.hand_value,dealer.hand_value)
    game.payout()

    if game.money<20:
        playing=False
        print("Sorry you ran out of money")

        








