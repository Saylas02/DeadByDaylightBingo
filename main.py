from discord import Game

import BingoCard

if __name__ == "__main__":
    values = 'Trapper, Wraith, Hillbilly, Nurse, Huntress, Shape, Hag, Doctor, Cannibal, Nightmare, Pig, Clown, Spirit, Legion, Plague, Ghost Face, Demogorgon, Oni, Deathslinger, Executioner, Blight, Twins, Trickster, Nemesis, Cenobite'
    player = 'Silas, Anna, Alex, Marcel'
    game = BingoCard.BingoCard(player, values)

