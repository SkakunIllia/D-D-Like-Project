import Entities
import logging
import os
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


def print_player_classes():
    print("1. Archer")
    print("2. Wizard")
    print("3. Gnome")
    print("4. Ogr")
    print("5. Knight")

def read_player_name():
    while (player_name := input("What is your name? ")) == "":
        continue
    return player_name

def read_player_class():
    try:
        while not (player_class := int(input("What class do you want to play? (Enter a number) "))):
            continue
        match player_class:
            case 1: player_class = "Archer"
            case 2: player_class = "Wizard"
            case 3: player_class = "Gnome"
            case 4: player_class = "Ogr"
            case 5: player_class = "Knight"
            case _: raise ValueError("Wrong player_class. Usage: 1 <= player_class <= 5")
        return player_class
    except ValueError:
        return read_player_class()

def main():
    log()
    player_name = read_player_name()
    print_player_classes()
    player_class = read_player_class()
    player = Entities.Player(player_name, player_class)
    print(player)

main()