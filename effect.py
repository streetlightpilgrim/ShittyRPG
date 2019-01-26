class CombatEffects:
    def __init__(self, name):
        self.name = name
        self.effect_code = None
        self.expiry_time = None
        self.buff = False
        self.stackable = False
        self.priority = None
        self.instant = False

class CombatEffectsManager:
    def __init__(self):
        pass
class Fireball:
    def __init__(self, name):
        self.name = name
        self.effect_code = 1
        self.expiry_time = 2
        self.buff = False
        self.stackable = False
        self.priority = None
        self.instant = True

    def addonplayerturn

    def effect(self):
