import os, time, logging, Entities, re
from datetime import datetime
from glob import glob

def log():
    path = "logs/*.log"
    files = glob(path)
    if len(files) >= 5:
        os.remove(files[0])

    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    date_now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".log"
    log_path = os.path.join(log_dir, date_now)
    logging.basicConfig(level = logging.DEBUG, filename = log_path, filemode = "w", format = "%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger("Logger")
    logger.info("Initializing logger")
    return logger

logger = log()

def print_player_classes():
    separator()
    print("Here are the classes that you can play in this game: ")
    print("1. Archer")
    print("2. Wizard")
    print("3. Gnome")
    print("4. Ogr")
    print("5. Knight")
    time.sleep(delay_time)

def print_player_classes_description():
    separator()
    print("Each class has its own speciality")
    print("1. Archer")
    print(f"\tYou posses a bow with which you can hit enemies from long distance. Health: {Entities.Archer.get_health(Entities.Archer(None))}. "
          f"Damage: {Entities.Archer.get_damage(Entities.Archer(None))}")
    print("2. Wizard")
    print(f"\tYou posses a magic wand with which you can hit enemies from long distance. Health: {Entities.Wizard.get_health(Entities.Wizard(None))}. "
        f"Damage: {Entities.Wizard.get_damage(Entities.Wizard(None))}")
    print("3. Gnome")
    print(f"\tYou posses a golden pickaxe with which you can hit enemies from short distance. Health: {Entities.Gnome.get_health(Entities.Gnome(None))}. "
        f"Damage: {Entities.Gnome.get_damage(Entities.Gnome(None))}")
    print("4. Ogr")
    print(f"\tYou posses a mace with which you can hit enemies from medium distance. Health: {Entities.Ogr.get_health(Entities.Ogr(None))}. "
        f"Damage: {Entities.Ogr.get_damage(Entities.Ogr(None))}")
    print("5. Knight")
    print(f"\tYou posses a silver sword  with which you can hit enemies from short distance. Health: {Entities.Knight.get_health(Entities.Knight(None))}. "
        f"Damage: {Entities.Knight.get_damage(Entities.Knight(None))}")
    time.sleep(delay_time)

def read_player_name():
    separator()
    while (player_name := input("What is your name? ")) == "":
        continue
    return player_name

def read_player_class():
    separator()
    try:
        while not (player_class := int(input("What class do you want to play? (Enter a number) "))):
            continue
        if not ( 1 <= player_class <= 5):
            raise ValueError("Wrong player_class. Usage: 1 <= player_class <= 5")
        return player_class
    except ValueError:
        return read_player_class()

def greeting():
    logger.info("def greeting invocation")
    print("Welcome to the game of D&D Light")
    print("The concept of the game is the same as in the D&D")
    print("The game consists of some random amount of quest that you have to complete")
    print("Then you enter the boss stage and that's all")
    print("Pretty simple, isn't it?")
    print("So let's try this game out!")
    time.sleep(delay_time)

def separator():
    logger.info("def separator invocation")
    print("====================================")

def next_thing():
    separator()
    def internal():
        logger.info("def next_thing invocation")
        if re.match("Yes|yes|aha|Sure|OK|yeah|Yeah|y|Y|yep|Yep", re.sub(" ", "", input("Are you ready to go futher?: "))):
            return True
        else:
            logger.info("def next_thing additional time to make decision")
            print("Alright, take your time, dear guest of mine")
            time.sleep(2)
            return internal()
    return internal()

delay_time = 1

def main():
    logger.info("def main invocation")
    greeting()
    next_thing()

    print_player_classes()
    print_player_classes_description()
    next_thing()

    player_name = read_player_name()
    player_class = read_player_class()
    player = Entities.initialize_entity(player_class, player_name)
    print(player)
    # next_thing()

main()