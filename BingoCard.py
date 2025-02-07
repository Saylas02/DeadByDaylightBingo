import json

class BingoCard:
    def __init__(self, player: str, values: str):
        """Create Bingo Card indexed by player"""
        arr_player, arr_values = player.split(','), values.split(',')

    def save_to_json(self, player: [], values: []):
        """Save Bingo Card indexed by player """
