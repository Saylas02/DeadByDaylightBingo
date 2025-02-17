class Player:
    def __init__(self, player_id: int, player_name: str, player_deck: list):
        self.player_id: int = player_id
        self.player_name: str = player_name
        self.player_deck: list = player_deck

    def has_bingo(self) -> bool:
        """Checks whether player has bingo"""
        """TODO: testing"""
        # check rows
        for row in self.player_deck:
            if all(killer["used"] for killer in row):
                return True

        # check columns
        for col in range(len(self.player_deck[0])):
            if all(row[col]["used"] for row in self.player_deck):
                return True

        # main diagonal
        if all(self.player_deck[i][i]["used"] for i in range(len(self.player_deck))):
            return True

        # off diagonal
        if all(self.player_deck[i][len(self.player_deck) - 1 - i]["used"] for i in range(len(self.player_deck))):
            return True

        return False