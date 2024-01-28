classes = [
    "Artificer",
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard"
]

races = [
    "Dragonborn",
    "Dwarf",
    "Elf",
    "Gnome",
    "Half-Elf",
    "Halfling",
    "Half-Orc",
    "Human",
    "Tiefling",
    "Aarakocra",
]


class Player:
    def __init__(self, name, level, clas, race, health):
        self.name = name,
        self.level = level,
        self.clas = clas,
        self.race = race,
        self.health = health,

    def printStats(self):
        print(self.name)
        print(self.level)
        print(self.clas)
        print(self.race)
        print(self.health)
        