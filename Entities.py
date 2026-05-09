from random import randint


# Randomising value for the quest to be completed,
# if the value of the player's 'luck' is higher than
# the value it means that the quest has to be completed
def random():
    return randint(randint(20, 40), randint(50, 70))

def initialize_entity(player_class, player_name):
    match player_class:
        case 1: return Archer(player_name)
        case 2: return Wizard(player_name)
        case 3: return Gnome(player_name)
        case 4: return Ogr(player_name)
        case 5: return Knight(player_name)
        case _: return Player(player_name, "Not defined")

#===================================================================================
class Entity:
    def __init__(self, name):
        self._name = name
    def __repr__(self):
        return f'Entity[Name: {self._name}]'
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name

class Player(Entity):
    def __init__(self, name, player_class):
        super().__init__(name)
        self._player_class = player_class
        self._items = []
        self._health = 100
        self._weapon = None
    def __repr__(self):
        return f'Player[Name: {self._name}, health: {self._health}, items: {self._items}, weapon: {self._weapon}]'
    def set_health(self, health):
        self._health = health
    def get_health(self):
        return self._health
    def set_items(self, items):
        self._items = items
    def get_items(self):
        return self._items
    def get_player_class(self):
        return self._player_class

class Archer(Player):
    def __init__(self, name):
        super().__init__(name, "Archer")
        self.set_items([Item("Relict bow", 65, 10)])
        self.set_health(80)
        self._damage = 15
        self._weapon = self._items[0]
    def __repr__(self):
        return f'Archer[Name: {self._name}, health: {self._health}, items: {self._items}, weapon: {self._weapon}]'
    def get_damage(self):
        return self._damage

class Knight(Player):
    def __init__(self, name):
        super().__init__(name, "Knight")
        self.set_health(120)
        self.set_items([Item("Silver sword", 45, 13)])
        self._damage = 20
        self._weapon = self._items[0]
    def __repr__(self):
        return f'Knight[Name: {self._name}, health: {self._health}, items: {self._items}, weapon: {self._weapon}]'
    def get_damage(self):
        return self._damage

class Ogr(Player):
    def __init__(self, name):
        super().__init__(name, "Ogr")
        self.set_health(150)
        self.set_items([Item("Greeny mace", 80, 7)])
        self._damage = 30
        self._weapon = self._items[0]
    def __repr__(self):
        return f'Ogr[Name: {self._name}, health: {self._health}, items: {self._items}, weapon: {self._weapon}]'
    def get_damage(self):
        return self._damage

class Gnome(Player):
    def __init__(self, name):
        super().__init__(name, "Gnome")
        self.set_health(100)
        self.set_items([Item("Gold pickaxe", 50, 7)])
        self._damage = 20
        self._weapon = self._items[0]
    def __repr__(self):
        return f'Gnome[Name: {self._name}, health: {self._health}, items: {self._items}, weapon: {self._weapon}]'
    def get_damage(self):
        return self._damage

class Wizard(Player):
    def __init__(self, name):
        super().__init__(name, "Wizard")
        self.set_health(80)
        self.set_items([Item("Magical wand", 60, 15)])
        self._damage = 10
        self._weapon = self._items[0]
    def __repr__(self):
        return f'Gnome[Name: {self._name}, health: {self._health}, items: {self._items}, weapon: {self._weapon}]'
    def get_damage(self):
        return self._damage

#===================================================================================
class Item(Entity):
    def __init__(self, name, damage = 0, durability = 0):
        super().__init__(name)
        self._durability = durability
        self._damage = damage
    def __repr__(self):
        return f'Item[Name: {self._name}]'

#===================================================================================
class Quest:
    def __init__(self, name):
        self._name = name
        self._random_value = random()
    def __repr__(self):
        return f'Item[Name: {self._name}, random value: {self._random_value}]'