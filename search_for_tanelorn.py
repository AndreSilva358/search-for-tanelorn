print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
''''''''''''''''''''''''''''''''''''''''''''''''
def start_game():
    print("Welcome to the Search for Tanelorn")

    print("You find yourself standing at a crossroad.")
    print("To your left is a dark forest, to your right is a haunted castle.")
    print("Straight ahead is a winding path leading into a foggy valley.")
    print("What do you do?")
    
    choice = input("Enter 'left' to go to the dark forest, 'right' to enter the haunted castle, 'straight' to follow the winding path, or 'stay' to not choose any option: ").lower()
    
    if choice == "left":
        forest()
    elif choice == "right":
        mansion()
    elif choice == "straight":
        valley()
    elif choice == "stay":
        print("You decide to stay put. Nothing happens.")
    else:
        print("Invalid choice. Please try again.")
        start_game()

def forest():
    print("You enter the dark forest.")
    print("After walking for a while, you encounter a clearing with three paths.")
    print("One path is covered in thorns, another is shrouded in mist, and the third is overgrown with vines.")
    print("What do you do?")
    
    choice = input("Enter 'thorns' to take the path with thorns, 'mist' to take the misty path, 'vines' to take the path overgrown with vines, or 'return' to go back to the crossroad: ").lower()
    
    if choice == "thorns":
        print("You get scratched by the thorns and lose your way. Game over.")
    elif choice == "mist":
        print("The mist becomes thicker and thicker until you can't see anything. Game over.")
    elif choice == "vines":
        print("You struggle through the vines and eventually emerge into a beautiful meadow. You find a treasure chest!")
    elif choice == "return":
        start_game()
    else:
        print("Invalid choice. Please try again.")
        forest()

def mansion():
    print("You cautiously approach the spooky castle.")
    print("As you step inside, the door creaks shut behind you.")
    print("You find yourself in a dimly lit hallway with three doors.")
    print("One door has a skull engraved on it, another has a spider web, and the third has a bat hanging above.")
    print("What do you do?")
    
    choice = input("Enter 'skull' to open the door with the skull, 'spider' to open the door with the spider web, 'bat' to open the door with the bat, or 'leave' to exit the mansion: ").lower()
    
    if choice == "skull":
        print("You open the door and are immediately greeted by a swarm of bats. Game over.")
    elif choice == "spider":
        print("A giant spider descends from the ceiling and traps you in its web. Game over.")
    elif choice == "bat":
        print("You open the door and find a room filled with treasures!")
    elif choice == "leave":
        start_game()
    else:
        print("Invalid choice. Please try again.")
        mansion()

def valley():
    print("You follow the winding path into the foggy valley.")
    print("After some time, you come across a mystical pond with three glowing stones.")
    print("One stone is red, another is yellow, and the third is blue.")
    print("What do you do?")
    
    choice = input("Enter 'red' to touch the red stone, 'yellow' to touch the yellow stone, 'blue' to touch the blue stone, or 'continue' to keep walking through the valley: ").lower()
    
    if choice == "red":
        print("The red stone burns your hand. Game over.")
    elif choice == "yellow":
        print("The yellow stone emits a blinding light. Game over.")
    elif choice == "blue":
        print("You touch the blue stone and feel a surge of power coursing through you.")
    elif choice == "continue":
        print("You continue walking through the valley.")
        print("Eventually, you reach the end and find a beautiful garden.")
    else:
        print("Invalid choice. Please try again.")
        valley()

start_game()
