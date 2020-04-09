
import random

d4 = [1, 2, 3, 4]
d6 = [1, 2, 3, 4, 5, 6]
d8 = [1, 2, 3, 4, 5, 6, 7 ,8]
d10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
d20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

action_list = ["Attack", "Run", "Talk", "Done"]


enemies = [
      {"id": 1,
      "name": "Bandit", 
      "description": "Bandits rove in gangs and are sometimes led by thugs, veterans, or spellcasters. Not all bandits are evil.",
      "stats": {"str": 11, "dex": 12, "con": 12, "int": 10, "wis": 10, "cha": 10},
      "weapons": {"name": "Scimitar", "dice": "d6", "hit modifier": 3, "damage bonus": 1},
      "health": 11,
      "armor": 12,
      "dialogue": ["Give me your money or die by my sword", "Sorry, I need the money"] 
      },
      {"id": 2,
      "name": "Goblin",
      "descirption": "Goblins are small, black-hearted humanoids that lair in despoiled dungeons and other dismal settings.",
      "stats": {"str": 8, "dex": 14, "con": 10, "int": 10, "wis": 8, "cha": 8},
      "weapons":{"name": "Scimitar", "dice": "d6", "hit modifier": 4, "damage bonus": 2},
      "health": 7,
      "armor": 15,
      "dialogue": ["OOOhhh, SHINY!", "OOOhhhh, Looks TASTY!"]  
      }  
]

listlength = len(enemies)

userChoice = "NULL"
attack = 0

escape = ""

enemy = random.choice(enemies)
total_health = enemy["health"]

print('\n')
print("You've encountered a " + enemy["name"])
print('\n') 

while userChoice != "done" and total_health > 0 and escape != "success":
   
    userChoice = input(f"What do you want to do? {action_list} ")

    if userChoice == "Attack" or userChoice == "attack":
        attack = random.randint(1,20)
        if attack < enemy["armor"]:
            print("You rolled " + str(attack))
            print("Oh no! The attack missed")
        else:
            print("You rolled " + str(attack))
            damage = random.randint(1,6)
            total_health = total_health - damage
            
            if total_health > 0:
                print("The enemy has been wounded. You dealt " + str(damage) + " damage!")
                pass
            else:
                print("You have slain the " + enemy["name"])
                pass
            pass
    elif userChoice == "Run" or userChoice == "run":
        dexterity = random.randint(1,20)
        if dexterity <= enemy["stats"]["dex"]:
            print("You rolled " + str(dexterity))
            print("The enemy is keeping up! You can't get away!")
        else:
            print("You rolled " + str(dexterity))
            print("You have left the " + enemy["name"] + " in the dust!")
            escape = "success"
            pass
    elif userChoice == "talk" or userChoice == "Talk":
        print("You attempt to talk to the " + enemy["name"] +"!")
        print(enemy["name"] + ": " + random.choice(enemy["dialogue"]))
        print("Uh Oh!")   
        pass
    elif userChoice == "done" or userChoice == "Done":
        pass
    else:
        print("You don't know what to do!")
        pass
    



    pass


