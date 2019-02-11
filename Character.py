from database import Database
db = Database()
from battle import Combat

class Player: #class to interact with player objects
    def __init__(self, name):
        self.id = 1 #placeholder until save and load function
        #find match for correct player ID.
        self.match = db.PlayerInfoDatabase['id'] == self.id
        #establish key values by pulling from database.
        self.name = db.PlayerInfoDatabase['name'][self.match].values[0]
        #Load player stat information
        self.maxhealth = db.PlayerStatDatabase['maxhealth'][self.match].values[0]
        self.maxmana = db.PlayerStatDatabase['maxmana'][self.match].values[0]
        self.health = self.maxhealth
        self.mana = self.maxmana
        self.attack = db.PlayerStatDatabase['attack'][self.match].values[0]
        self.defense = db.PlayerStatDatabase['defense'][self.match].values[0]
        self.speed = db.PlayerStatDatabase['speed'][self.match].values[0]
        self.fire_enhance = db.PlayerStatDatabase['fire_enhance'][self.match].values[0]
        self.water_enhance = db.PlayerStatDatabase['water_enhance'][self.match].values[0]
        self.air_enhance = db.PlayerStatDatabase['air_enhance'][self.match].values[0]
        self.earth_enhance = db.PlayerStatDatabase['earth_enhance'][self.match].values[0]
        self.light_enhance = db.PlayerStatDatabase['light_enhance'][self.match].values[0]
        self.dark_enhance = db.PlayerStatDatabase['dark_enhance'][self.match].values[0]
        self.fire_resist = db.PlayerStatDatabase['fire_resist'][self.match].values[0]
        self.water_resist = db.PlayerStatDatabase['water_resist'][self.match].values[0]
        self.air_resist = db.PlayerStatDatabase['air_resist'][self.match].values[0]
        self.earth_resist = db.PlayerStatDatabase['earth_resist'][self.match].values[0]
        self.light_resist = db.PlayerStatDatabase['light_resist'][self.match].values[0]
        self.dark_resist = db.PlayerStatDatabase['dark_resist'][self.match].values[0]
        #Load player skill and inventory information
        self.equipped_skill_id = db.PlayerSkillDatabase['equipped_skill'][self.match].values[0]
        self.equipped_item_id = db.PlayerInventoryDatabase['equipped_item'][self.match].values[0]

    def __repr__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self):
        pass

class Monster: #class to interact with monster objects
    def __init__(self, name):
        self.name = name
        #returns True for rows that fulfill the criterias and False for others. There should always be one true since monster name is unique
        self.match = db.BestiaryDatabase['name'] == name
        #load monster base information
        self.maxhealth = db.BestiaryDatabase['maxhealth'][self.match].values[0]
        self.attack = db.BestiaryDatabase['attack'][self.match].values[0]
        self.defense = db.BestiaryDatabase['defense'][self.match].values[0]
        self.speed = db.BestiaryDatabase['speed'][self.match].values[0]
        self.fire_enhance = db.BestiaryDatabase['fire_enhance'][self.match].values[0]
        self.water_enhance = db.BestiaryDatabase['water_enhance'][self.match].values[0]
        self.air_enhance = db.BestiaryDatabase['air_enhance'][self.match].values[0]
        self.earth_enhance = db.BestiaryDatabase['earth_enhance'][self.match].values[0]
        self.light_enhance = db.BestiaryDatabase['light_enhance'][self.match].values[0]
        self.dark_enhance = db.BestiaryDatabase['dark_enhance'][self.match].values[0]
        self.fire_resist = db.BestiaryDatabase['fire_resist'][self.match].values[0]
        self.water_resist = db.BestiaryDatabase['water_resist'][self.match].values[0]
        self.air_resist = db.BestiaryDatabase['air_resist'][self.match].values[0]
        self.earth_resist = db.BestiaryDatabase['earth_resist'][self.match].values[0]
        self.light_resist = db.BestiaryDatabase['light_resist'][self.match].values[0]
        self.dark_resist = db.BestiaryDatabase['dark_resist'][self.match].values[0]
        self.skill = db.BestiaryDatabase['skill'][self.match].values[0]
        self.taunt = db.BestiaryDatabase['taunt'][self.match].values[0]
        self.flavour_text = db.BestiaryDatabase['flavour_text'][self.match].values[0]
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
#print("What is your name?")
#name = input(">>>> ")
name = 'placeholder'
PlayerIG = Player(name)
fight = Combat(PlayerIG, Monster('Goblin Soldier'))
fight = Combat(PlayerIG, Monster('Goblin Soldier'))
