import Player
import json

class Deck:
    def __init__(self, player_id: int, killer_grid: []):
        self.player_id: int = player_id
        self.killer_grid: [] = killer_grid

    def set_killers(self, killers: []):
        self.killer_grid: [] = killers

    def has_duplicate_killers(self) -> bool:
        """Check whether deck has a killer more than once"""
        killer_set = set()
        for row in self.killer_grid:
            for killer_entry in row:  # killer_entry ist ein Dictionary
                killer_name = killer_entry["killer"]  # Extrahiere nur den Killer-Namen
                if killer_name in killer_set:
                    return True
                killer_set.add(killer_name)
        return False

    @staticmethod
    def get_players_deck(json_data: str, bingo_id: int, player_id: int):
        """method to import Bingo Deck from json file"""
        for bingo in json_data["bingos"]:
            if str(bingo["bingo_id"]) == str(bingo_id):
                for player in bingo["players"]:
                    if str(player["player_id"]) == str(player_id):
                        return player["deck"]
        return None

    @staticmethod
    def export_deck(self):
        """TODO: method to import Bingo Deck from json file"""

#--------------Testing--------------#
# JSON-Datei laden
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Deck-Daten abrufen
player_id = 1
bingo_id = 1
deck_data = Deck.get_players_deck(json_data=data, bingo_id=bingo_id, player_id=player_id)

# Prüfen, ob das Deck existiert
if deck_data:
    # Deck-Instanz erstellen
    player_deck = Deck(player_id=player_id, killer_grid=deck_data)

    # Methode aufrufen
    if player_deck.has_duplicate_killers():
        print(f"Spieler {player_id} hat doppelte Killer im Deck!")
    else:
        print(f"Spieler {player_id} hat ein einzigartiges Deck.")
else:
    print(f"Kein Deck für Spieler {player_id} in Bingo {bingo_id} gefunden.")
#--------------End-of-Testing--------------#
