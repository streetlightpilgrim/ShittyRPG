from database import Database
db = Database()

class Effect: #class to interact with effect of skills, attributes and items
    def __init__(self, id, initiator, bystander, battleflow):
        #transfer Player, Monster and Battleflow class objects to Effect class so it can be referred to dynamically
        self.id = id
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
    def __init__(self, id, initiator, bystander, battleflow):
        super().__init__(id, initiator, bystander, battleflow)
        #returns True for rows that fulfill the criterias and False for others
        self.match = db.SkillDatabase['id'] == self.id
        self.name = db.SkillDatabase['name'] == self.id
        #load skill information
        if db.SkillDatabase['target'][self.match].values[0] == 'bystander':
            self.target = self.bystander
        elif db.SkillDatabase['target'][self.match].values[0] == 'initiator':
            self.target = self.initiator
        self.expirycounter = int(db.SkillDatabase['expirycounter'][self.match].values[0])
        self.buff = bool(db.SkillDatabase['buff'][self.match].values[0])
        self.stackable = bool(db.SkillDatabase['stackable'][self.match].values[0])
        self.startturnactivation = bool(db.SkillDatabase['startturnactivation'][self.match].values[0])
        self.endturnactivation = bool(db.SkillDatabase['endturnactivation'][self.match].values[0])
        self.battleflow.execute(self)

    def instant(self):
        exec(db.SkillDatabase['instant'][self.match].values[0])

    def persist(self):
        exec(db.SkillDatabase['persist'][self.match].values[0])

    def deactivation(self):
        exec(db.SkillDatabase['deactivation'][self.match].values[0])

class Item(Effect): #class to interact with item objects
    def __init__(self, id, initiator, bystander, battleflow):
        super().__init__(id, initiator, bystander, battleflow)
        #returns True for rows that fulfill the criterias and False for others. There should always be one true since monster name is unique
        self.match = db.ItemDatabase['id'] == self.id
        #load item information
        if db.ItemDatabase['target'][self.match].values[0] == 'bystander':
            self.target = self.bystander
        elif db.ItemDatabase['target'][self.match].values[0] == 'initiator':
            self.target = self.initiator
        self.expirycounter = db.ItemDatabase['expirycounter'][self.match].values[0]
        self.buff = db.ItemDatabase['buff'][self.match].values[0]
        self.stackable = db.ItemDatabase['stackable'][self.match].values[0]
        self.startturnactivation = db.ItemDatabase['startturnactivation'][self.match].values[0]
        self.endturnactivation = db.ItemDatabase['endturnactivation'][self.match].values[0]

    def instant(self):
        exec(db.ItemDatabase['instant'][self.match].values[0])

    def persist(self):
        exec(db.ItemDatabase['persist'][self.match].values[0])

    def deactivation(self):
        exec(db.ItemDatabase['deactivation'][self.match].values[0])

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
