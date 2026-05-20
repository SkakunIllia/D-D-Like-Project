from functools import wraps
from re import match, sub
from Logger import dlog, logs
from time import sleep
from random import randint

# Global variables:
delay_time = 1
delay_time_quest = 1

# Logo
@dlog("printing the logo's separator")
def logo():
    logs(logo, 1, "printing the logo")
#     print(r"""
#      _
#     | |
#   __| |_   _ _ __   __ _  ___  ___  _ __  ___
#  / _` | | | | '_ \ / _` |/ _ \/ _ \| '_ \/ __|
# | (_| | |_| | | | | (_| |  __/ (_) | | | \__ \
#  \__,_|\__,_|_| |_|\__, |\___|\___/|_| |_|___/
#                     __/ |
#                    |___/ """, end = "")
#     print(r"""
#                              _
#                             | |
#               __ _ _ __   __| |
#              / _` | '_ \ / _` |
#             | (_| | | | | (_| |
#              \__,_|_| |_|\__,_| """)
#     print(r"""
#          _
#         | |
#       __| |_ __ __ _  __ _  ___  _ __  ___
#      / _` | '__/ _` |/ _` |/ _ \| '_ \/ __|
#     | (_| | | | (_| | (_| | (_) | | | |__ \
#      \__,_|_|  \__,_|\__, |\___/|_| |_|___/
#                       __/ |
#                      |___/""", end = "\n")
#     print(r"""
# ______                                               ___     _____
# |  _  \                                              / _ \   |  __ \
# | | | |_   _ _ __   __ _  ___  ___  _ __  ___   _   / /_\ \  | |  | |_ __ __ _  __ _  ___  _ __  ___
# | | | | | | | '_ \ / _` |/ _ \/ _ \| '_ \/ __| (_)  |  _  |  | |  | | '__/ _` |/ _` |/ _ \| '_ \/ __|
# | |/ /| |_| | | | | (_| |  __/ (_) | | | \__ \  _   | | | |  | |__| | | | (_| | (_| | (_) | | | \__ \
# |___/  \__,_|_| |_|\__, |\___|\___/|_| |_|___/ (_)  \_| |_/  |_____/|_|  \__,_|\__, |\___/|_| |_|___/
#                     __/ |                                                       __/ |
#                    |___/                                                       |___/
#     """)
    print(r"""
 .          .                 .         .
    ___  _  _  ___       _     _  ___  _   _  ___ 
   |  _\| \| || _ \     | |   | |/  _\| |_| ||_ _|  *
   | |  |    || | |     | |__ | | (_ ||  _  | | | 
   |___/|_|\_||___/     |____||_|\___||_| |_| |_|
      *          .              *                .
    """)
    logs(logo, 1, "printing the logo's separator")
    print("=================================================")

# Separator
def separator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sep()
        return func(*args, **kwargs)
    return wrapper

def sep():
    print("====================================")

# Randomising value for the quest to be completed,
# if the value of the player's 'luck' is higher than
# the value it means that the quest has to be completed
@dlog()
def random() -> int:
    return randint(randint(10, 20), randint(50, 70))

# Functions:
@dlog()
def sleep_delay(time_to_subtract: int = 0) -> None:
    if time_to_subtract == delay_time:
        sleep(delay_time)
    elif time_to_subtract == delay_time_quest:
        sleep(delay_time_quest)
    else:
        sleep(delay_time - time_to_subtract if delay_time - time_to_subtract > 0 else delay_time)

@dlog("verifying whether the answer is positive")
def verify_answer(string: str) -> bool|None:
    return match("Yes|yes|aha|Sure|OK|yeah|Yeah|y|Y|yep|Yep", sub(" ", "", string))

@dlog()
def language() -> None:
    print("Choose a language:")
    print("""1. English\t2. Polski\t3. Русский\t4. Державна""")
    input("Enter a number: ")

@separator
@dlog()
def next_thing():
    @dlog("are we going forward?")
    def internal():
        if verify_answer(input("Are you ready to go further?: (Y/N) ")):
            logs(next_thing, 1, "we are going forward")
            return True
        else:
            logs(next_thing, 1, "additional time to make decision")
            print("Alright, take your time, dear guest of mine")
            return internal()
    return internal()