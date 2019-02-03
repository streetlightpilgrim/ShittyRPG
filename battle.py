from database import Database
db = Database()
import effect

class Combat:
    def __init__(self, player, monster):
        #transfer Player and Monster class objects to Combat class so it can be referred to dynamically
        self.player = player
        self.monster = monster
        #Load player battle exclusive information
        self.player.health = self.player.maxhealth
        self.player.mana = self.player.maxmana
        #Load player skills for quick access
        self.player.equipped_skill_name = []
        self.player.equipped_skill_manacost = []
        for skill in self.player.equipped_skill_id:
            skillmatch = db.SkillDatabase['id'] == skill
            self.player.equipped_skill_name.append(db.SkillDatabase['name'][skillmatch].values[0])
            self.player.equipped_skill_manacost.append(int(db.SkillDatabase['manacost'][skillmatch].values[0]))
        self.player.turncounter = 0
        #Load monster battle exclusive information
        self.monster.health = self.monster.maxhealth
        self.monster.turncounter = 0
        #load Battleflow
        self.battleflow = effect.Battleflow()
        #activate prefight phase
        self.prefight()

    def prefight(self):
        #battle intro message
        print("{T1} VS {T2}".format(T1 = self.player.name, T2 = self.monster.name))
        print(self.monster.taunt)
        #activate turncount phase
        self.turncount()

    def turncount(self):
        #calculates using player and monster speed, who will get to 100 first
        while self.monster.turncounter <= 100 and self.player.turncounter <= 100:
            self.player.turncounter += self.player.speed
            self.monster.turncounter += self.monster.speed
        #activates starturn phase and reduce counter (keeps excess)
        if self.player.turncounter >= 100:
            self.player.turncounter -= 100
            self.startturn(self.player)
        #activates starturn phase and reduce counter (keeps excess)
        if self.monster.turncounter >= 100:
            self.monster.turncounter -= 100
            self.startturn(self.monster)

    def startturn(self, initiator):
        #check for battle effects on player's turn activation
        self.battleflow.onstartturn(initiator)
        #check for battle ending conditions
        self.battleconclusion = self.endcheck()
        if self.battleconclusion == 'L':
            self.postfight('L')
        elif self.battleconclusion == 'W':
            self.postfight('W')
        #begin initiator's turn
        elif initiator == self.player:
            self.playerturn()
        elif initiator == self.monster:
            self.monsterturn()

    def playerturn(self):
        #player battle input menu
        print("(1) Attack")
        print("(2) Defend")
        print("(3) Skills")
        print("(4) Invetory")
        print("(5) Inspect")
        print("(6) Run")
        print("(7) Help")
        option = input(">>>").title()
        #activate generic attack
        if option == "Attack" or option == '1':
            effect.Skill(1, self.player, self.monster, self.battleflow).instant()
        #activate generid defense
        elif option == "Defend" or option == '2':
            effect.Skill(2, self.player, self.monster, self.battleflow).instant()
            #effect.Potion(self.player, self.monster, self.battleflow).instant()
        elif option == "Skills" or option == '3':
            print("What should I cast?")
            self.playerskillmenu()

        elif option == "Inventory" or option == '4':
            pass
        elif option == "Inspect" or option == '5':
            pass
        elif option == "Run" or option == '6':
            pass
        elif option == "Help" or option == '7':
            pass
        else:
            self.playerturn()
        #check for battle ending conditions
        self.battleconclusion = self.endcheck()
        if self.battleconclusion == 'L':
            self.postfight('L')
        elif self.battleconclusion == 'W':
            self.postfight('W')
        else: #activate endturn phase
            self.endturn(self.playerturn)

    def monsterturn(self):
        #check for battle ending conditions
        self.endcheck()
        #activate endturn phase
        self.endturn(self.monsterturn)

    def endturn(self, initiator):
        #check for battle effects on end of turn activation
        self.battleflow.onendturn(initiator)
        #check for battle ending conditions
        self.battleconclusion = self.endcheck()
        if self.battleconclusion == 'L':
            self.postfight('L')
        elif self.battleconclusion == 'W':
            self.postfight('W')
        else: #loop back and activate turncount phase
            self.turncount()

    def playerskillmenu(self):
        print(self.player.equipped_skill_name)
        option = input(">>>").title()
        if option in self.player.equipped_skill_name:
            enough_mana = self.checkmana(option)
            if enough_mana == True:
                self.player.mana -= self.manacost
                skill_id = self.player.equipped_skill_id[self.player.equipped_skill_name.index(option)]
                effect.Skill(skill_id, self.player, self.monster, self.battleflow).instant()
            elif enough_mana == False:
                print("Woops, looks like I don't have enough mana for this spell.")
                self.playerskillmenu()
        elif option == "Back":
            print("back clicked")
        else:
            print("Huh, I don't think I've ever learnt that incantation.")
            self.playerskillmenu()

    def checkmana(self, option):
        self.manacost = self.player.equipped_skill_manacost[self.player.equipped_skill_name.index(option)]
        if self.manacost <= self.player.mana:
            return True
        elif self.manacost > self.player.mana:
            return False

    def endcheck(self):
        if self.player.health <= 0:
            print("You Lose")
            return 'L'
            ##gameover
        elif self.monster.health <= 0:
            print("You Win")
            return 'W'

    def postfight(self, result):
        if result == 'L':
            pass
        if result == 'W':
            pass
            print("battle over")
