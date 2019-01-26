class Combat:
    def __init__(self, player, monster):
        self.state = "__init__"
        #Load player base information.
        player.maxhealth = player.playerfile['maxhealth'][player.match].values[0]
        player.maxmana = player.playerfile['maxmana'][player.match].values[0]
        player.attack = player.playerfile['attack'][player.match].values[0]
        player.defense = player.playerfile['defense'][player.match].values[0]
        player.speed = player.playerfile['speed'][player.match].values[0]
        player.fire_enhance = player.playerfile['fire_enhance'][player.match].values[0]
        player.water_enhance = player.playerfile['water_enhance'][player.match].values[0]
        player.air_enhance = player.playerfile['air_enhance'][player.match].values[0]
        player.earth_enhance = player.playerfile['earth_enhance'][player.match].values[0]
        player.light_enhance = player.playerfile['light_enhance'][player.match].values[0]
        player.dark_enhance = player.playerfile['dark_enhance'][player.match].values[0]
        player.fire_resist = player.playerfile['fire_resist'][player.match].values[0]
        player.water_resist = player.playerfile['water_resist'][player.match].values[0]
        player.air_resist = player.playerfile['air_resist'][player.match].values[0]
        player.earth_resist = player.playerfile['earth_resist'][player.match].values[0]
        player.light_resist = player.playerfile['light_resist'][player.match].values[0]
        player.dark_resist = player.playerfile['dark_resist'][player.match].values[0]
        player.skill = player.playerfile['skill'][player.match].values[0]
        #load monster base information.
        monster.maxhealth = monster.monsterfile['maxhealth'][monster.match].values[0]
        monster.maxmana = monster.monsterfile['maxmana'][monster.match].values[0]
        monster.attack = monster.monsterfile['attack'][monster.match].values[0]
        monster.defense = monster.monsterfile['defense'][monster.match].values[0]
        monster.speed = monster.monsterfile['speed'][monster.match].values[0]
        monster.fire_enhance = monster.monsterfile['fire_enhance'][monster.match].values[0]
        monster.water_enhance = monster.monsterfile['water_enhance'][monster.match].values[0]
        monster.air_enhance = monster.monsterfile['air_enhance'][monster.match].values[0]
        monster.earth_enhance = monster.monsterfile['earth_enhance'][monster.match].values[0]
        monster.light_enhance = monster.monsterfile['light_enhance'][monster.match].values[0]
        monster.dark_enhance = monster.monsterfile['dark_enhance'][monster.match].values[0]
        monster.fire_resist = monster.monsterfile['fire_resist'][monster.match].values[0]
        monster.water_resist = monster.monsterfile['water_resist'][monster.match].values[0]
        monster.air_resist = monster.monsterfile['air_resist'][monster.match].values[0]
        monster.earth_resist = monster.monsterfile['earth_resist'][monster.match].values[0]
        monster.light_resist = monster.monsterfile['light_resist'][monster.match].values[0]
        monster.dark_resist = monster.monsterfile['dark_resist'][monster.match].values[0]
        monster.skill = monster.monsterfile['skill'][monster.match].values[0]
        monster.taunt = monster.monsterfile['taunt'][monster.match].values[0]
        monster.flavour_text = monster.monsterfile['flavour_text'][monster.match].values[0]
        #Load player battle exclusive information.
        player.health = player.maxhealth
        player.mana = player.maxmana
        player.fire_effective = player.fire_enhance - monster.fire_resist
        player.water_effective = player.water_enhance - monster.water_resist
        player.air_effective = player.air_enhance - monster.air_resist
        player.earth_effective = player.earth_enhance - monster.earth_resist
        player.light_effective = player.light_enhance - monster.light_resist
        player.dark_effective = player.dark_enhance - monster.dark_resist
        player.attack_enhance = player.attack - monster.defense + \
                                player.fire_effective + player.water_effective + \
                                player.air_effective + player.earth_effective + \
                                player.light_effective + player.dark_effective
        player.turncounter = 0
        #Load monster battle exclusive information.
        monster.health = monster.maxhealth
        monster.mana = monster.maxmana
        monster.fire_effective = monster.fire_enhance - player.fire_resist
        monster.water_effective = monster.water_enhance - player.water_resist
        monster.air_effective = monster.air_enhance - player.air_resist
        monster.earth_effective = monster.earth_enhance - player.earth_resist
        monster.light_effective = monster.light_enhance - player.light_resist
        monster.dark_effective = monster.dark_enhance - player.dark_resist
        monster.attack_enhance = monster.attack - player.defense + \
                                monster.fire_effective + monster.water_effective + \
                                monster.air_effective + monster.earth_effective + \
                                monster.light_effective + monster.dark_effective
        monster.turncounter = 0

        self.prefight(player, monster, state)

    def prefight(self, player, monster, state):
        self.state = "prefight"
        #Battle intro message.
        print("{T1} VS {T2}".format(T1 = player.name, T2 = monster.name))
        print(monster.taunt)

        self.turncount(player, monster, state)

    def turncount(self, player, monster, state):
        self.state = "turncount"
        #Calculates using player and monster speed, who will get to 100 first.
        while monster.turncounter <= 100 and player.turncounter <= 100:
            player.turncounter += player.speed
            monster.turncounter += monster.speed
        #Activates player turn and reduce counter (keeps excess)
        if player.turncounter >= 100:
            player.turncounter -= 100
            self.playerturn(player, monster, state)
        #Activates monster turn and reduce counter (keeps excess)
        if monster.turncounter >= 100:
            monster.turncounter -= 100
            self.monsterturn(player, monster, state)

    def playerturn(self, player, monster, state):
        self.state = "playerturn"
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
            self.playerattack(player, monster, state)
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
            self.playerturn(player, monster, state)

    def preengage(self, player, monster, caster, target, state):
        self.state = "preengage"
        engage(player, monster, caster, target, state)

    def engage(self, player, monster, caster, target, state):
        self.state = "engage"
        postengage(player, monster, caster, target, state)

    def postengage(self, player, monster, caster, target, state):
        self.state = "postengage"
        endturn(player, monster, state)

    def playerattack(self, player, monster, state):
        self.state = "playerattack"
        monster.health -= player.attack_enhance
        self.fightcheck(player, monster, state)

    def endturn(self, player, monster, state):
        self.state = "endturn"
        self.turncount(player, monster, state)

    def endcheck(self, player, monster, state):
        if player.health <= 0:
            print("You Lose")
            ##gameover
        if monster.health <= 0:
            print("You Win")
            postfight(player, monster, state)

    def postfight(self, player, monster, state):
        self.state = "postfight"
        print("battle over")
