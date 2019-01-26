import pandas as pd
from battle import Combat

PlayerDatabase = 'playerinfo.csv' #playerinfo is the database for player stats
BestiaryDatabase = 'bestiary.csv' #bestiary is the database for monster information
SkillDatabase = 'skill.csv' #skill is the database for skill information
outputleft = "***          "
outputright = "          ***"
user_input = ">>>"

class Player:
    def __init__(self, name):
        self.id = 1 #placeholder until save and load function
        #establish connection with player database
        self.playerfile = pd.read_csv(PlayerDatabase, sep = ',', header = 0, encoding = 'utf-8')
        #find match for correct player ID.
        self.match = self.playerfile['id'] == self.id
        #establish key values by pulling from database.
        self.name = self.playerfile['name'][self.match].values[0]
        print(self.name)

    def __repr__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self):
        pass

class Monster: #class to interact with monster objects.
    def __init__(self, name):
        self.name = name
        #establish connection with monster database.
        self.monsterfile = pd.read_csv(BestiaryDatabase, sep = ',', header = 0, encoding = 'utf-8')
        #returns True for rows that fulfill the criterias and False for others. There should always be one true since monster name is unique.
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
Combat(PlayerIG, Monster('Goblin Soldier'), SkillDatabase)
