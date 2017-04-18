# Create a Card class, that has a color and a value
# Create a constructor for setting those values
# Card should be represented as string in this format:
# 9 Hearts
# Jack Diamonds
# Create a Deck class, that has a list of cards in it
# Create a constructor that takes a whole number as parameter
# The constructor should fill the list with the number of different cards using at least 4 different colors (except if the number given is smaller than four, than all cards should have different colors)
# We should be able to shuffle the deck, which randomly orders the cards
# We should be able to draw the top card which returns the drawn card and also removes it from the deck
# Deck should be represented as string in this format:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades
#****deck = Deck(12)
#****print(deck)
# Should print out:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades
#****top_card = deck.draw()
#****print(top_card)
#****print(deck)
# Should print out:
# Queen Spades
# 11 cards - 3 Clubs, 3 Diamonds, 3 Hearts, 2 Spades

import random


class Card():

    def __init__(self):
        self.color = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Deck():

    def __init__(self, number):
        self.number = number
        self.list_of_cards_generator()
        print(self.list_of_cards)
        self.shuffle_list_of_cards()
        print(self.shuffled_list)

    def list_of_cards_generator(self):
        self.list_of_cards = []
        self.card = ''
        for i in range(self.number):
            self.card = random.choice(card.value) + " " + random.choice(card.color)
            self.list_of_cards.append(self.card)
        return self.list_of_cards

    def draw_top_card(self):
        top_card = self.list_of_cards[0]
        self.list_of_cards = self.list_of_cards[1:]
        return top_card

    def shuffle_list_of_cards(self):
        self.shuffled_list = random.shuffle(self.list_of_cards)
        return self.shuffled_list

card = Card()
deck = Deck(12)
