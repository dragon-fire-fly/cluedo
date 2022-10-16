import random


class Cards:
    def __init__(self, cards, dealt_cards):
        self.cards = cards
        self.dealt_cards = dealt_cards

    def shuffle_cards(self, card_deck):
        random.shuffle(card_deck)
        return card_deck

    def deal_cards(self):
            cards = self.shuffle_cards(self.cards)

            # Pop one suspect, one weapon and one room
            murder_envelope = cards[0].pop(), cards[1].pop(), cards[2].pop()

            # mix the remaining cards together
            remaining_cards = []
            for i in range(3):
                for card in cards[i]:
                    remaining_cards.append(card)
            shuffled_cards = self.shuffle_cards(remaining_cards)
            print(shuffled_cards)

            # Deal to each of the six suspects
            while shuffled_cards:
                for key in self.dealt_cards.keys():
                    random_card = shuffled_cards.pop()
                    self.dealt_cards[key].append(random_card)

            return self.dealt_cards