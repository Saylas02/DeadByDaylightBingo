import Player
import json

class Deck:
    def __init__(self, killer_grid: []):
        self.killer_grid: [] = killer_grid

    def set_killers(self, killers: []):
        self.killer_grid: [] = killers

    @staticmethod
    def import_deck(json_data: str, bingo_id: int, player_id: int):
        """TODO: method to import Bingo Deck from json file"""
        for bingo in json_data["bingos"]:
            if bingo["bingo_id"] == bingo_id:
                for player in bingo["players"]:
                    killer_grid = [[entry["killer"] for entry in row] for row in player["deck"]]
                    return Deck(killer_grid)
        return None

    @staticmethod
    def export_deck(self):
        """TODO: method to import Bingo Deck from json file"""

    def has_duplicate_killers(self) -> bool:
        """Check whether deck has a killer more than once"""
        killer_set = set()
        for row in self.killer_grid:
            for killer in row:
                if killer in killer_set:
                    return True
                killer_set.add(killer)
        return False
