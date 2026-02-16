coinage = 0
# coinage = 7

def starting_room():
    global coinage
    sr_choice = input('''You look around the room some more. You've never actually seen a grandfather [clock] in person. You notice the taxidermied 
[raven] is holding something in it's beak and you're sure that [painting]s eye's are following you.\n\n''').lower()

    if sr_choice == "raven":
        print('''\nYou take a closer look at the raven, it's got a coffee coin in it's beak. You pocket the coin and move on.
''')
        coinage += 1
    elif sr_choice == "clock":
        print('''\nYou walk up to the clock, mesmerized by the swinging pendulum. After watching it for a while you decide you should probably move on.
''')
    elif sr_choice == "painting" or sr_choice == "paintings":
        print('''\nThe massive oil painting towers over you, it's of a stern man in a Victorian suit, the eyes are definitely following you. 
You decide you should move on before it steals your soul or something.
''')
    else:
        print("\nYou decide to stop dilly dallying and get a move on.\n")


def hallway():
    global coinage
    hallway_choice = input("You want to check out the [view] but you feel you're waisting time and should probably just focus on progressing.\n\n").lower()

    if hallway_choice == "view":
        print('''\nYou decide it's no big deal, there's no time limit after all. You approach the window, you can see one of the 
groundskeepers trimming the hedges outside. You notice a coffee coin sitting on the windowsill that you couldn't see 
before. You pocket the coin, take in the view, and then move on.
''')
        coinage += 1
    else:
        print("\nYou decide the view from here is enough and move on.\n")


def doll_room():
    global coinage
    dr_choice = input('''Among the [doll]s there's a few other things that interest you. A [music] box, an empty [birdcage], and a cabinet 
that has an Alice in Wonderland themed sign on one of the door knobs.\n\n''').lower()

    if dr_choice == "doll" or dr_choice == "dolls":
        print('''\nYou've never understood the appeal of creepy dolls made of the most horrendous material known to man, unfinished porcelain. 
You shiver at the touch of touching one.
''')
    elif dr_choice == "music":
        print('''\nYou walk over to the music box, wind it up, and open to see what's inside. No spinning ballerina, but there 
is a coffee coin which you pocket.
''')
        coinage += 1
    elif dr_choice == "birdcage":
        print('''\nYou walk over to the tiny cage, you hope nothing has ever actually been placed inside. You've always found caging
a bird was cruel, especially when it's in such inadequate space. You notice a few coffee coins in the bottom tray but 
your only able to retrieve two of them.
''')
        coinage += 2
    else:
        print("\nYou really just want to see what the sign says.\n")


def stairway():
    global coinage
    sw_choice = input('''The creepiest of which are the picture of the young girl with a stuffed [rabbit], the sleeping [baby], the [family] of farmers, and the [woman] in a fancy dress.\n\n''').lower()

    if sw_choice == "rabbit":
        print('''\nOddly just as cute as it is disturbing. There's a coffee coin taped to the wall beside it that you successfully remove without 
damaging the paint.
''')
        coinage += 1
    elif sw_choice == "baby":
        print("\nYou hope it's actually sleeping but you know it's more likely this was taken post-mortem.\b")
    elif sw_choice == "family":
        print("\nAbsolutely apathetic. Disturbing so.")
    elif sw_choice == "woman":
        print("\nYou think about how far fashion has come. How it's more accessible now but lacks quality or inspiration.")
    else:
        print('''\nThey all look extremely haunted and you feel if you look too closely they'll look back so you rush down the 
stairs as quickly as possible.''')


def study():
    global coinage
    st_choice = input('''\nYou wonder if you should look closer at the [globe], the [books] that haven't been put back on the 
shelves yet, the [maps] on the desk or head straight for the computer.\n\n''').lower()

    if st_choice == "globe":
        print('''\nAs you get closer the hum gets louder, you notice a coffee coin on the rim that goes around the center. 
You pocket it and head over to the computer.
''')
        coinage += 1
    elif st_choice == "books":
        print('''\nOne book is about Quantum Mechanics, another on Inter-Universal Teichmüller Theory, they all seem a little 
above your comprehension. You decide to move on and figure your next stop should be the computer.
''')
    elif st_choice == "maps":
        print('''\nYou don't recognise any of the maps, you're not even sure if they're of this world or fictional. 
        
You rummage through them for a while, pocket two coffee coins, and then turn your attention to the computer.
''')
        coinage += 2
    else:
        print("\nYou walk over to the desk, push the maps to the side and give your focus to the computer.\n")

def update_coinage(new_game):
    global coinage
    if new_game:
        coinage = 0

# starting_room()
# hallway()
# doll_room()
# stairway()
# study()
# print(coinage)