from tabulate import tabulate


class Scorecard:
    def __init__(self, scorecard):
        self.scorecard = scorecard

    def show_scorecard(self):
        '''
        Returns the scorecard as a table
        '''
        print(tabulate(self.scorecard, tablefmt="pretty"))
        # return tabulate(self.scorecard)

    def update_scorecard(self, character, search_card):
        '''
        Takes the shown card and the character who showed it and updates the
        scorecard in the position of the intersect between that card and
        character.
        '''
        # What's the index of the character who showed the card?
        char_num = self.scorecard[0].index(character)

        # What's the index of the list that contains the search card?
        list_index = 0
        for list in self.scorecard[1:]:
            if search_card in list:
                list_index = self.scorecard.index(list)

        # Add a cross in the appropriate place
        self.scorecard[list_index][char_num] = "x"

        # card_num = self.scorecard.index(search_card)

        # print(char_num)
        # print(list_index)
        # print(tabulate(self.scorecard, tablefmt="pretty"))


scorecard = [[
    " ",
    "Miss Scarlett",
    "Colonel Mustard",
    "Mrs White",
    "Reverend Green",
    "Mrs Peacock",
    "Professor Plum"
    ], [
        'Miss Scarlett',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Colonel Mustard',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Mrs White',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Reverend Green',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Mrs Peacock',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Professor Plum',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
    ], [
        'Rope',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Lead piping',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Candlestick',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Dagger',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Spanner',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Revolver',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
    ], [
        'Main Hall',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Dining Room',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Billiard Room',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Ball Room',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Library',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Conservatory',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Study',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Lounge',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Kitchen',  ' ',  ' ', ' ', ' ', ' ', ' '
    ]]

# scorecard_test = Scorecard(scorecard)

# scorecard_test.show_scorecard()

# char = "Miss Scarlett"
# char2 = "Colonel Mustard"
# char3 = "Mrs White"
# char4 = "Reverend Green"

# card = "Revolver"
# card2 = "Conservatory"
# card3 = "Dagger"
# card4 = "Kitchen"
# card5 = "Ball Room"
# card6 = "Mrs White"

# scorecard_test.update_scorecard(char, card)
# scorecard_test.update_scorecard(char2, card2)
# scorecard_test.update_scorecard(char3, card3)
# scorecard_test.update_scorecard(char4, card4)
# scorecard_test.update_scorecard(char3, card5)
# scorecard_test.update_scorecard(char2, card6)
