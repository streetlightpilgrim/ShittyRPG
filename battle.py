from database import Database
db = Database()
import effect

class Combat:
    def __init__(self, player, monster):
        #transfer Player and Monster class objects to Combat class so it can be referred to dynamically
        self.player = player
        self.monster = monster
        #Load player battle exclusive information
        self.player.turncounter = 0
        #Load player skills for quick access
        self.player.equipped_skill_name = []
        self.player.equipped_skill_manacost = []
        for skill in self.player.equipped_skill_id:
            skillmatch = db.SkillDatabase['id'] == skill
            self.player.equipped_skill_name.append(db.SkillDatabase['name'][skillmatch].values[0])
            self.player.equipped_skill_manacost.append(int(db.SkillDatabase['manacost'][skillmatch].values[0]))
        #Load player items for quick access
        self.player.equipped_item_name = []
        for item in self.player.equipped_item_id:
            itemmatch = db.ItemDatabase['id'] == item
            self.player.equipped_item_name.append(db.ItemDatabase['name'][itemmatch].values[0])

        #Load monster battle exclusive information
        self.monster.health = self.monster.maxhealth
        self.monster.turncounter = 0

        #load Battleflow
        self.battleflow = effect.Battleflow()
        #activate prefight phase
        self.prefight()

    def prefight(self):
        #battle intro message
        print("Another worthy opponent approaches. You are dragged to a fight against your will!!!\n")
        print("{} challenges you to a last man standing match!\n".format(self.monster.name))
        print("<++++++|BATTLE START|++++++>\n")
        print("{}: {}\n".format(self.monster.name, self.monster.taunt))
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
        print("<++++++|PLAYER TURN|++++++>\n")
        print("{}: What would be my best option here? Think...think...\n".format(self.player.name))
        #player battle input menu
        print("---|DILEMMA MENU|---")
        print("(1) Attack")
        print("(2) Defend")
        print("(3) Witchcraft")
        print("(4) Invetory")
        print("(5) Inspect")
        print("(6) Run")
        print("(7) Help")
        print("")

        option = input(">>> ").title()
        print("")

        #activate generic attack
        if option == "Attack" or option == '1':
            print("{}: Energy Wave!\n".format(self.player.name))
            effect.Skill(1, self.player, self.monster, self.battleflow).instant()
        #activate generic defense
        elif option == "Defend" or option == '2':
            print("{}: Focus Barrier!\n".format(self.player.name))
            effect.Skill(2, self.player, self.monster, self.battleflow).instant()
        elif option == "Witchcraft" or option == '3':
            print("{}: What should I cast?\n".format(self.player.name))
            self.playerskillmenu()
        elif option == "Inventory" or option == '4':
            print("{}: Stand over there for a second. Just going through my bag.\n".format(self.player.name))
            self.playeritemmenu()
        elif option == "Inspect" or option == '5':
            pass
        elif option == "Run" or option == '6':
            print("Alright, alright, I'm out of here.")
            self.postfight('L')
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
        self.battleconclusion = self.endcheck()
        if self.battleconclusion == 'L':
            self.postfight('L')
        elif self.battleconclusion == 'W':
            self.postfight('W')

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
        #show available skills for battle
        print("---|WITCHCRAFT SPELLS|---")
        print(self.player.equipped_skill_name,"\n")
        option = input(">>> ").title()
        print("")

        if option in self.player.equipped_skill_name:
            enough_mana = self.checkmana(option) #check if player has enough mana for skill
            if enough_mana == True:
                self.player.mana -= self.manacost
                #activate skill after deducting mana
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

    def playeritemmenu(self):
        #show available skills for battle
        print(self.player.equipped_item_name)
        option = input(">>> ").title()
        print("\n")

        if option in self.player.equipped_item_name:
            #activate item after removing from equipped inventory
            item_id = self.player.equipped_item_id[self.player.equipped_item_name.index(option)]
            self.player.equipped_item_name.remove(option)
            effect.Item(item_id, self.player, self.monster, self.battleflow).instant()
        elif option == "Back":
            print("back clicked")
        else:
            print("Huh, I don't think I've ever learnt that incantation.")
            self.playeritemmenu()

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
