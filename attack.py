import random

playerhp = 200
attackl = 20
attackh = 50

while playerhp > 0:
    damage = random.randrange(attackl, attackh)
    playerhp = playerhp-damage
    if playerhp <=30:
        playerhp=30
    if playerhp == 30:
        print("Warning!! You are on low health!")
    print("Enemy did a damage of", damage,"points.","Current HP =",playerhp) 
    if playerhp == 0:
        print("You can't go any further... you've reached the limit.")