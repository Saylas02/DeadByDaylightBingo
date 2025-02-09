class Player:
    def __init__(self, name: str, deck: [], balance: int):
        self.name: str = name
        self.deck: [] = deck
        self.balance: int = balance

    def set_name(self , name: str):
        self.name: str = name

    def get_name(self):
        return self.name

    def set_deck(self, deck: []):
        self.deck: [] = deck

    def get_deck(self):
        return self.deck

    def set_balance(self, balance: int):
        self.balance: int = balance
