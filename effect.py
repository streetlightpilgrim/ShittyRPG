from database import Database
db = Database()
import pandas as pd

class Effect: #class to interact with effect of skills, attributes and items
    def __init__(self, id, initiator, bystander, battleflow):
        #transfer Player, Monster and Battleflow class objects to Effect class so it can be referred to dynamically
        self.id = id
        self.initiator = initiator
        self.bystander = bystander
        self.battleflow = battleflow

    def instant(self):
        #instants are activations that happen immediately after casting
        exec(self.skillfile['instant'][self.match].values[0])

    def persist(self):
        #persists are activations that happen in a different phase after casting
        exec(self.skillfile['persist'][self.match].values[0])

    def deactivation(self):
        #deactivations are activations that happen before the effect class object is deleted from Battleflow
        exec(self.skillfile['deactivation'][self.match].values[0])

class Skill(Effect): #class to interact with skill objects
    def __init__(self, id, initiator, bystander, battleflow):
        super().__init__(id, initiator, bystander, battleflow)
        #establish connection with skill database
        self.skillfile = pd.read_json(db.SkillDatabase, orient = 'records', encoding = 'utf-8')
        #returns True for rows that fulfill the criterias and False for others
        self.match = self.skillfile['id'] == self.id
        self.name = self.skillfile['name'] == self.id
        #load skill information
        if self.skillfile['target'][self.match].values[0] == 'bystander':
            self.target = self.bystander
        elif self.skillfile['target'][self.match].values[0] == 'initiator':
            self.target = self.initiator
        print(self.target.name)
        self.expirycounter = int(self.skillfile['expirycounter'][self.match].values[0])
        self.buff = bool(self.skillfile['buff'][self.match].values[0])
        self.stackable = bool(self.skillfile['stackable'][self.match].values[0])
        self.startturnactivation = bool(self.skillfile['startturnactivation'][self.match].values[0])
        self.endturnactivation = bool(self.skillfile['endturnactivation'][self.match].values[0])
        self.battleflow.execute(self)

    def instant(self):
        super().instant()

    def persist(self):
        super().persist()

    def deactivation(self):
        super().deactivation()

class BattleItem(Effect): #class to interact with inventory objects
    def __init__(self, name, initiator, bystander, battleflow):
        super().__init__(name, initiator, bystander, battleflow)
        #establish connection with skill database
        self.battleitemfile = pd.read_json(db.BattleItemDatabase, orient = 'records', encoding = 'utf-8')
        #returns True for rows that fulfill the criterias and False for others. There should always be one true since monster name is unique
        self.match = self.battleitemfile['name'] == name
        #load skill information
        if self.battleitemfile['target'][self.match].values[0] == 'bystander':
            self.target = self.bystander
        elif self.battleitemfile['target'][self.match].values[0] == 'initiator':
            self.target = self.initiator
        self.expirycounter = self.battleitemfile['expirycounter'][self.match].values[0]
        self.buff = self.battleitemfile['buff'][self.match].values[0]
        self.stackable = self.battleitemfile['stackable'][self.match].values[0]
        self.startturnactivation = self.battleitemfile['startturnactivation'][self.match].values[0]
        self.endturnactivation = self.battleitemfile['endturnactivation'][self.match].values[0]

class Battleflow: #class to handle effect activations
    def __init__(self):
        #list to contain executions from skills, attributes and items
        self.executions = []

    def execute(self, execution):
        #add executions to list to be tracked
        self.executions.append(execution)

    def onstartturn(self, initiator):
        #effects activated at start of target turn
        for execution in self.executions:
            #activate persist effect if counter > 0
            if execution.startturnactivation == True and execution.expirycounter > 0 and execution.target == initiator:
                execution.persist()
                execution.expirycounter -= 1
            #delete execution if counter = 0
            if execution.expirycounter <= 0:
                execution.deactivation()
                self.executions.remove(execution)

    def onendturn(self, initiator):
        #effects activated at end of target turn
        for execution in self.executions:
            #activate persist effect if counter > 0
            if execution.endturnactivation == True and execution.expirycounter > 0 and execution.target == initiator:
                execution.persist()
                execution.expirycounter -= 1
            #delete execution if counter = 0
            if execution.expirycounter <= 0:
                execution.deactivation
                self.executions.remove(execution)
