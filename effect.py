import pandas as pd

class Effect:
    def __init__(self, name, caster, target, battleflow):
        self.name = name
        self.caster = caster
        self.target = target
        self.battleflow = battleflow

    def instant(self):
        pass

    def persist(self):
        pass

    def deactivation(self):
        pass

class Skill(Effect):
    def __init__(self, name, caster, target, battleflow, SkillDatabase):
        self.skillfile = pd.read_csv(SkillDatabase, sep = ',', header = 0, encoding = 'utf-8')
        self.match = self.skillfile['name'] == name

        self.expiry_counter = self.skillfile['expiry_counter'][self.match].values[0]
        self.buff = self.skillfile['buff'][self.match].values[0]
        self.stackable = self.skillfile['stackable'][self.match].values[0]
        self.playerturnactivation = self.skillfile['playerturnactivation'][self.match].values[0]
        self.monsterturnactivation = self.skillfile['monsterturnactivation'][self.match].values[0]
        self.endturnactivation = self.skillfile['endturnactivation'][self.match].values[0]

        super().__init__(name, caster, target, battleflow)

    def instant(self):
        super().instant(self)

    def persist(self):
        super().persist(self)

    def deactivation(self):
        super().deactivation(self)

class Attack(Skill):
    def __init__(self, caster, target, battleflow, SkillDatabase):
        self.name = 'Attack'

        super().__init__(self.name, caster, target, battleflow, SkillDatabase)

        print(self.buff, self.name, self.endturnactivation, self.expiry_counter)

        self.skillvalues = [self, self.name, self.expiry_counter, self.buff, self.stackable, \
                    self.playerturnactivation, self.monsterturnactivation, \
                    self.endturnactivation, self.caster, self.target]

        battleflow.execute(self.skillvalues, battleflow)

    def instant(self):
        self.value = self.caster.attack - self.target.defense
        self.target.health -= self.value
        print(self.target.health)

    def persist(self):
        print("Hellow")

    def deactivation(self):
        pass

class Battleflow:
    def __init__(self):
        self.executions = []

        self.classobject = 'classobject'
        self.name = 'name'
        self.expiry_counter = 'expiry_counter'
        self.buff = 'buff'
        self.stackable = 'stackable'
        self.playerturnactivation = 'playerturnactivation'
        self.monsterturnactivation = 'monsterturnactivation'
        self.endturnactivation = 'endturnactivation'
        self.caster = 'caster'
        self.target = 'target'
        self.skillkeys = [self.classobject, self.name, self.expiry_counter, self.buff, self.stackable, \
                    self.playerturnactivation, self.monsterturnactivation, \
                    self.endturnactivation, self.caster, self.target]

    def execute(self, skillvalues, battleflow):
        self.joinkeyandvalues = dict(zip(self.skillkeys, skillvalues))
        self.executions.append(self.joinkeyandvalues)

    def onplayerturn(self):
        for execution in self.executions:
            if execution['playerturnactivation'] == True and execution['expiry_counter'] >= 0:
                execution['classobject'].persist()

    def onmonsterturn(self):
        for execution in self.executions:
            if execution['monsterturnactivation'] == True and execution['expiry_counter'] >= 0:
                execution['classobject'].persist()

    def onendturn(self):
        for execution in self.executions:
            if execution['endturnactivation'] == True and execution['expiry_counter'] >= 0:
                execution['classobject'].persist()
