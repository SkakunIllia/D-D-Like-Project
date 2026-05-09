from random import randint

# Randomising value for the quest to be completed,
# if the value of the player`s 'luck' is higher than
# the value it means that the quest has to be completed
def random():
    return randint(randint(20, 40), randint(50, 70))

class Entity:
    def __init__(self, name, type):
        self._name = name
        self._type = type
    def __repr__(self):
        return f'Entity[Name: {self._name}, type: {self._type}]'

class Player(Entity):
    def __init__(self, name, player_class):
        super().__init__(name, "Player")
        self._player_class = player_class
        self._items = []
        self._health = 100
        self._weapon = None
    def __repr__(self):
        return f'Player[Name: {self._name}, type: {self._type}, health:]'

class Archer(Player):
    def __init__(self, name):
        super().__init__(name, "Archer")
        self._health = 90
        self._damage = 15
        self._items = [Item("Relict bow", "Bow", 65, 10)]

class Knight(Player):
    def __init__(self, name):
        super().__init__(name, "Knight")
        self._health = 120
        self._damage = 20
        self._items = [Item("Silver sword", "Sword", 45, 13)]

class Ogr(Player):
    def __init__(self, name):
        super().__init__(name, "Ogr")
        self._health = 150
        self._damage = 30
        self._items = [Item("Greeny mace", "Mace", 80, 7)]

class Gnome(Player):
    def __init__(self, name):
        super().__init__(name, "Gnome")
        self._health = 100
        self._damage = 20
        self._items = [Item("Gold pickaxe", "Pickaxe", 50, 7)]

class Wizard(Player):
    def __init__(self, name):
        super().__init__(name, "Wizard")
        self._health = 80
        self._damage = 10
        self._items = [Item("Magical wand", "Wand", 60, 15)]

class Item(Entity):
    def __init__(self, name, typeOfEntity = "Entity", damage = 0, durability = 0):
        super().__init__(name, "Item")
        self._durability = durability
        self._damage = damage
        self._type = typeOfEntity
    def __repr__(self):
        return f'Item[Name: {self._name}, type: {self._type}]'

class Quest:
    def __init__(self, name):
        self._name = name
        self._random_value = random()
    def __repr__(self):
        return f'Item[Name: {self._name}, random value: {self._random_value}]'