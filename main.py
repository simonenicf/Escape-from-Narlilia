import sys
import time
from menu import Menu
from game_engine import Console, Player

console = Console()
player = Player()
start = True
name = " "
start_sim = " "
enter = " "
retry_input = " "
bye = 0

# Function to exit the game
def quit():
    print("Okay bye")
    exit(0)

# put the intro here
def intro():
    print("You were invited by your friend to test his newest simulator.")
    time.sleep(1)
    print("He wanted to see how you would react on his invention.")
    time.sleep(1)
    print("Because he wanted to see how people would react on fleeing there own country.")
    time.sleep(1)
    print("And to discover how it is to trade a place you are familiar with for something new.")
    time.sleep(1)
    print("Far away from your friends and family.")
    time.sleep(1)
    print("So he created this simulator called escape simulator.")
    time.sleep(1)
    print("He told you the simulation will take place in a land called Narlilia.")
    time.sleep(1)
    print("The country is in constant war with the civilians.")
    time.sleep(1)
    print("The war is getting so out of hand that the civilians are starting to attack you for your believe.")
    time.sleep(1)
    print("You don't see a other way out anymore than to escape from the country.")
    time.sleep(1)
    print("The country you love and grow up in.")
    time.sleep(1)
    print("Will you manage to escape out of this country or fail horribly.")
    time.sleep(1)
    console.check_answer("Plz press enter to continue.")

    adventure()

def help():
    print(" ")
    print(67 * "-")
    print(" ")
    console.check_answer("Plz press enter to continue.")

# Start part 0
# Start adventure
def adventure():
    print("@: Is anybody there???: ")
    console.check_answer("Plz press enter to continue.")
    time.sleep(1)
    print("@: WHAAAAAA!!!!")
    time.sleep(1)
    print("@: Oh sorry. I didn't expect that you where here already.")
    time.sleep(1)
    player.set_name(console.check_answer("So what is our name user?"))
    print("@: Oh hi " + player.get_name(name) + ". It's nice to meet you.")
    time.sleep(1)
    print("@: I'm escape simulator.")
    time.sleep(1)
    print("@: I'm here to teach you how it is to escape the country you currently live in")
    time.sleep(1)
    print("@: So shall we start the simulator?")
    time.sleep(1)
    print("1. Yes")
    time.sleep(1)
    print("2. No")
    time.sleep(1)
    print(" ")
    print(67 * "-")
    print(" ")
    run()

def run():
    print(" ")
    time.sleep(1)
    start_sim = console.check_answer("Will you start the sim?: ", ["1", "yes", "y", "2", "no", "n"]).lower()
    if start_sim == ("1") or start_sim == ("yes") or start_sim == ("y"):
        print("Nyaaa")
        Sim_start()
    elif start_sim == ("2") or start_sim == ("no") or start_sim == ("n"):
        print("@: Uhmmm...")
        time.sleep(1)
        print("@: Are you sure?")
        time.sleep(0.5)
        print("1. Yes")
        time.sleep(0.5)
        print("2. No")
        time.sleep(0.5)
        print(67 * "-")
        print(" ")
        run2()

def run2():
    sure = console.check_answer("Are you sure?: ", ["1", "yes", "y", "2", "no", "n"]).lower()
    if sure == ("1") or sure == ("yes") or sure == ("y"):
        print("@: Ohhh bye then")
        time.sleep(0.5)
        print("You left the simulator alone without going on the adventure.")
        time.sleep(0.5)
        print("You never know what would have happened")
        time.sleep(0.5)
        print(67 * "-")
        print(" ")
        print("GAME OVER")
        print(" ")
        time.sleep(1)
        print("ENDING 1")
        print("Nope not going to do this")
        time.sleep(1)
        console.check_answer("Plz press enter to continue.")
        play_again()
    elif sure == ("2") or sure == ("no") or sure == ("n"):
        retry()

def retry():
    print(" ")
    print(67 * "-")
    print(" ")
    time.sleep(1)
    print("So do you want to start the simulator?")
    time.sleep(0.5)
    print("1. yes")
    time.sleep(0.5)
    print("2. no")
    time.sleep(0.5)
    retry_input = console.check_answer("start simulator?: ", ["1", "2", "yes", "y", "no", "n"]).lower()
    if retry_input == ("1") or retry_input == ("yes") or retry_input == ("y"):
        print(" ")
        Sim_start()
    elif retry_input == ("2") or retry_input == ("no") or retry_input == ("n"):
        print("@: ARE")
        time.sleep(0.5)
        print("@: YOU")
        time.sleep(0.3)
        print("@: KIDDING")
        time.sleep(0.2)
        print("@: ME!!!!!!!")
        time.sleep(3)
        print("Good job you made the program so pissed that it blow it self up.")
        time.sleep(1)
        print("Now you can't enter the simulator anymore.")
        time.sleep(1)
        print("GG player")
        time.sleep(1)
        print(67 * "-")
        print(" ")
        print("GAME OVER")
        time.sleep(1)
        print(" ")
        print("ENDING 2")
        print("BYE BYE SIMULATOR")
        time.sleep(1)
        console.check_answer("Plz press enter to continue.")
        play_again()

# End part 0
# Start part 1
def Sim_start():
    print("")


def play_again():
    print(" ")
    print(67 * "-")
    print(" ")
    print("Do you want to restart the adventure, go back to the menu or quit the game?")
    time.sleep(1)
    print("1. Restart")
    time.sleep(1)
    print("2. Quit")
    time.sleep(1)
    print("3. Menu")
    time.sleep(1)
    again = console.check_answer("Restart, quit or menu: ", ["1", "yes", "y", "restart", "2", "no", "n", "quit", "3", "menu", "m"]).lower()
    if again == ("1") or again == ("yes") or again == ("y") or again == ("restart"):
        print("Okay")
        print("Good luck on your next run")
        adventure()
    elif again == ("2") or again == ("no") or again == ("n") or again == ("quit"):
        quit()
    elif again == ("3") or again == ("menu") or again == ("m"):
        print("Lets go back to the menu")
        time.sleep(1)
        print(" ")
        print(67 * "-")
        print(" ")

# starts the game and menu
while start == True:
    Menu.print_menu(Menu)
    menu = console.check_answer("What do you want to do?", ["1", "intro", "start", "2", "skip", "quit", "3", "help", "4"])
    print(" ")
    if menu == ("1") or menu == ("intro") or menu == ("start"):
        intro()
    elif menu == ("2") or menu == ("skip"):
        adventure()
    elif menu == ("help") or menu == ("3"):
        help()
    elif menu == ("quit") or menu == ("4"):
        quit()