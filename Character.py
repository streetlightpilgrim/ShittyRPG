from database import Database
db = Database()
import pandas as pd
from battle import Combat


class Player: #class to interact with player objects
    def __init__(self, name):
        self.id = 1 #placeholder until save and load function
        #establish connection with player database
        self.playerfile = pd.read_csv(db.PlayerDatabase, sep = ',', header = 0, encoding = 'utf-8')
        #find match for correct player ID.
        self.match = self.playerfile['id'] == self.id
        #establish key values by pulling from database.
        self.name = self.playerfile['name'][self.match].values[0]

    def __repr__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self):
        pass

class Monster: #class to interact with monster objects
    def __init__(self, name):
        self.name = name
        #establish connection with monster database
        self.monsterfile = pd.read_csv(db.BestiaryDatabase, sep = ',', header = 0, encoding = 'utf-8')
        #returns True for rows that fulfill the criterias and False for others. There should always be one true since monster name is unique
        self.match = self.monsterfile['name'] == name

    def __repr__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self):
        pass

#os.system('cls')
print("""
Welcome to my sh1tty RPG
""")
print("What is your name?")
name = input(">>>> ")
PlayerIG = Player(name)
Combat(PlayerIG, Monster('Goblin Soldier'))
