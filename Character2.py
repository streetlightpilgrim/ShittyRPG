import os
import sys
import pandas as pd
import csv

BestiaryDatabase = 'bestiary.csv' #bestiary is the database for monster information.
outputleft = "***          "
outputright = "          ***"
user_input = ">>>"

class Player:
    def __init__(self, name):
        self.name = name
        self.basestat = {'maxhealth': 10, 'maxmana': 10, 'str': 5, 'def': 5, 'spd': 5, \
                        'resf': 0, 'resa': 0, 'resw': 0, 'rese': 0, 'resl': 0, 'resd': 0}
        self.equipstat = {'maxhealth': 0, 'maxmana': 0, 'str': 0, 'def': 0, 'spd': 0, \
                        'resf': 0, 'resa': 0, 'resw': 0, 'rese': 0, 'resl': 0, 'resd': 0}
        self.statuseffect = []
        self.health = self.basestat.get('maxhealth')
        self.mana = self.basestat.get('maxmana')
        self.skill = []
        self.occupation = {'alchemy': 0, 'barter': 0, 'dungeon': 0}
        self.reputation = {'guild': 0, 'association': 0, 'community': 0}
        self.relationship = {}
        print(self.name)

class Monster: #class to interact with monster objects.
    def __init__(self, name):
        #establish connection with monster database.
        monsterfile = pd.read_csv(BestiaryDatabase, sep = ',', header = 0, encoding = 'utf-8')
        #returns True for rows that fulfill the criterias and False for others. There should always be one true since monster name is unique.
        match = monsterfile['name'] == name
        self.name = name
        #return value from monster database using lookup of the appropriate header and what was true on match. Again should always only be one cell value returned since monster name is unique.
        self.id = monsterfile['id'][match].values[0]
        self.maxhealth = monsterfile['maxhealth'][match].values[0]
        self.maxmana = monsterfile['maxmana'][match].values[0]
        self.attack = monsterfile['attack'][match].values[0]
        self.defense = monsterfile['defense'][match].values[0]
        self.speed = monsterfile['speed'][match].values[0]
        self.fire_enhance = monsterfile['fire_enhance'][match].values[0]
        self.water_enhance = monsterfile['water_enhance'][match].values[0]
        self.air_enhance = monsterfile['air_enhance'][match].values[0]
        self.earth_enhance = monsterfile['earth_enhance'][match].values[0]
        self.light_enhance = monsterfile['light_enhance'][match].values[0]
        self.dark_enhance = monsterfile['dark_enhance'][match].values[0]
        self.fire_resist = monsterfile['fire_resist'][match].values[0]
        self.water_resist = monsterfile['water_resist'][match].values[0]
        self.air_resist = monsterfile['air_resist'][match].values[0]
        self.earth_resist = monsterfile['earth_resist'][match].values[0]
        self.light_resist = monsterfile['light_resist'][match].values[0]
        self.dark_resist = monsterfile['dark_resist'][match].values[0]
        self.skill = monsterfile['skill'][match].values[0]
        self.exp = monsterfile['exp'][match].values[0]
        self.gold = monsterfile['gold'][match].values[0]
        self.loot = monsterfile['loot'][match].values[0]
        self.kill_count = monsterfile['loot'][match].values[0]
        self.flavour_text = monsterfile['flavour_text'][match].values[0]
        self.discovered = monsterfile['discovered'][match].values[0]
        #establish health and mana which would be used in battles flexibly
        self.health = self.maxhealth
        self.mana = self.maxmana

    def __repr__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self):
        pass

def prefight(monster):
    player = PlayerIG
    print("{A}{T1} VS {T2}{Z}".format(A = outputleft, T1 = player.name, T2 = monster.name, Z = outputright))
    #fightturn(player, monster)
    fightplayerturn(player, monster)

def fightturncount(player, monster):
    pass

def fightplayerturn(player, monster):
    print("(1) Attack")
    print("(2) Defend")
    print("(3) Skills")
    print("(4) Invetory")
    print("(5) Inspect")
    print("(6) Run")
    print("(7) Help")
    option = input(user_input).lower()

    if option == "attack" or option == '1':
        playerattack(player, monster)
    elif option == "defend" or option == 2:
        playerdefend()
    elif option == "skills" or option == 3:
        skillsbattle()
    elif option == "inventory" or option == 4:
        iventorybattle()
    elif option == "inspect" or option == 5:
        inspectbattle()
    elif option == "run" or option == 6:
        runbattle()
    elif option == "help" or option == 7:
        helpbattle()
    else:
        fightplayerturn(player, monster)

def playerattack(player, monster):
    monster.health -= player.basestat['str']
    player.health -= monster.attack
    print(monster.health)
    print(player.health)
    fightcheck(player, monster)

def defend():
    pass
def skill():
    pass
def inventory():
    pass

def fightcheck(player, monster):
    if monster.health <= 0:
        print("You Win")
    fightplayerturn(player, monster)

#os.system('cls')
print("""
Welcome to my sh1tty RPG
""")
print("What is your name?")
name = input(">>>> ")
PlayerIG = Player(name)
prefight(Monster('Goblin Soldier'))
