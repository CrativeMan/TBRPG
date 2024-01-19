class Player:
    def __init__(self, name, level=1, health=100, attack=10, defense=5):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        enemy.take_damage(damage)
