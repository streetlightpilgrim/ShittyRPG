import pandas as pd

class Database(): #class to interact with database files
    def __init__(self):
        self.PlayerInfoDatabase = pd.read_json('playerinfo.json', orient = 'records', encoding = 'utf-8') #playerinfo is the database for player generic information
        self.PlayerStatDatabase = pd.read_json('playerstat.json', orient = 'records', encoding = 'utf-8') #playerstat is the database for player stats
        self.PlayerSkillDatabase = pd.read_json('playerskill.json', orient = 'records', encoding = 'utf-8') #playerskill is the database for player skills
        self.PlayerInventoryDatabase = pd.read_json('playerinventory.json', orient = 'records', encoding = 'utf-8') #playerinventory is the database for player inventory
        self.BestiaryDatabase = pd.read_json('bestiary.json', orient = 'records', encoding = 'utf-8') #bestiary is the database for monster information
        self.SkillDatabase = pd.read_json('skill.json', orient = 'records', encoding = 'utf-8') #skill is the database for skill information
        self.ItemDatabase = pd.read_json('item.json', orient = 'records', encoding = 'utf-8') #item is the database for item information
        #self.BattleItemDatabase = pd.read_json('battleitem.json', orient = 'records', encoding = 'utf-8') #battleitem is the database for battleitem information
