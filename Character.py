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
        #Load player base information
        self.maxhealth = self.playerfile['maxhealth'][self.match].values[0]
        self.maxmana = self.playerfile['maxmana'][self.match].values[0]
        self.attack = self.playerfile['attack'][self.match].values[0]
        self.defense = self.playerfile['defense'][self.match].values[0]
        self.speed = self.playerfile['speed'][self.match].values[0]
        self.fire_enhance = self.playerfile['fire_enhance'][self.match].values[0]
        self.water_enhance = self.playerfile['water_enhance'][self.match].values[0]
        self.air_enhance = self.playerfile['air_enhance'][self.match].values[0]
        self.earth_enhance = self.playerfile['earth_enhance'][self.match].values[0]
        self.light_enhance = self.playerfile['light_enhance'][self.match].values[0]
        self.dark_enhance = self.playerfile['dark_enhance'][self.match].values[0]
        self.fire_resist = self.playerfile['fire_resist'][self.match].values[0]
        self.water_resist = self.playerfile['water_resist'][self.match].values[0]
        self.air_resist = self.playerfile['air_resist'][self.match].values[0]
        self.earth_resist = self.playerfile['earth_resist'][self.match].values[0]
        self.light_resist = self.playerfile['light_resist'][self.match].values[0]
        self.dark_resist = self.playerfile['dark_resist'][self.match].values[0]
        self.skill = self.playerfile['skill'][self.match].values[0]

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
        #load monster base information
        self.maxhealth = self.monsterfile['maxhealth'][self.match].values[0]
        self.attack = self.monsterfile['attack'][self.match].values[0]
        self.defense = self.monsterfile['defense'][self.match].values[0]
        self.speed = self.monsterfile['speed'][self.match].values[0]
        self.fire_enhance = self.monsterfile['fire_enhance'][self.match].values[0]
        self.water_enhance = self.monsterfile['water_enhance'][self.match].values[0]
        self.air_enhance = self.monsterfile['air_enhance'][self.match].values[0]
        self.earth_enhance = self.monsterfile['earth_enhance'][self.match].values[0]
        self.light_enhance = self.monsterfile['light_enhance'][self.match].values[0]
        self.dark_enhance = self.monsterfile['dark_enhance'][self.match].values[0]
        self.fire_resist = self.monsterfile['fire_resist'][self.match].values[0]
        self.water_resist = self.monsterfile['water_resist'][self.match].values[0]
        self.air_resist = self.monsterfile['air_resist'][self.match].values[0]
        self.earth_resist = self.monsterfile['earth_resist'][self.match].values[0]
        self.light_resist = self.monsterfile['light_resist'][self.match].values[0]
        self.dark_resist = self.monsterfile['dark_resist'][self.match].values[0]
        self.skill = self.monsterfile['skill'][self.match].values[0]
        self.taunt = self.monsterfile['taunt'][self.match].values[0]
        self.flavour_text = self.monsterfile['flavour_text'][self.match].values[0]
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
