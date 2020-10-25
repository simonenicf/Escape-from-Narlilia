import sys
import time
import random
from menu import Menu
from game_engine import Console, Player

console = Console()
player = Player()
start = True
basement_suprise = ["demon", "open", "closed", "bear"]
choice = " "
name = " "
start_sim = " "
enter = " "
retry_input = " "
wake_up = " "
escape = " "
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
    print("The war is getting so out of hand that the civilians are starting to attack you for being befriend with the leader of the resistance.")
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

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# End part 0
# Start part 1
def Sim_start():
    print("You hear a dull beep noise.")
    print("It sounds like your alarm is going of.")
    print("So what will you do?")
    print("1. Wake up.")
    print("2. Go back to sleep.")
    print("3. Throw your alarm out of the window.")
    wake_up = console.check_answer("while you go back to sleep or wake up: ", ["1", "wake up", "2" , "sleep", "3", "throw"]).lower()
    if wake_up == "1" or wake_up == "wake up":
        print("You wake up and turn of your alarm.")
        print("You look at the time and you see that its 10.00 am.")
        print("You get up out of bed and get yourself ready.")
        print("Outside you hear the occasional screaming of people and gunshots being fired in the far distance.")
        print("You are kind of getting sick of this.")
        print("You go down stairs to get some breakfast.")
        print("When you got down stairs you see some shady people sitting in your living room.")
        shady_people()
    elif wake_up == "2" or wake_up == "sleep":
        print("zzzzzz")
        print("zzzzzzzzzzzzzzz......")
        print("You hear suddenly a loud scream.")
        print("???: He you lazy peace of shit wake the fuck up!!!!")
        print("That immediately wakes you up.")
        print("You look around and then you see your best friend standing by your bed trying to wake up.")
        print("Her name is Monika and she is the leader of the local resistance group.")
        print("Monika: Ah you finnally awake.")
        print("Monika: That took you long enough.")
        print("You ask what is going on and why she woke you up.")
        print("Monika: There is no time to explain.")
        print("Monika: We need to get out of here right the fuck now.")
        print("You do what Monika tells you.")
        print("You quickly put on some clothes and leave your house through the back door.")
        quick_escape()
    elif wake_up == "3" or wake_up == "throw":
        print("You grab your alarm and throw it out of the window.")
        print("The alarm hits the head of a unexpect civilian.")
        print("People though it was a bomb you throw out so they throw a grenade back to you.")
        print("*booooooooommmmmm*")
        print("You got hit by the explosion and died instantly.")
        print(67 * "-")
        print(" ")
        print("GAME OVER")
        time.sleep(1)
        print(" ")
        print("ENDING 3")
        print("Unexpected event")
        time.sleep(1)
        console.check_answer("Plz press enter to continue.")
        play_again()
    
def shady_people():
    print("You look again and see its your best friend Monika and some friends of her.")
    print("Monika is the leader of the resitance in your neighborhood.")
    print("You start asking what they are doing here.")
    print("Monika: We are here to warn you that there are some people after you.")
    print("Monika: And its is the best that you get out of here.")
    print("Monika: The country is not safe anymore for you.")
    print("Monika: The found out that you're befriend with me.")
    print("You ask her what you need to do and if your family is safe.")
    print("Monika: We have prepared for you a escape route you can take to get out of here.")
    print("Monika: And don't worry about your family they are safe.")
    print("Monika: I know some people that can help you leave the country.")
    print("Monika's phone goes of.")
    print("Monika picks up the phone and start talking to the person on the phone.")
    print("After a few minutes of Monika being on the phone.")
    print("Monika look at you and signs that you need to leave")
    print("You know something bad is going to happen.")
    print("How will you leave or will you hide?")
    print("1. Front door.")
    print("2. Back door.")
    print("3. Hide in the basement")
    escape = console.check_answer("what do you do?: ", ["1", "2", "3", "front", "back", "hide"]).lower()
    if escape == "1" or escape == "front":
        print("You quickly make your way towards the front door.")
        print("")
    elif escape == "2" or escape == "back":
        print("")
    elif escape == "3" or escape == "hide":
        print("You quickly make your way to your basement door.")
        print("You open you basement door and go down into your basement.")
        print("You pick up a heavy piece of wood you found on the ground and try to block the door with it.")
        print("You wait a while in the basement.")
        basement()

def basement():
    choice = random.choice(basement_suprise)
    if choice == "bear":
        print("You feel like someone is breathing in your neck.")
        print("You slowly turn around in the dark basement to check what it is.")
        print("You put your hands forward to feel what it is.")
        print("It feels really fluffy and fur like.")
        print("Wait a second you think to yourself.")
        print("It would have impossible that that bear you locked up here a few days weeks ago is still right.")
        print("Will your are thinking about it the bear is getting ready to murder you")
        print("*slash* And there you go.")
        print("Killed by a bear.")
        print("R.I.P. " + player.get_name(name) + ".")
        print(67 * "-")
        print(" ")
        print("GAME OVER")
        time.sleep(1)
        print(" ")
        print("ENDING BEAR")
        print("schrödinger bear")
        time.sleep(1)
        console.check_answer("Plz press enter to continue.")
        play_again()
    elif choice == "demon":
        print("You are alone down in the basement.")
        print("You suddenly hear a voice coming from the dark corner of the room.")
        print("Co...me.... wi....th.. u...s....")
        print("You were pretty sure that there is nothing else down here..... RIGHT????")
        print("You feel chill flowing down your spine.")
        print("You know there is something down here. There has to be right......")
        print("You starting to panic and don't know what to do.")
        print("The panic is so overwhelming that you feel like that you don't want to be here anymore.")
        print("You lose consciousness.")
        print(67 * "-")
        print(" ")
        print("GAME OVER")
        time.sleep(1)
        print(" ")
        print("ENDING 666")
        print("Demonic take over")
        time.sleep(1)
        console.check_answer("Plz press enter to continue.")
        play_again()
    elif choice == "open":
        print("After hiding in the basement for a while you hear some people entering your house.")
        print("Angery man: Hey " + player.get_name(name) + "we know your in here.")
        print("You hear them going through your house.")
        print("You hope the are unable to find you.")
        print("You suddenly hear them kicking against the basement door")
        print("You hope the door can hold it.")
        print("Then you hear *bam* the door flies downwards right in your face.")
        print("The door knocks you unconscious.")
        print(67 * "-")
        print(" ")
        print("GAME OVER")
        time.sleep(1)
        print(" ")
        print("ENDING DOOR")
        print("Knock knock who is there?")
        print("The door")
        time.sleep(1)
        console.check_answer("Plz press enter to continue.")
        play_again()
    elif choice == "closed":
        print("After hiding in the basement for a while you hear some people entering your house.")
        print("Angery man: Hey " + player.get_name(name) + "we know your in here.")
        print("You hear them going through your house.")
        print("You hope the are unable to find you.")
        print("You suddenly hear them kicking against the basement door")
        print("You hope the door can hold it.")
        print("You hear this guy trying really hard to open up the door but the door won't budge.")
        print("Then you hear someone yell.")
        print("Angery man: Guys he is nowhere to be found lets move out.")
        print("You hear everyone that is upstairs leave.")
        print("You survived this stressfull ordeal.")
        escaped_basement()

def escaped_basement():
    print("succes")

def quick_escape():
    print(" ")

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
    Sim_start()
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