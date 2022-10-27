# import built in modules
import random
from re import A


class Cards:
    def __init__(
        self, cards: list[list[str]],
        dealt_cards: dict[str, list],
        murder_envelope,
            ):
        self.cards = cards
        self.dealt_cards = dealt_cards
        self.murder_envelope = murder_envelope

    def shuffle_cards(self, card_deck: list[list[str]]) -> list[list[str]]:
        random.shuffle(card_deck)
        return card_deck

    def deal_cards(self):
        cards = self.shuffle_cards(self.cards)

        # Pop one suspect, one weapon and one room
        self.murder_envelope = cards[0].pop(), cards[1].pop(), cards[2].pop()

        # mix the remaining cards together
        remaining_cards = []
        for i in range(3):
            for card in cards[i]:
                remaining_cards.append(card)
        shuffled_cards = self.shuffle_cards(remaining_cards)

        # Deal to each of the six suspects
        while shuffled_cards:
            for key in self.dealt_cards.keys():
                random_card = shuffled_cards.pop()
                self.dealt_cards[key].append(random_card)

    def check_murder_envelope(self, player_guess):
        for cards in player_guess:
            if \
                    self.murder_envelope[0] == player_guess[0] and \
                    self.murder_envelope[1] == player_guess[1] and \
                    self.murder_envelope[2] == player_guess[2]:
                return "Congratulations, you correctly guessed the cards! \
                    You win!"
            else:
                correct_cards = ""
                for cards in self.murder_envelope:
                    correct_cards += cards

                return f"Sorry, that was the wrong guess. The correct cards\
                    were: {correct_cards}. You lose!"
