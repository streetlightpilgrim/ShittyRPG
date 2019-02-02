from database import Database
db = Database()
import pandas as pd
from battle import Combat


class Player: #class to interact with player objects
    def __init__(self, name):
        self.id = 1 #placeholder until save and load function
        #establish connection with player database
        self.playerinfofile = pd.read_json(db.PlayerInfoDatabase, orient = 'records', encoding = 'utf-8')
        self.playerstatfile = pd.read_json(db.PlayerStatDatabase, orient = 'records', encoding = 'utf-8')
        self.playerskillfile = pd.read_json(db.PlayerSkillDatabase, orient = 'records', encoding = 'utf-8')
        self.playerinventoryfile = pd.read_json(db.PlayerInventoryDatabase, orient = 'records', encoding = 'utf-8')

        #find match for correct player ID.
        self.match = self.playerinfofile['id'] == self.id
        #establish key values by pulling from database.
        self.name = self.playerinfofile['name'][self.match].values[0]
        #Load player base information
        self.maxhealth = self.playerstatfile['maxhealth'][self.match].values[0]
        self.maxmana = self.playerstatfile['maxmana'][self.match].values[0]
        self.attack = self.playerstatfile['attack'][self.match].values[0]
        self.defense = self.playerstatfile['defense'][self.match].values[0]
        self.speed = self.playerstatfile['speed'][self.match].values[0]
        self.fire_enhance = self.playerstatfile['fire_enhance'][self.match].values[0]
        self.water_enhance = self.playerstatfile['water_enhance'][self.match].values[0]
        self.air_enhance = self.playerstatfile['air_enhance'][self.match].values[0]
        self.earth_enhance = self.playerstatfile['earth_enhance'][self.match].values[0]
        self.light_enhance = self.playerstatfile['light_enhance'][self.match].values[0]
        self.dark_enhance = self.playerstatfile['dark_enhance'][self.match].values[0]
        self.fire_resist = self.playerstatfile['fire_resist'][self.match].values[0]
        self.water_resist = self.playerstatfile['water_resist'][self.match].values[0]
        self.air_resist = self.playerstatfile['air_resist'][self.match].values[0]
        self.earth_resist = self.playerstatfile['earth_resist'][self.match].values[0]
        self.light_resist = self.playerstatfile['light_resist'][self.match].values[0]
        self.dark_resist = self.playerstatfile['dark_resist'][self.match].values[0]
        #self.skill = self.playerstatfile['skill'][self.match].values[0]

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
        self.monsterfile = pd.read_json(db.BestiaryDatabase, orient = 'records', encoding = 'utf-8')
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
