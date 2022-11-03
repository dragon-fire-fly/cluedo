from tabulate import tabulate


class Scorecard:
    def __init__(self, scorecard: list[list[str]]):
        self.scorecard = scorecard

    def show_scorecard(self) -> None:
        """
        Returns the scorecard as a table
        """
        print(tabulate(self.scorecard, tablefmt="fancy_grid", stralign="center"))

    def update_scorecard(self, character: str, search_card: str) -> None:
        """
        Takes the shown card and the character who showed it and updates the
        scorecard in the position of the intersect between that card and
        character.
        """
        # What's the index of the character who showed the card?
        char_num = self.scorecard[0].index(character)

        # What's the index of the list that contains the search card?
        list_index = 0
        for list in self.scorecard[1:]:
            if search_card in list:
                list_index = self.scorecard.index(list)

        # Add a cross in the appropriate place
        self.scorecard[list_index][char_num] = "x"
