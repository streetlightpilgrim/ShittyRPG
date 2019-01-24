def prefight(player, monster):
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

    #Battle intro message.
    print("{T1} VS {T2}".format(T1 = player.name, T2 = monster.name))
    print(monster.taunt)

    turncount(player, monster)
    #fightplayerturn(player, monster)

def turncount(player, monster):
    #Calculates using player and monster speed, who will get to 100 first.
    while monster.turncounter <= 100 and player.turncounter <= 100:
        player.turncounter += player.speed
        monster.turncounter += monster.speed
    #Activates player turn and reduce counter (keeps excess)
    if player.turncounter >= 100:
        player.turncounter -= 100
        playerturn(player,monster)
    #Activates monster turn and reduce counter (keeps excess)
    if monster.turncounter >= 100:
        monster.turncounter -= 100
        #monsterturn(player,monster)

def playerturn(player, monster):
    print("(1) Attack")
    print("(2) Defend")
    print("(3) Skills")
    print("(4) Invetory")
    print("(5) Inspect")
    print("(6) Run")
    print("(7) Help")
    option = input("FIGHT").lower()

    if option == "attack" or option == '1':
        playerattack(player, monster)
    elif option == "defend" or option == 2:
        playerdefend()
    elif option == "skills" or option == 3:
        skillsbattle()
    elif option == "inventory" or option == 4:
        iventorybattle()
    elif option == "inspect" or option == 5:
        inspectbattle()
    elif option == "run" or option == 6:
        runbattle()
    elif option == "help" or option == 7:
        helpbattle()
    else:
        playerturn(player, monster)

def playerattack(player, monster):
    monster.health -= player.attack_enhance
    fightcheck(player, monster)

def playerdefend():
    playerdefendcounter = 1

def skill():
    pass
def inventory():
    pass

def fightcheck(player, monster):
    if player.health <= 0:
        print("You Lose")
        ##gameover
    if monster.health <= 0:
        print("You Win")
    turncount(player, monster)
