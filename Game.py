import Deck
import Player

class Game:
    def __init__(self, player: [], board: []):
        self.player: [] = player
        self.board: [] = board

    def set_player(self, player: []):
        self.player: [] = player

    def get_player(self) -> []:
        return self.player

    def set_board(self, board: []):
        self.board: [] = board

    def get_board(self) -> []:
        return self.board
