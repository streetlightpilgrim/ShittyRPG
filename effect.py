from database import Database
db = Database()
import pandas as pd

class Effect: #class to interact with effect of skills, attributes and items
    def __init__(self, name, initiator, bystander, battleflow):
        #transfer Player, Monster and Battleflow class objects to Effect class so it can be referred to dynamically
        self.name = name
        self.initiator = initiator
        self.bystander = bystander
        self.battleflow = battleflow

    def instant(self):
        #instants are activations that happen immediately after casting
        pass

    def persist(self):
        #persists are activations that happen in a different phase after casting
        pass

    def deactivation(self):
        #deactivations are activations that happen before the effect class object is deleted from Battleflow
        pass

class Skill(Effect): #class to interact with skill objects
    def __init__(self, name, initiator, bystander, battleflow):
        super().__init__(name, initiator, bystander, battleflow)
        #establish connection with skill database
        self.skillfile = pd.read_csv(db.SkillDatabase, sep = ',', header = 0, encoding = 'utf-8')
        #returns True for rows that fulfill the criterias and False for others. There should always be one true since monster name is unique
        self.match = self.skillfile['name'] == name
        #load skill information
        if self.skillfile['target'][self.match].values[0] == 'bystander':
            self.target = self.bystander
        elif self.skillfile['target'][self.match].values[0] == 'initiator':
            self.target = self.initiator
        self.expirycounter = self.skillfile['expirycounter'][self.match].values[0]
        self.buff = self.skillfile['buff'][self.match].values[0]
        self.stackable = self.skillfile['stackable'][self.match].values[0]
        self.startturnactivation = self.skillfile['startturnactivation'][self.match].values[0]
        self.endturnactivation = self.skillfile['endturnactivation'][self.match].values[0]

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
        self.battleitemfile = pd.read_csv(db.BattleItemDatabase, sep = ',', header = 0, encoding = 'utf-8')
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

class Attack(Skill):
    def __init__(self, initiator, bystander, battleflow):
        self.name = 'Attack'
        super().__init__(self.name, initiator, bystander, battleflow)
        self.battleflow.execute(self)

    def instant(self):
        self.value = self.initiator.attack - self.bystander.defense
        self.bystander.health -= self.value

    def persist(self):
        super.persist()

    def deactivation(self):
        super().deactivation()

class Defend(Skill):
    def __init__(self, initiator, bystander, battleflow):
        self.name = 'Defend'
        super().__init__(self.name, initiator, bystander, battleflow)
        self.battleflow.execute(self)

    def instant(self):
        self.value = self.initiator.defense * 1.5
        self.initiator.defense += self.value

    def persist(self):
        super().persist()

    def deactivation(self):
        self.initiator.defense -= self.value

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
