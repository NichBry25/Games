import random

##### DICTIONARIES

cards = {
    "ace_spades":11, "ace_hearts": 11, "ace_diamonds": 11, "ace_clubs": 11,
    "two_spades":2, "two_hearts":2, "two_diamonds":2, "two_clubs":2,
    "three_spades": 3, "three_hearts": 3, "three_diamonds": 3, "three_clubs": 3,
    "four_spades":4, "four_hearts":4, "four_diamonds":4, "four_clubs":4,
    "five_spades":5, "five_hearts":5, "five_diamonds":5, "five_clubs":5,
    "six_spades":6, "six_hearts":6, "six_diamonds":6, "six_clubs":6,
    "seven_spades":7, "seven_hearts":7, "seven_diamonds":7, "seven_clubs":7,
    "eight_spades":8, "eight_hearts":8, "eight_diamonds":8, "eight_clubs":8,
    "nine_spades":9, "nine_hearts":9, "nine_diamonds":9, "nine_clubs":9,
    "ten_spades":10, "ten_hearts":10, "ten_diamonds":10, "ten_clubs":10,
    "jack_spades":10, "three_hearts":10, "three_diamonds":10, "three_clubs":10,
    "queen_spades":10, "queen_hearts":10, "queen_diamonds":10, "queen_clubs":10,
    "king_spades":10, "king_hearts":10, "king_diamonds":10, "king_clubs":10,
}

cards_not_played = {}
for card_played_or_not in cards:
    cards_not_played[card_played_or_not] = True

#Player Variables
card_picked_value_player = 0
list_of_player_cards = []

#Dealer Variables
dealer_value = 0
list_of_dealer_cards = []

##### CODE EXECUTION

class playing:
    def first_deal_out(self):
        global card_picked_value_player
        global list_of_player_cards
        random_card1 = random.choice(list(cards_not_played.items()))
        if cards_not_played[random_card1[0]] == True:
            card_picked1 = random_card1[0]
            list_of_player_cards.append(card_picked1)
            card_picked_value_player += cards[random_card1[0]]
            cards_not_played[random_card1[0]] = False
        else:
            self.rerun_first_deal_out()
        random_card2 = random.choice(list(cards_not_played.items()))
        if cards_not_played[random_card2[0]] == True:
            cards_picked2 = random_card2[0]
            list_of_player_cards.append(cards_picked2)
            card_picked_value_player += cards[random_card2[0]]
            cards_not_played[random_card2[0]] = False
        else:
            self.rerun_first_deal_out()
        print("--------------------------------------------------------------")
        print("You are getting dealt 2 cards!")
        print(f"You got {card_picked1} and {cards_picked2}!")
        print(f"The value in your hand is {card_picked_value_player}.")
        cards_not_played[random_card1[0]] = False
        cards_not_played[random_card2[0]] = False
        print("--------------------------------------------------------------")

    def first_deal_out_for_dealer(self):
        global dealer_value
        global card_picked_dealer2
        global random_card_dealer2
        global list_of_dealer_cards
        random_card_dealer1 = random.choice(list(cards_not_played.items()))
        if cards_not_played[random_card_dealer1[0]] == True:
            card_picked_dealer1 = random_card_dealer1[0]
            list_of_dealer_cards.append(card_picked_dealer1)
            dealer_value += cards[random_card_dealer1[0]]
            cards_not_played[random_card_dealer1[0]] = False
        else:
            self.rerun_first_deal_out()
        random_card_dealer2 = random.choice(list(cards_not_played.items()))
        if cards_not_played[random_card_dealer2[0]] == True:
            card_picked_dealer2 = random_card_dealer2[0]
            list_of_dealer_cards.append(card_picked_dealer2)
            cards_not_played[random_card_dealer2[0]] = False
        else:
            self.rerun_first_deal_out()

        print(f"The dealer got 2 cards. One of which is {card_picked_dealer1}.")
        print(f"The value in the dealer's hand is {dealer_value}.")
        
    def deal_card_again(self):
        print(f"You want another card!")
        global card_picked_value_player
        global list_of_player_cards
        random_card_new = random.choice(list(cards_not_played.items()))
        if cards_not_played[random_card_new[0]] == True:
            card_picked_new = random_card_new[0]
            list_of_dealer_cards.append(card_picked_new)
            card_picked_value_player += cards[random_card_new[0]]
            cards_not_played[random_card_new[0]] = False
        else:
            self.rerun_deal_card_again()
        random_card2 = random.choice(list(cards_not_played.items()))

        print(f"You got a {card_picked_new}!")
        print(f"Your total card value now is {card_picked_value_player}")
        
    def rerun_first_deal_out(self):
        self.first_deal_out()
    def rerun_first_deal_out_for_dealer(self):
        self.first_deal_out_for_dealer()
    def rerun_deal_card_again(self):
        self.deal_card_again()

    def end_the_game(self):
        global card_picked_value_player
        global card_picked_dealer2
        global random_card_dealer2
        global dealer_value
        dealer_value += cards[random_card_dealer2[0]]
        print("The game is ending.")
        print(f"Your cards' value are: {card_picked_value_player}")
        print("--------------------------------------------------------------")
        print(f"The dealer's hidden card is {card_picked_dealer2}.")
        print(f"The dealer's cards' value now are: {dealer_value}")
        
##### CODE EXECUTION

if __name__ == "__main__":
    gameplay = True
    player_and_dealer_playing = playing() #Creates an object from class playing().
    player_and_dealer_playing.first_deal_out()
    player_and_dealer_playing.first_deal_out_for_dealer()
    while gameplay == True:
        print("What do you want to do? ")
        print("[1] - Deal a card.")
        print("[2] - End the game.")
        option = int(input())
        match option:
            case 1:
                player_and_dealer_playing.deal_card_again()
                if card_picked_value_player > 21:
                    if "ace_spades" in list_of_player_cards or "ace_diamonds" in list_of_player_cards or "ace_hearts" in list_of_player_cards or "ace_clubs" in list_of_player_cards:
                        print("You have passed 21, but you have an ace. Pheww.")
                        print("Be careful.")
                        card_picked_value_player -= 10
                        print(f"Your value now is {card_picked_value_player}")
                        if "ace_spades" in list_of_player_cards:
                            list_of_player_cards.remove("ace_spades")
                        if "ace_diamonds" in list_of_player_cards:
                            list_of_player_cards.remove("ace_diamonds")
                        if "ace_hearts" in list_of_player_cards:
                            list_of_player_cards.remove("ace_hearts")
                        if "ace_clubs" in list_of_player_cards:
                            list_of_player_cards.remove("ace_clubs")
                    else:
                        print(f"Your cards are now at {card_picked_value_player}")
                        print("You busted! Try again.")
                        gameplay = False
            case 2:
                player_and_dealer_playing.end_the_game()
                if "ace_spades" in list_of_player_cards or "ace_diamonds" in list_of_player_cards or "ace_hearts" in list_of_player_cards or "ace_clubs" in list_of_player_cards:
                    dealer_value -= 10
                if dealer_value > card_picked_value_player:
                    print("You lose. Try again.")
                elif dealer_value < card_picked_value_player:
                    print("YOU WON!")
                else:
                    print("You try.")
                gameplay = False