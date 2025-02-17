import Deck
import Player
import json

class Game:
    def __init__(self, json_data: str, bingo_id: int):
        """Loading bingo game and saves all Decks of players"""
        self.bingo_id: int = bingo_id
        self.players: list[Player] = []

    def load_players(self, json_data: str):
        """Create player object for all players of a bingo game"""
        """TODO: test method"""
        for bingo in json_data["bingos"]:
            if bingo["bingo_id"] == self.bingo_id:
                return [Player(player["player_id"], player["player_name"], player["player_deck"]) for player in bingo["players"]]
            return []
