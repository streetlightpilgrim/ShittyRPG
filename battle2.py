import effect

class Combat:
    def __init__(self, player, monster, SkillDatabase):
        self.player = player
        self.monster = monster
        self.SkillDatabase = SkillDatabase
        #Load player base information.
        self.player.maxhealth = self.player.playerfile['maxhealth'][self.player.match].values[0]
        self.player.maxmana = self.player.playerfile['maxmana'][self.player.match].values[0]
        self.player.attack = self.player.playerfile['attack'][self.player.match].values[0]
        self.player.defense = self.player.playerfile['defense'][self.player.match].values[0]
        self.player.speed = self.player.playerfile['speed'][self.player.match].values[0]
        self.player.fire_enhance = self.player.playerfile['fire_enhance'][self.player.match].values[0]
        self.player.water_enhance = self.player.playerfile['water_enhance'][self.player.match].values[0]
        self.player.air_enhance = self.player.playerfile['air_enhance'][self.player.match].values[0]
        self.player.earth_enhance = self.player.playerfile['earth_enhance'][self.player.match].values[0]
        self.player.light_enhance = self.player.playerfile['light_enhance'][self.player.match].values[0]
        self.player.dark_enhance = self.player.playerfile['dark_enhance'][self.player.match].values[0]
        self.player.fire_resist = self.player.playerfile['fire_resist'][self.player.match].values[0]
        self.player.water_resist = self.player.playerfile['water_resist'][self.player.match].values[0]
        self.player.air_resist = self.player.playerfile['air_resist'][self.player.match].values[0]
        self.player.earth_resist = self.player.playerfile['earth_resist'][self.player.match].values[0]
        self.player.light_resist = self.player.playerfile['light_resist'][self.player.match].values[0]
        self.player.dark_resist = self.player.playerfile['dark_resist'][self.player.match].values[0]
        self.player.skill = self.player.playerfile['skill'][self.player.match].values[0]
        #load monster base information.
        self.monster.maxhealth = self.monster.monsterfile['maxhealth'][self.monster.match].values[0]
        self.monster.maxmana = self.monster.monsterfile['maxmana'][self.monster.match].values[0]
        self.monster.attack = self.monster.monsterfile['attack'][self.monster.match].values[0]
        self.monster.defense = self.monster.monsterfile['defense'][self.monster.match].values[0]
        self.monster.speed = self.monster.monsterfile['speed'][self.monster.match].values[0]
        self.monster.fire_enhance = self.monster.monsterfile['fire_enhance'][self.monster.match].values[0]
        self.monster.water_enhance = self.monster.monsterfile['water_enhance'][self.monster.match].values[0]
        self.monster.air_enhance = self.monster.monsterfile['air_enhance'][self.monster.match].values[0]
        self.monster.earth_enhance = self.monster.monsterfile['earth_enhance'][self.monster.match].values[0]
        self.monster.light_enhance = self.monster.monsterfile['light_enhance'][self.monster.match].values[0]
        self.monster.dark_enhance = self.monster.monsterfile['dark_enhance'][self.monster.match].values[0]
        self.monster.fire_resist = self.monster.monsterfile['fire_resist'][self.monster.match].values[0]
        self.monster.water_resist = self.monster.monsterfile['water_resist'][self.monster.match].values[0]
        self.monster.air_resist = self.monster.monsterfile['air_resist'][self.monster.match].values[0]
        self.monster.earth_resist = self.monster.monsterfile['earth_resist'][self.monster.match].values[0]
        self.monster.light_resist = self.monster.monsterfile['light_resist'][self.monster.match].values[0]
        self.monster.dark_resist = self.monster.monsterfile['dark_resist'][self.monster.match].values[0]
        self.monster.skill = self.monster.monsterfile['skill'][self.monster.match].values[0]
        self.monster.taunt = self.monster.monsterfile['taunt'][self.monster.match].values[0]
        self.monster.flavour_text = self.monster.monsterfile['flavour_text'][self.monster.match].values[0]
        #Load player battle exclusive information.
        self.player.health = self.player.maxhealth
        self.player.mana = self.player.maxmana
        self.player.fire_effective = self.player.fire_enhance - self.monster.fire_resist
        self.player.water_effective = self.player.water_enhance - self.monster.water_resist
        self.player.air_effective = self.player.air_enhance - self.monster.air_resist
        self.player.earth_effective = self.player.earth_enhance - self.monster.earth_resist
        self.player.light_effective = self.player.light_enhance - self.monster.light_resist
        self.player.dark_effective = self.player.dark_enhance - self.monster.dark_resist
        self.player.attack_enhance = self.player.attack - self.monster.defense + \
                                self.player.fire_effective + self.player.water_effective + \
                                self.player.air_effective + self.player.earth_effective + \
                                self.player.light_effective + self.player.dark_effective
        self.player.turncounter = 0
        #Load monster battle exclusive information.
        self.monster.health = self.monster.maxhealth
        self.monster.mana = self.monster.maxmana
        self.monster.fire_effective = self.monster.fire_enhance - player.fire_resist
        self.monster.water_effective = self.monster.water_enhance - player.water_resist
        self.monster.air_effective = self.monster.air_enhance - player.air_resist
        self.monster.earth_effective = self.monster.earth_enhance - player.earth_resist
        self.monster.light_effective = self.monster.light_enhance - player.light_resist
        self.monster.dark_effective = self.monster.dark_enhance - player.dark_resist
        self.monster.attack_enhance = self.monster.attack - player.defense + \
                                self.monster.fire_effective + self.monster.water_effective + \
                                self.monster.air_effective + self.monster.earth_effective + \
                                self.monster.light_effective + self.monster.dark_effective
        self.monster.turncounter = 0

        self.battleflow = effect.Battleflow()

        self.prefight()

    def prefight(self):
        #Battle intro message.
        print("{T1} VS {T2}".format(T1 = self.player.name, T2 = self.monster.name))
        print(self.monster.taunt)

        self.turncount()

    def turncount(self):
        #Calculates using player and monster speed, who will get to 100 first.
        while self.monster.turncounter <= 100 and self.player.turncounter <= 100:
            self.player.turncounter += self.player.speed
            self.monster.turncounter += self.monster.speed
        #Activates player turn and reduce counter (keeps excess)
        if self.player.turncounter >= 100:
            self.player.turncounter -= 100
            self.playerturn()
        #Activates monster turn and reduce counter (keeps excess)
        if self.monster.turncounter >= 100:
            self.monster.turncounter -= 100
            self.monsterturn()

    def playerturn(self):

        self.battleflow.onplayerturn()
        #Input menu
        print("(1) Attack")
        print("(2) Defend")
        print("(3) Skills")
        print("(4) Invetory")
        print("(5) Inspect")
        print("(6) Run")
        print("(7) Help")
        option = input("FIGHT").lower()

        if option == "attack" or option == '1':
            effect.Attack(self.player, self.monster, self.battleflow, self.SkillDatabase).instant()
            ##effect.Attack.instant()
            self.endturn()
            #value = self.playerattack(player, monster, state)
            #self.preengage(player, monster, state, value)
        elif option == "defend" or option == '2':
            pass
            #self.playerdefend(player, monster, state)
        elif option == "skills" or option == '3':
            pass
        elif option == "inventory" or option == '4':
            pass
        elif option == "inspect" or option == '5':
            pass
        elif option == "run" or option == '6':
            pass
        elif option == "help" or option == '7':
            pass
        else:
            self.playerturn()

    def endturn(self):
        self.battleflow.onendturn()
        self.turncount()

    def endcheck(self):
        if self.player.health <= 0:
            print("You Lose")
            ##gameover
        if self.self.monster.health <= 0:
            print("You Win")
            postfight()

    def postfight(self):
        print("battle over")
