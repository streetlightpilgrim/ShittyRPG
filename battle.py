from database import Database
db = Database()
import effect
import os

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
        print("Another worthy opponent approaches. {} is dragged to a fight against his will!!!\n".format(self.player.name))
        print("{} challenges {} to a last man standing match!\n".format(self.monster.name, self.player.name))
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
        elif self.monster.turncounter >= 100:
            self.monster.turncounter -= 100
            self.startturn(self.monster)

    def startturn(self, initiator):
        #check for battle effects on player's turn activation
        self.battleflow.onstartturn(initiator)

        #check for battle ending conditions
        self.battleconclusion = self.endcheck()
        if self.battleconclusion == False:
            self.postfight(False)
        elif self.battleconclusion == True:
            self.postfight(True)

        #begin initiator's turn
        elif initiator == self.player:
            self.playerturn()
        elif initiator == self.monster:
            self.monsterturn()

    def playerturn(self):
        condition = False
        while condition == False:
            print("<++++++|PLAYER TURN|++++++>")
            print("{}".format(self.player.name))
            print("HP: {}".format(int(self.player.health)))
            print("Mana: {}\n".format(int(self.player.mana)))
            print("{}".format(self.monster.name))
            print("HP: {}\n".format(int(self.monster.health)))
            print("{}: What would be my best option here? Think...think...\n".format(self.player.name))
            #player battle input menu
            print("---|DILEMMA|---")
            print("(1) Attack")
            print("(2) Defend")
            print("(3) Witchcraft")
            print("(4) Invetory")
            print("(5) Inspect")
            print("(6) Run")
            print("")

            option = input(">>> ").title()
            print("")

            #activate generic attack
            if option == "Attack" or option == '1':
                os.system('cls')
                print("{}: Energy Wave!\n".format(self.player.name))
                effect.Skill(1, self.player, self.monster, self.battleflow).instant()
                condition = True

            #activate generic defense
            elif option == "Defend" or option == '2':
                os.system('cls')
                print("{}: Focus Barrier!\n".format(self.player.name))
                effect.Skill(2, self.player, self.monster, self.battleflow).instant()
                condition = True

            elif option == "Witchcraft" or option == '3':
                os.system('cls')
                print("{}: What should I cast?\n".format(self.player.name))
                condition = True
                self.playerskillmenu()

            elif option == "Inventory" or option == '4':
                os.system('cls')
                print("{}: Stand over there for a second. Just going through my bag.\n".format(self.player.name))
                condition = True
                self.playeritemmenu()

            elif option == "Inspect" or option == '5':
                os.system('cls')
                print("{}: Sense Check!\n".format(self.player.name))
                print("{}".format(self.monster.name))

                print("Max HP: {}".format(int(self.monster.maxhealth)))
                print("Attack: {}".format(int(self.monster.attack)))
                print("Defense: {}".format(int(self.monster.defense)))
                print("Speed: {}".format(int(self.monster.speed)))
                print("")

                print("Fire Enhance: {}".format(int(self.monster.fire_enhance)))
                print("Water Enhance: {}".format(int(self.monster.water_enhance)))
                print("Air Enhance: {}".format(int(self.monster.air_enhance)))
                print("Earth Enhance: {}".format(int(self.monster.earth_enhance)))
                print("Light Enhance: {}".format(int(self.monster.light_enhance)))
                print("Dark Enhance: {}".format(int(self.monster.dark_enhance)))
                print("")

                print("Fire Resist: {}".format(int(self.monster.fire_resist)))
                print("Water Resist: {}".format(int(self.monster.water_resist)))
                print("Air Resist: {}".format(int(self.monster.air_resist)))
                print("Earth Resist: {}".format(int(self.monster.earth_resist)))
                print("Light Resist: {}".format(int(self.monster.light_resist)))
                print("Dark Resist: {}".format(int(self.monster.dark_resist)))
                print("")

                print("{}: I see, so that's what you are...\n".format(self.player.name))
                condition = False

            elif option == "Run" or option == '6':
                os.system('cls')
                self.player.health = 0
                condition = True

            else:
                os.system('cls')
                print("{} I have to make a perfectly logical decision.\n".format(self.player.name))

        #check for battle ending conditions
        self.battleconclusion = self.endcheck()
        if self.battleconclusion == False:
            self.postfight(False)
        elif self.battleconclusion == True:
            self.postfight(True)
        else: #activate endturn phase
            self.endturn(self.playerturn)

    def monsterturn(self):
        #check for battle ending conditions
        print("<++++++|ENEMY TURN|++++++>")
        self.battleconclusion = self.endcheck()
        if self.battleconclusion == False:
            self.postfight(False)
        elif self.battleconclusion == True:
            self.postfight(True)

        #activate endturn phase
        self.endturn(self.monsterturn)

    def endturn(self, initiator):
        #check for battle effects on end of turn activation
        self.battleflow.onendturn(initiator)

        #check for battle ending conditions
        self.battleconclusion = self.endcheck()
        if self.battleconclusion == False:
            self.postfight(False)
        elif self.battleconclusion == True:
            self.postfight(True)
        else: #loop back and activate turncount phase
            self.turncount()

    def playerskillmenu(self):
        #show available skills for battle
        print("---|WITCHCRAFT|---")
        print("{}".format(self.player.name))
        print("HP: {}".format(int(self.player.health)))
        print("Mana: {}\n".format(int(self.player.mana)))
        print("{}".format(self.monster.name))
        print("HP: {}\n".format(int(self.monster.health)))
        print(self.player.equipped_skill_name,"\n")
        option = input(">>> ").title()
        os.system('cls')

        if option in self.player.equipped_skill_name:
            enough_mana = self.checkmana(option) #check if player has enough mana for skill
            if enough_mana == True:
                print("{}: {}!\n".format(self.player.name, option))
                self.player.mana -= self.manacost
                #activate skill after deducting mana
                skill_id = self.player.equipped_skill_id[self.player.equipped_skill_name.index(option)]
                effect.Skill(skill_id, self.player, self.monster, self.battleflow).instant()
            elif enough_mana == False:
                print("{}: Woops, looks like I don't have enough mana for this spell.\n".format(self.player.name))
                print("{}: Perhaps the very useful \"Back\" spell is needed here.\n".format(self.player.name))
                self.playerskillmenu()
        elif option == "Back":
            self.playerturn()
        else:
            print("{}: Huh, I don't think I've ever learnt that incantation.\n".format(self.player.name))
            print("{}: Perhaps the very useful \"Back\" spell is needed here.\n".format(self.player.name))
            self.playerskillmenu()

    def playeritemmenu(self):
        #show available skills for battle
        print("---|INVENTORY|---")
        print("{}".format(self.player.name))
        print("HP: {}".format(int(self.player.health)))
        print("Mana: {}\n".format(int(self.player.mana)))
        print("{}".format(self.monster.name))
        print("HP: {}\n".format(int(self.monster.health)))
        print(self.player.equipped_item_name, "\n")
        option = input(">>> ").title()
        os.system('cls')

        if option in self.player.equipped_item_name:
            print("{}: {}!\n".format(self.player.name, option))
            #activate item after removing from equipped inventory
            item_id = self.player.equipped_item_id[self.player.equipped_item_name.index(option)]
            self.player.equipped_item_name.remove(option)
            effect.Item(item_id, self.player, self.monster, self.battleflow).instant()
        elif option == "Back":
            self.playerturn()
        else:
            print("{}: That must be a legendary item, I don't think I have that.\n".format(self.player.name))
            print("{}: Perhaps the very useful \"Back\" spell is needed here.\n".format(self.player.name))
            self.playeritemmenu()

    def checkmana(self, option):
        self.manacost = self.player.equipped_skill_manacost[self.player.equipped_skill_name.index(option)]
        if self.manacost <= self.player.mana:
            return True
        elif self.manacost > self.player.mana:
            return False

    def endcheck(self):
        if self.player.health <= 0:
            print("XXX|DEFEAT|XXX")
            print("{} has been defeated in battle by {}\n".format(self.player.name, self.monster.name))
            return False
            #gameover
        elif self.monster.health <= 0:
            print("XXX|VICTORY|XXX")
            print("{} snatches another victory by besting {} in combat.\n".format(self.player.name, self.monster.name))
            print("{}: {}\n".format(self.monster.name, self.monster.final_words))
            return True

    def postfight(self, result):
        if result == False:
            print("{}: Arggh! Okay, you made your point. I'll see you again next week...\n".format(self.player.name))
        if result == True:
            print("{}: Your belongings is now my capitalism! Hooooo!!!\n".format(self.player.name))
