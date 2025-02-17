import Player
import json

class Deck:
    def __init__(self, killer_grid: []):
        self.killer_grid: [] = killer_grid

    def set_killers(self, killers: []):
        self.killer_grid: [] = killers

    def import_deck(self):
        """TODO: method to import Bingo Deck from json file"""

    def export_deck(self):
        """TODO: method to import Bingo Deck from json file"""

    def has_duplicate_killers(self):
        """Check whether deck has a killer more than once"""
        killer_set = set()
        for row in self.killer_grid:
            for killer in row:
                if killer in killer_set:
                    return True
                killer_set.add(killer)
        return False
