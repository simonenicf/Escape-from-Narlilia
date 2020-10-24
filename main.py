import sys
import time
from menu import Menu
from game_engine import Console, Player

console = Console()
player = Player()
start = True
name = " "
trigger = 0
start_sim = " "
retry_input = " "
bye = 0

# Function to exit the game
def quit():
    print("okay bye")
    exit(0)

# put the intro here
def intro():
    print("please put intro here")
    adventure()

# Start adventure
def adventure():
    input("@: Is anybody there???: ")
    time.sleep(0.5)
    print("@: WHAAAAAA!!!!")
    time.sleep(0.5)
    print("@: Oh sorry. I didn't expect that you where there.")
    time.sleep(0.5)
    player.set_name(console.check_answer("So what is our name user?"))
    print("Oh hi " + player.get_name(name) + ". It's nice to meet you.")
    time.sleep(0.5)
    print("@: I'm escape simulator.")
    time.sleep(0.5)
    print("@: I'm here to teach you how it is to escape")
    time.sleep(0.5)
    print("@: So shall we start the simulator?")
    time.sleep(0.5)
    print("1. Yes")
    time.sleep(0.5)
    print("2. No")
    time.sleep(0.5)
    print(" ")
    print(67 * "-")
    print(" ")
    run()

def run():
    start_sim = console.check_answer("Will you start the sim?: ", ["1", "yes", "y", "2", "no", "n"]).lower()
    if start_sim == ("1") or start_sim == ("yes") or start_sim == ("y"):
        print("Nyaaa")
        Sim_start()
    elif start_sim == ("2") or start_sim == ("no") or start_sim == ("n"):
        print("@: Uhmmm...")
        print("@: Are you sure?")
        print("1. Yes")
        print("2. No")
        print(67 * "-")
        print(" ")
        run2()

def run2():
    sure = input("Are you sure?: ").lower()
    if sure == ("1") or sure == ("yes") or sure == ("y"):
        print("@: Ohhh bye then")
        print("You left the simulator alone without going on the adventure.")
        print("You never know what would have happened")
        print(67 * "-")
        print(" ")
        print("GAME OVER")
        print(" ")
        print("ENDING 1")
        print("Nope not going to do this")
        play_again()
    elif sure == ("2") or sure == ("no") or sure == ("n"):
        time.sleep(1)
        retry()
    else:
        print("Plz enter valid answer")


def retry():
    print("So do you want to start the simulator?")
    print("1. yes")
    print("2. no")
    retry_input = console.check_answer("start simulator?: ", ["1", "2", "yes", "y", "no", "n"]).lower()
    if retry_input == ("1") or retry_input == ("yes") or retry_input == ("y"):
        print(" ")
        Sim_start()
    elif retry_input == ("2") or retry_input == ("no") or retry_input == ("n"):
        print("@: ARE")
        time.sleep(0.5)
        print("@: YOU")
        time.sleep(0.5)
        print("@: KIDDING")
        time.sleep(0.5)
        print("@: ME!!!!!!!")
        time.sleep(3)
        print("Good job you made the program so pissed that it blow it self up.")
        print("Now you can't enter the simulator anymore.")
        print("GG player")
        print(67 * "-")
        print(" ")
        print("GAME OVER")
        print(" ")
        print("ENDING 2")
        print("BYE BYE SIMULATOR")
        play_again()

def Sim_start():
    print("hi")

def play_again():
    print("Do you want to restart the adventure or go back to menu?")
    print("1. Yes")
    print("2. No")
    print("3. Menu")
    again = input("Restart, quit or menu: ").lower()
    if again == ("1") or again == ("yes") or again == ("y") or again == ("restart"):
        print("Okay")
        print("Good luck on your next run")
        adventure()
    elif again == ("2") or again == ("no") or again == ("n") or again == ("quit"):
        quit()
    elif again == ("3") or again == ("menu") or again == ("m"):
        print("Lets go back")
        print(" ")
        print(67 * "-")
        print(" ")
    else:
        print("Plz enter valid answer")
        play_again()

# starts the game and menu
while start == True:
    Menu.print_menu(Menu)
    menu = console.check_answer("What do you want to do?", ["1", "intro", "start", "2", "skip", "quit", "3"])
    print(" ")
    if menu == ("1") or menu == ("intro") or menu == ("start"):
        intro()
    elif menu == ("2") or menu == ("skip"):
        adventure()
    elif menu == ("quit") or menu == ("3"):
        quit()