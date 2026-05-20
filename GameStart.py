from Entities import *
from Auxiliary import *

@dlog("greeting the player")
def greeting():
    print("Welcome to the game of D&D Light")
    print("The concept of the game is the same as in the D&D")
    print("The game consists of some random amount of quest that you have to complete")
    print("Then you enter the boss stage and that's all")
    print("Pretty simple, isn't it?")
    print("So let's try this game out!")
    sleep_delay(delay_time)

@separator
@dlog("printing classes")
def print_player_classes():
    print("Here are the classes that you can play in this game: ")
    print("1. Archer")
    print("2. Wizard")
    print("3. Gnome")
    print("4. Ogre")
    print("5. Knight")
    sleep_delay(5)

@separator
@dlog("printing classes description")
def print_player_classes_description():
    print("Each character has its own speciality")
    print("1. Archer")
    print(f"\tYou posses a bow with which you can hit enemies from long distance. Health: {Archer.get_health(Archer(None))}.")
    print("2. Wizard")
    print(f"\tYou posses a magic wand with which you can hit enemies from long distance. Health: {Wizard.get_health(Wizard(None))}.")
    print("3. Gnome")
    print(f"\tYou posses a golden pickaxe with which you can hit enemies from short distance. Health: {Gnome.get_health(Gnome(None))}.")
    print("4. Ogre")
    print(f"\tYou posses a mace with which you can hit enemies from medium distance. Health: {Ogre.get_health(Ogre(None))}.")
    print("5. Knight")
    print(f"\tYou posses a silver sword  with which you can hit enemies from short distance. Health: {Knight.get_health(Knight(None))}.")
    sleep_delay(7)

@separator
@dlog("reading player's name")
def read_player_name():
    while (player_name := input("What is your name? ")) == "":
        logs(read_player_name, 1, "null name")
        continue
    return player_name

@dlog("reading player's class")
def read_player_class():
    try:
        while not (player_class := int(input("What class do you want to play? (Enter a number from a list above) "))):
            logs(read_player_class, 1, "null class")
            continue
        if not ( 1 <= player_class <= 5):
            logs(read_player_class, 1, "improper class")
            raise ValueError("Wrong player_class. Usage: 1 <= player_class <= 5")
        return player_class
    except ValueError:
        return read_player_class()

@dlog("choosing class")
def class_choice():
    player_name = read_player_name()
    player_class = read_player_class()
    logs(class_choice, 1, "initializing player")
    player = initialize_entity(player_class, player_name)
    print()
    sep()
    print(f"Here is your character -> {player.__repr__()}\n", end="")
    if verify_answer(input("Is that what you wanted? (Y/N) ")):
        logs(class_choice, 1, "going to the game itself")
        sep()
        print("\nAlright, then let's start our journey into the world of D&D Light!")
        return player
    else:
        logs(class_choice, 1, "rechoosing the class or the name")
        return class_choice()