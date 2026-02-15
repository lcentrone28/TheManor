import random
import ledger
import password
import cipher
import areas
import handsofprov
import ledger
import coffee
import num_guess

game_finished = False

while game_finished == False:
# main variables
    game_over = False
    lucky = True
    lives = 1
    prize_amount = 0
    prize_amount_total = 0
    difficulty = ""
    achievements = {}

    # game variables
    hop_win = False
    hop_req = 0
    hop_req_str = ""

    ledger_win = False
    ledger_req = 0
    points = 0

    consensus_choice_made = False
    consensus_opponents = 0
    chosen_gem = ""
    chose_ruby = False
    chose_emerald = False
    greedy_players = 0
    winning_gem = ""
    many_greedy = False

    code_solved = False
    code_attempts = 0
    code_length = 0

    # password and cipher
    ## i understand that decrypted_password == random_password and so decrypted_password is unnecessary
    ## but for the sake of this project as a practice project i created it just to create it

    shift = random.randint(1,100)
    def determined_shift():
        return shift

    random_password = password.generate_password(8)
    encrypted_password = cipher.encrypt(random_password, shift)
    decrypted_password = cipher.decrypt(encrypted_password, shift)

    # print(random_password)
    # print(encrypted_password)
    # print(decrypted_password)

    while game_over == False and lives > 0:
        print('''\n\033[1m   _   _    _______ _            __  __                           _   _
  | | | |  |__   __| |          |  \\/  |                         | | | | 
 / __) __)    | |  | |__   ___  | \\  / | __ _ _ __   ___  _ __  / __) __)
 \\__ \\__ \\    | |  | '_ \\ / _ \\ | |\\/| |/ _` | '_ \\ / _ \\| '__| \\__ \\__ \\
 (   (   /    | |  | | | |  __/ | |  | | (_| | | | | (_) | |    (   (   /
  |_| |_|     |_|  |_| |_|\\___| |_|  |_|\\__,_|_| |_|\\___/|_|     |_| |_| \033[0m\n''')

        print('''You have been invited to The Manor to participate in a series of trials, sponsored by rich people with nothing 
better to do who like to bet on the contestants. There was a short, incredibly invasive, interview that you passed with 
flying colors. For a shot at $10,000 you didn't care if a bunch of randoms find out how often you wash your bedsheets 
and if you're religious, the character analysis was actually kinda fun. Like the biggest “What type of pasta are you?” 
quiz you could imagine. 
        
When you arrive at The Manor the butler, Niles, graciously welcomed you in and directed you to your corridor, he's now 
explaining the rules as you try not to get distracted by all the eclectic decor, failing miserably, and worse only 
realizing you failed when he hands you a note and you have no idea why. 
        
“Now then, I shall be off to show the next candidate to their section of the estate.” He states before beginning to walk 
out of the room. You stare at the note for a moment and then muster up the courage to ask for repetition. “I'm terribly 
sorry sir but can you please explain one more time just to make sure I understand.” You say as you look at him like a 
lost puppy. Niles smiles, “Of course, you did just win me $500 after all.” he chuckles then continues “You will navigate 
through those doors” he points at the door on the other side of the room “and into each of the rooms that follows. 
Completing a few harmless trials until you reach the final test. I cannot reveal anything to you except that the 
password on that paper must be altered before it can be used. If you fail a trial you will be excused and if you happen 
to find any of these coins” he pulls a unique coin out of his coat pocket, it's silver and has a coffee cup on it “I 
advise you take it with you.” Niles puts the coin back in his coat pocket and continues
''')

        first_input = input('"Okay then, I assume you understand now,\033[1m yes\033[0m?" Niles says as if it were a statement and not a question, \n\n').lower()

        if first_input == "yes" or first_input == "ya":
            print('''\nHe smiles again, puts the coin in his coat pocket, bows slightly, wishes you luck and begins to walk out. 
“Oh uh Niles?” you proclaim inquisitively “I assume you meant you bet on me earlier. How did you know I would need it 
explained again?” Niles turns back towards you “Well your favorite thing on a hot summer day is a Choco Taco from an 
ice cream truck, so naturally one can assume as much.” he swiftly turns back and leaves you with no more explanation 
than that. Puzzled how the two possibly connect you begin to look around.
''')
        elif first_input == "no":
            print('''\n"My apologies but I do not have the time to explained it more than twice." Niles states as he puts the coin in his coat 
pocket. He then wishes you luck and leaves you to it.
''')
            achievements['Absent Minded'] = "Still didn't understand Niles's explanation."
        else:
            print('''\n"I do not have the time to deal with your lack of decorum." Niles states as he puts the coin in his coat pocket, 
seemingly upset by your tomfoolery, he turns and leaves without another word.
''')
            achievements['No Couth'] = "Upset Niles with your lack of decorum."

        # print(achievements)

        areas.starting_room()

        print('''You exit the first room into a hallway, smaller than the other hallways in the rest of the house but still bigger 
than most hallways in average homes. There is one room across from you, a window to the right of you and stairs leading 
down to the left of you.
''')

        areas.hallway()

        print('''You approach the big antique door and open to find a dizzying gallery of Victorian curiosities, less interesting than the last room, 
way more creepy. Porcelain dolls with fixed glass stares watch you from every corner. The air is thick with the 
scent of lavender and old lace.
''')

        areas.doll_room()

        print('''You approach the cabinet, “Open Me” it insists. You oblige, a mechanical hand springs to life as soon as you open the doors. 
“Welcome to the Hand of Providence” an unrecognized voice from seemingly nowhere states “I will be your game master, 
watching your every move for our investors. The is a simple game of Rock, Paper, Scissors. And your first real decision. 
You are currently playing for a chance at $10,000, but what if I told you you could win, 20, 30, or even 50 thousand 
dollars?” the voice excitedly exclaims. “How?” you reply, simple and sweet because you can't conjure up much of anything 
else. “Well this is a betting game after all. Now's the time for you to bet on yourself!” the voice continues “You can 
continue as is and have the opportunity at the previously promised $10,000 or you can up the ante and go for the 20, 30, 
or 50 thousand dollar marks, just know the completion requirements will be higher as well." 
''')

        diff_choice_made = False

        while diff_choice_made == False:
            diff_choice = input('''He pauses for a moment and then, as if he expected an answer already, asks you “So how good do you think you are? 
How much would you like to wager?\033[1m 10, 20, 30,\033[0m or\033[1m 50\033[0m thousand dollars?"\n\n''').lower()

            if diff_choice == "10" or diff_choice == "10,000" or diff_choice == "$10,000" or diff_choice == "10k" or diff_choice == "$10k":
                difficulty = "easy"
                lives = 9999
                hop_req = 2
                hop_req_str = "2/3"
                ledger_req = 2
                consensus_opponents = 2
                code_attempts = 9999
                code_length = 2
                prize_amount = 10000
                diff_choice_made = True
            elif diff_choice == "20" or diff_choice == "20,000" or diff_choice == "$0,000" or diff_choice == "20k" or diff_choice == "$20k":
                difficulty = "normal"
                lives = 9
                hop_req = 3
                hop_req_str = "3/5"
                ledger_req = 3
                consensus_opponents = 3
                code_attempts = 50
                code_length = 4
                prize_amount = 20000
                diff_choice_made = True
            elif diff_choice == "30" or diff_choice == "30,000" or diff_choice == "$30,000" or diff_choice == "30k" or diff_choice == "$30k":
                difficulty = "hard"
                lives = 5
                hop_req = 5
                hop_req_str = "5/9"
                ledger_req = 5
                consensus_opponents = 5
                code_attempts = 25
                code_length = 4
                prize_amount = 30000
                diff_choice_made = True
            elif diff_choice == "50" or diff_choice == "50,000" or diff_choice == "$50,000" or diff_choice == "50k" or diff_choice == "$50k":
                difficulty = "insane"
                lives = 1
                hop_req = 7
                hop_req_str = "7/13"
                ledger_req = 7
                consensus_opponents = 9
                code_attempts = 25
                code_length = 6
                prize_amount = 50000
                diff_choice_made = True
            else:
                print("\nMy apologies I didn't quite get that. Mind repeating?\n")

        # print(difficulty)
        # print(lives)
        # print(hop_req)
        # print(ledger_req)
        # print(consensus_opponents)
        # print(code_attempts)
        # print(code_length)

        code_str = ""
        first_number = 0

        for i in range(code_length):
            digit = str(random.randint(1, 9))
            code_str += digit

            if i == 0:
                first_number = int(digit)

        first_number = int(code_str[0])
        code = int(code_str)

        # print(code)
        # print(first_number)

        print(f'''\n“Splendid!” The voice proclaims “Now that that matter has been settled we can get on with our first trial, 
you will compete against the Hand of Providence in a classic\033[1m rock, paper, scissors\033[0m battle.”
        
“Since you chose to face these trials on {difficulty} difficulty you must best The Hand {hop_req_str} times, you can start whenever 
you're ready. It will automatically make its choice when it senses your movement and I will record the results. 
May the odds be in your favor.”

You stare at the hand, wondering how it works, you assume the game master tells it to do whichever action but you 
decide it would be way cooler to give it sentience and imagine yourself up against a great mechanical foe. You try to 
anticipate this great foe's first move and plan accordingly.

"I know I said start whenever but can you start sooner rather than later?" the game master interrupts your imaginary 
plot to so rudely tell to you to hurry up and make a choice. You move your hand to assume the first position to see if 
the hand responds, then change it at the last second to..''')

        while not hop_win and not game_over:
            hop_win, lives = handsofprov.hop_game(hop_req, lives)

            # print(lives)

            if not hop_win:
                achievements['Strategy Deficit'] = "Successfully bested by the mechanical hand."
                lucky = False
                lives -= 1
                if lives >= 1:
                    print('''\n"It seems The Hand has bested you, we would hate for the game to be over so soon. Go ahead and try again.” states 
the game master.''')
                elif lives <= 0:
                    print('''\n"Unfortunately, that's a wrap. You can exit back through where you came in since you didn't make it very far at all. 
Better luck next time.” States the game master.''')
                    game_over = True

        if game_over == True:
            break

        print('''\nYou valiantly defeat the great mechanical foe and continue on your quest for greatness. You exit the room the way you came and turn to 
your right, heading down the stairway with tons of creepy pictures.\n''')

        areas.stairway()

        print('''At the end of the stairway there's a large oak door. Inside, the walls stretch well above where they should and are lined 
with books. A massive celestial globe in the center hums with a low, electric vibration.''')

        areas.study()

        # print(areas.coinage)

        print('''You wake it up by clicking the space bar on the keyboard. There is a program already loaded up. Across the top 
in big bold lettering it reads "The Global Ledger", and below that in regular lettering "Check your understanding with 
our database of interesting facts! Compare the first statistic and guess if it's higher or lower than the second. 
See how many you can get in a row and challenge your friends to best you!" It seems simple enough but you're not too 
confident that you'll know anything, hoping luck will be on your side you press the start button below all the text.

The game loads up and presents you with two options to compare.''')

        while not ledger_win and not game_over:
            ledger_win, lives, points = ledger.ledger_game(ledger_req, lives)

            # print(lives)

            if not ledger_win:
                achievements['Statistical Anomaly'] = "Failed the Trial of the Global Ledger."
                lucky = False
                lives -= 1
                if lives >= 1:
                    print('''\n"It seems The Global Ledger has bested you, we would hate for the game to end here. Go ahead and try again.” 
states the game master.''')
                elif lives <= 0:
                    print('''\n“Unfortunately, that's a wrap.” States the game master, a bookshelf to the right of the desk moves and reveals a door “You can exit 
through the door to the right. Better luck next time.”''')
                    game_over = True

        if game_over == True:
            break

        print(f'''\nThe screen updates and shows your score, you got {points} correct, proving you’re not just looks. It must've been a high 
enough score because a bookshelf behind you moves and reveals a small door. You go through the door and enter a small 
passageway. It's the first area that doesn’t have any decorations, only a table to the left and a glass door at the end. 

On the table there is a note and two pendants. The note states that the red pendant on the left is a\033[1m ruby\033[0m and 
is for those who wish to share the victory, while the green pendant on the right is an\033[1m emerald\033[0m and is for those 
who wish to take it all. It explains that you must choose one to carry with you into the next challenge and that the 
other participants gathered here today will also face the same choice. By choosing the ruby you stand in solidarity 
with your peers, everyone who passes the trials gets to enjoy “the fruits of their labor” as the note calls it. By 
choosing the emerald you are attempting to steal all the prizes for yourself. You realize that could turn out to be a 
very hefty sum, especially if any of the other participants completed the trials on a higher difficulty, but you wonder 
why it chose the wording it did. Attempting to steal implies you can fail, presumably if others choose the same.
''')


        while not consensus_choice_made:
            chosen_gem = input("You choose the..\n\n").lower()

            if chosen_gem == "ruby" or chosen_gem == "emerald":
                consensus_choice_made = True
            else:
                print("You need to choose,\033[1m ruby\033[0m or\033[1m emerald\033[0m.")

        if chosen_gem == "ruby":
            chose_ruby = True
        else:
            chose_emerald = True

        if difficulty == "easy":
            consensus_choices = ["emerald", "ruby", "ruby", "ruby", "ruby", "ruby", "ruby", "ruby", "ruby", "ruby", "ruby", "ruby", "ruby", "ruby", "ruby"]
        elif difficulty == "normal" or difficulty == "hard":
            consensus_choices = ["emerald", "ruby", "ruby", "ruby", "ruby", "ruby", "ruby", "ruby", "ruby", "ruby"]
        elif difficulty == "insane":
            consensus_choices = ["emerald", "ruby", "ruby", "ruby", "ruby"]

        for i in range(consensus_opponents):
            choice = random.choice(consensus_choices)
            if choice == "emerald":
                greedy_players += 1

        if greedy_players >= 2:
            many_greedy = True

        if greedy_players == 1:
            winning_gem = "emerald"
        else:
            winning_gem = "ruby"

        print(f'''\nYou pocket the {chosen_gem} and venture onward through the glass door, it swings closed and then automatically locks. 

You look around the glass room, the sun shining in from above feels good on your skin. The room is full of plants and 
strangely enough, a coffee machine and computer desk. It’s an odd pairing but you imagine it was originally built for 
someone who just wanted to work outside but was tethered to their desk, you think about how once you get this money 
you’ll have the freedom to make your dreams come true just like this imaginary person did.
''')

        coffee.run_coffee(areas.coinage, first_number)

        if coffee.chose_mocha == True:
            achievements['Coffee Connoisseur'] = "Purchased the Mochaccino."

        print(f'''You walk over to the desk. There’s a computer, an interesting lock box with a {code_length} digit code needed to open it, 
and some pens in a cup. It’s definitely vintage and maybe even haunted. You pick up the box and start fiddling with 
the combination. You move each dial to the lowest possible number so it reads {"1" * code_length}, it beeps at you two times. You mess 
with it some more and try all 9s, this time it only beeps once. You infer that one beep must mean the code is lower than 
your guess and two must mean it's higher.
''')
        # print(code)

        while not code_solved and not game_over:
            code_solved, lives = num_guess.code_game(code, code_attempts, lives)

            # print(lives)

            if not code_solved:
                achievements['Security Breach'] = "Failed to unlock the Conservatory Code in time."
                lucky = False
                lives -= 1
                print('''"You still working on that?“ says the game master, snarkily"''')
            elif lives <= 0:
                print('''The game master returns "Unfortunately you exceeded the amount of allowed attempts, I mean we can't just let you fool 
with it all day, there are other participants waiting for you to finish after all. Such a shame, you made it so far 
just to have a silly little number guessing game be your doom. Kinda embarrassing if you ask me but we thank you for 
playing nonetheless. Hang out, enjoy a cup of coffee while you wait, Niles will retrieve you shortly.”''')
                game_over = True

        if game_over == True:
            break

        print(f'''You take out the note you got at the begging of the game, it reads "\033[1m{encrypted_password}\033[0m", you remember Niles called it a password 
and said it must be altered before it can be used, "Maybe I'm supposed to enter this into this little machine?” you 
say under your breath, finishing your thought out loud.
''')
        password_decrypted = False

        while password_decrypted == False:
            decrypt_attempt = input("").upper()

            # print(decrypt_attempt)

            if decrypt_attempt != encrypted_password:
                print('''\nThe screen flashes "TRY AGAIN" a few times and then goes back to "READY FOR INPUT". You're sure the password goes into 
this machine so you try again, ensuring to type it exactly as it is written on the note.
''')
            else:
                print(f'''\nThe screen displays a new password "\033[1m{decrypted_password}\033[0m". You grab a pen from the desk and write it below the old password on the note.
''')
                password_decrypted = True

        print('''You set the little machine back down on the desk and turn your attention to the computer. The actual computer part is 
laying on it's side instead of standing upright like every other computer you've seen, the monitor is stationed on top 
of it. "Very strange" you think before moving the mouse to wake it up. The black screen turns into a lush green background 
filled with foliage, the only shortcuts on the desktop are an empty recycling bin and something called "Gem Scanner".
''')

        # decrypted_password = "test"

        password_input = input("You click on Gem Scanner and it prompts you for a password.\n\n").upper()

        password_entered_incorrectly = False

        if password_input != decrypted_password:
            password_entered_incorrectly = True

        while password_entered_incorrectly == True:
            print("\nThe password field empties and a red line of text below it appears, politely informing you the password is incorrect.")
            password_input = input("You re-enter the password.\n\n").upper()

            if password_input == decrypted_password:
                password_entered_incorrectly = False

        print('''\nThe computer pops open a tray, I guess it wasn't laying on its side after all, such a strange contraption.
         
On screen you are instructed to put your pendant inside the tray and close it, you follow the instructions and the 
computer thanks you. Such a well mannered program you think. It makes some strange noises and then prints out a slip 
of paper. 

On screen it advises you that your choice has been recorded, your receipt has been printed, congratulates you on your 
completion of the game, and informs you to wait for further instructions. 

You wait patiently, first sitting still in place, then wandering around a bit, before too long Niles opens the door 
adjacent to the one you entered the room through. 

He smiles and bows “Congratulations on completing the Hand of Providence, the Global Ledger, and the Conservatory Code.” 
he returns to a normal standing position “I must say, your choice for the Consensus Conundrum was unexpected. I will 
now bring you to the game room where you can relax and unwind while you wait for the other participants to finish and 
the winners to be determined. And just to ensure you understand fully, the NDA you signed at your interview includes 
other participants, so please for your sake and the sake of the competition do not discuss today's activities or 
outcomes with anyone including other contestants.” he swiftly turns on his heels back towards the door from which he 
came “Come along then” he says before departing. 

You follow close behind as he tells you of all the amenities the game room has. Everything from billiards to arcade 
machines to shuffleboards, whatever shuffleboard is. Apparently there's even high tech VR machines like the roller 
coaster simulators at arcades. But you're most excited for the open snack bar. Even if you don't end up winning 
anything you'll make it worth your while and get your pay in Snickers, Cheetos, and Diet Coke.
''')

        # prize_amount_total = "$10,000"
        # winning_gem = "ruby"
        # winning_gem = "emerald"
        # chose_ruby = True
        # chose_emerald = True
        # many_greedy = True
        # greedy_players = 3

        possible_participant_winnings = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 20000, 20000, 20000, 20000, 20000, 20000, 30000, 30000, 50000]
        participant_winnings = []

        for i in range(consensus_opponents):
            p_winnings = random.choice(possible_participant_winnings)
            participant_winnings.append(p_winnings)

        if winning_gem == "emerald" and many_greedy == False:
            winner_tense = " is"
        else:
            winner_tense = "s are"

        print(f'''After walking for what felt like an eternity you finally reached the game room. You tell Niles he should get a 
step counter, he chuckles and says it would just become another variable to bet on if he did and tells you to enjoy 
yourself. You look around the game room, it’s everything Niles said it would be and more. 
        
You grab yourself a king size Snickers and play some pinball. You try out one of the VR games but it makes you queasy 
so you decide best not to mess with those anymore. You brutally lose against your fellow participants in air hockey and 
decide as consolation you’ll have an entire family sized bag of crunchy Cheetos and a 2 liter of Diet Coke. 
        
As you're sitting at one of the tables in one of the comfiest chairs you’ve ever placed your behind in, Niles returns 
“Thank you all for waiting so patiently. I'm sure you all are more than ready to hear the results from the final trial, 
the Consensus Conundrum, so without further ado the winner{winner_tense}..."
''')

        if greedy_players > 2:
            plural = "s"
        else:
            plural = ""

        if winning_gem == "ruby":
            if many_greedy == False:
                print(f'''Niles creates a drumroll effect by tapping on a nearby surface "The ruby bearers! Congratulations everyone, this is my 
favorite of all the outcomes, it truly warms my heart to see. You are free to hang out and enjoy yourselves here for a 
little longer if you’d like, whenever you are ready to leave please come see me and exchange your receipt for your earnings.” 
        
You hang out until you reach your social battery and trade Niles your receipt for your prize. He bids you a farewell 
and you are sent on your way, having had an unforgettable experience, gained some new friends, and a more than decent 
chunk of change, ${prize_amount:,} to be precise. You cant help but smile from ear to ear the whole ride home thinking about 
all the fun you had and all the possibilities the future holds.
''')
            elif many_greedy == True:
                print('''Niles creates a drumroll effect by tapping on a nearby surface “The ruby bearers! Congratulations everyone that chose ruby, 
unfortunately there were a few of you that tried to steal but failed. If you chose emerald please bring me your receipts 
and excuse yourselves, we can’t have you spoiling the party for everyone else. If you chose ruby you are free to hang 
out and enjoy yourselves here for a little longer if you’d like, whenever you are ready to leave please come see me and 
exchange your receipt for your earnings, there will be a little extra than expected since the emerald bearers earnings 
are forfeit.”
''')
                if chose_ruby == True:
                    if greedy_players != consensus_opponents:
                        forfeited_winnings = 0

                        for i in range(greedy_players):
                            forfeit = random.choice(participant_winnings)
                            forfeited_winnings += forfeit

                        split = consensus_opponents - greedy_players

                        split_up = forfeited_winnings // split

                        prize_amount_total = prize_amount + split_up
                    else:
                        forfeited_winnings = sum(participant_winnings)

                        prize_amount_total = prize_amount + forfeited_winnings
                        achievements['Last of Us'] = "The only player to choose the ruby."
                    print(f'''You hang out until you reach your social battery and trade Niles your receipt for your prize. He bids you a farewell 
and you are sent on your way, having had an unforgettable experience, gained some new friends, and a more than decent 
chunk of change, ${prize_amount_total:,} to be precise. You cant help but smile from ear to ear the whole ride home thinking about 
all the fun you had and all the possibilities the future holds.
''')
                    achievements['Pure Integrity'] = "Faith in the collective pays off."
                elif chose_ruby == False:
                    print(f'''You and the other emerald bearer{plural} stand up and give Niles your receipts, he thanks you for playing, and sends you 
on your way. You shot for the sun and burnt up like Icarus, you can hear the others still having fun as you walk down 
the hallway in silence towards the exit. You wonder if they’ll give you another chance and if they do if you’ll do 
anything different.
''')
                    achievements['Unsportsmanlike Conduct'] = "Double the greed equals none of the prize."

        elif winning_gem == "emerald":
            print('''Niles creates a drumroll effect by tapping on a nearby surface “The emerald bearer. If you chose the emerald please come 
see me and exchange your receipt for your stolen earnings. Everyone else, we have 20 extra large pizzas that will be 
here shortly and there will be movies running in the theater until midnight, you are free to hang out and enjoy yourselves 
until then if you’d like and we do hope you’ll return if invited for another go at it. Thank you all for playing”
''')
            if chose_emerald == True:
                forfeited_winnings = sum(participant_winnings)

                prize_amount_total = prize_amount + forfeited_winnings
                print(f'''You stand up and walk towards Niles, you can feel your fellow contestants eyes piercing you like daggers, you all were 
having so much fun before you actually feel a bit guilty now. You hand Niles your receipt and he instructs you to follow 
him. He writes you a check for ${prize_amount_total:,}, informs you that you will never be invited back, and sends you 
on your way. You feel bad for the others but they’re having a blast now regardless and might even get another shot so 
it’s really not all bad for them either. Your attention quickly moves from the guilt you feel to how you're gonna spend 
sooooo much money. 
''')
            elif chose_emerald == False:
                print('''You hang out until you reach your social battery and bid Niles a farewell, he informs you that the investors were pleased 
with your performance and you will most likely be asked to return. This takes a substantial amount of the sting out of 
the loss and allows you to just enjoy the experience for what it was.
        ''')
                achievements['Betrayed Trust'] = "You opted for the Ruby of Solidarity but they could only see green."

        game_over = True

    if game_over == True:
        if lives > 0:
            print('''\n\n✦•·································•✦•·································•✦
    
Congratulations on completing
\033[1m   _   _    _______ _            __  __                           _   _
  | | | |  |__   __| |          |  \\/  |                         | | | | 
 / __) __)    | |  | |__   ___  | \\  / | __ _ _ __   ___  _ __  / __) __)
 \\__ \\__ \\    | |  | '_ \\ / _ \\ | |\\/| |/ _` | '_ \\ / _ \\| '__| \\__ \\__ \\
 (   (   /    | |  | | | |  __/ | |  | | (_| | | | | (_) | |    (   (   /
  |_| |_|     |_|  |_| |_|\\___| |_|  |_|\\__,_|_| |_|\\___/|_|     |_| |_| \033[0m
    
✦•·································•✦•·································•✦
''')

            if difficulty == "easy":
                achievements['Junior Finalist'] = "Successfully beat the game on Easy difficulty."
            elif difficulty == "normal":
                achievements['Proven Candidate'] = "Successfully beat the game on Normal difficulty."
            elif difficulty == "hard":
                achievements['Professional Competitor'] = "Successfully beat the game on Hard difficulty."
            elif difficulty == "insane":
                achievements['Grandmaster Champion'] = "Successfully beat the game on Insane difficulty."

            if lucky == True:
                achievements['The Untouchable'] = "Completed the entire tournament without losing a single life."

        else:
            print('''\n\n✦•·································•✦•·································•✦
    
You were dismissed from
\033[1m   _   _    _______ _            __  __                           _   _
  | | | |  |__   __| |          |  \\/  |                         | | | | 
 / __) __)    | |  | |__   ___  | \\  / | __ _ _ __   ___  _ __  / __) __)
 \\__ \\__ \\    | |  | '_ \\ / _ \\ | |\\/| |/ _` | '_ \\ / _ \\| '__| \\__ \\__ \\
 (   (   /    | |  | | | |  __/ | |  | | (_| | | | | (_) | |    (   (   /
  |_| |_|     |_|  |_| |_|\\___| |_|  |_|\\__,_|_| |_|\\___/|_|     |_| |_| \033[0m
    
Better luck next time!!!
    
✦•·································•✦•·································•✦
''')

    print("You earned the following achievements:\n")

    for key, value in achievements.items():
        print(f"\u2022 {key}: {value}")

    replay_answered = False

    while replay_answered == False:
        replay = input("\nWould you like to play again?\n\n").lower()

        if replay == "no":
            print('''
\033[1mThanks for playing my game, hope it was as much fun to play as it was to make!\033[0m
               
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠶⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡴⠞⠳⠶⠦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠋⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠉⠳⣦⡀⠀⠀⠀⠀⠀⠀⣤⡾⠿⣷⠀⠀⠀⢠⡞⠁⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠀⣤⠤⠼⢤⡿⠃⠀⠼⠟⠻⠿⡤⠛⠀⠀⠀⠀⣠⣼⣤⣀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡇⠀⠀⣴⠖⠒⢶⡦⠀⠀⠀⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠁⠀⠠⠀⠀⠻⣦⣄⣹⡄⠀⢹⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡄⠀⠀⡏⣠⡾⢻⠇⠠⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠙⢿⠀⠀⢸⡇⠀⠀⠀⠀⡎⠑ ⢀⡀ ⢀⣸   ⣏⡱ ⡇ ⢀⡀ ⢀⣀ ⢀⣀⠀⠀
⠀⠀⠀⢸⡄⠀⠘⢷⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠣⠝ ⠣⠜ ⠣⠼   ⠧⠜ ⠣ ⠣⠭ ⠭⠕ ⠭⠕
⠀⠀⠀⣾⠄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠠⠜⢧⡀⠀⠀⠀⠀⠀
⠀⠀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀
⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⡆⠀⠀⠀⢀⣀⠀⠀⠀⠀⣿⣿⣿⡆⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⢀⠙⣧⠀⠀
⣼⡍⠀⣀⡀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠐⠄⠛⠿⠛⠁⠀⠀⠰⠏⠙⠷⠀⠀⠀⠈⠉⠉⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠶⣼⡇⠀
⣿⣷⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠁⠀⠀⠀⢰⣀⠘⣇⠀
⣿⠀⢀⡴⠲⠀⠀⠀⠀⠀⠒⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡟⠀
⠹⣞⠋⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⣰⠇⠀⠀
⠀⠻⣄⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀
⠀⠀⠙⠷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⣷⠶⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⢹⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣤⡴⠖⠶⣄⠀
⠀⠀⠀⠀⠀⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⢸⡆
⠀⠀⠀⣴⠞⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⣠⡿⠀
⠀⠀⠀⢿⡀⠀⢿⡀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⣠⡟⣀⣴⡾⠛⢈⠀
⠀⠀⠀⠐⠛⠶⣤⣽⣶⣄⠀⠀⠀⠸⣇⡀⠀⠀⠤⠴⣿⠀⠀⠀⠀⠀⢸⡶⠶⠀⠀⢀⣿⠐⠀⣀⣀⣠⣤⠾⠛⠛⠋⡁⠀⠀⠀⠀
⠀⠀⠀⠐⠀⠀⠤⠄⠈⠉⠛⠛⠶⠶⢿⣄⠀⠄⠀⣠⣧⣤⣤⣤⡤⠶⠾⣇⠀⠀⢐⣽⠟⠛⢛⠉⠍⠁⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠙⡷⠖⣟⣋⣀⣀⣀⣀⠀⠀⠀⠈⠛⠛⠋⠥⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')
            replay_answered = True
            game_finished = True
        elif replay == "yes":
            print("\n" * 100)
            replay_answered = True
        else:
            print("\nPlease answer with either\033[1m yes or\033[0m\033[1m no.\033[0m")