import random


class Cards:
    def __init__(self, cards, dealt_cards):
        self.cards = cards
        self.dealt_cards = dealt_cards

    def shuffle_cards(self, card_deck):
        random.shuffle(card_deck)
        return card_deck
