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
        option = input("FIGHT").lower()
        #activate generic attack
        if option == "attack" or option == '1':
            effect.Attack(self.player, self.monster, self.battleflow).instant()
        #activate generid defense
        elif option == "defend" or option == '2':
            effect.Defend(self.player, self.monster, self.battleflow).instant()
            #effect.Potion(self.player, self.monster, self.battleflow).instant()

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
