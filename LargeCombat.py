import random

rollAgain = "n"

while 1:
    if rollAgain == "n":
        #name = raw_input("Enter Name: ")
        number = input("Number of Creatures in Attack Group: ")
        numAtk = input("Enter Number of Attacks per Unit: ")
        diceNum = input("Enter Number of Dice: ")
        diceSize = input("Enter Dice Size: ")
        toHit = input("Enter to Hit: ")
        toDmg = input("Enter Bonus to Damage: ")
        ac = input("Enter the AC of the target: ")

    tot = 0
    for x in range(number):
        for i in range(numAtk):
            roll = random.randint(1, 20) + toHit
            if roll >= ac:
                dmg = 0
                if roll == (20 + toHit):
                    for i in range(diceNum * 2):
                        dmg += random.randint(1, diceSize)
                else:
                    for j in range(diceNum):
                        dmg = dmg + random.randint(1, diceSize)
                dmg = dmg + toDmg
        tot = tot + dmg
    print ("\nTotal Damage: %d" % tot)
    rollAgain = raw_input("\nRoll Again with same Creature [y/n]")