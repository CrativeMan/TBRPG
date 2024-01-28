import json
from player import Player, classes, races

print("Please input your character's name: ")
Player.name = input()

print("Please choose your character's class:")
for i, class_name in enumerate(classes, start=1):
    print(f"{i}. {class_name}")

print("Please input the number of your class:")
class_num = int(input())
Player.clas = classes[class_num - 1]

print("Please choose your race: ")
for i, race in enumerate(races, start=1):
    print(f"{i}. {race}")

print("Please input the number of your race:")
race_num = int(input())
Player.race = races[race_num - 1]

Player.printStats(Player)
