import random

def hop_game(hop_req, lives):
    hand_wins = 0
    player_wins = 0

    options = ["rock", "paper", "scissors"]

    last_choice = ""

    while lives > 0:
        hand_choice = random.choice(options)

        while hand_choice == last_choice:
            hand_choice = random.choice(options)

        last_choice = hand_choice
        # print(hand_choice)

        valid_choice_made = False

        while not valid_choice_made:
            player_choice = input("\n").lower()

            if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
                print("\nThe game master informs you that you must play [rock], [paper], or [scissors].")
            else:
                valid_choice_made = True

        if hand_choice == player_choice:
            print(f"\nThe hand mimics yours, also choosing {hand_choice}, nobody won this round.")
        elif hand_choice == "rock":
            print(f"\nThe Hand forms a fist, indicating it chose rock.\n")
            if player_choice == "paper":
                player_wins += 1
                print("Paper covers rock, you win this round.")
            elif player_choice == "scissors":
                hand_wins += 1
                print("Rock smashes scissors, The Hand wins this round.")
        elif hand_choice == "paper":
            print(f"\nThe Hand flattens itself, indicating it chose paper.\n")
            if player_choice == "scissors":
                player_wins += 1
                print("Scissors cuts paper, you win this round.")
            elif player_choice == "rock":
                hand_wins += 1
                print("Paper covers rock, The Hand wins this round.")
        elif hand_choice == "scissors":
            print(f"\nThe Hand forms a fist and then sticks out its pointer and middle fingers, indicating it chose scissors.\n")
            if player_choice == "rock":
                player_wins += 1
                print("Rock smashes scissors, you win this round.")
            elif player_choice == "paper":
                hand_wins += 1
                print("Scissors cuts paper, The Hand wins this round.")

        if hand_wins == hop_req:
            lives -= 1
            return False, lives
        elif player_wins == hop_req:
            return True, lives

    if lives <= 0:
        return  False, 0
    else:
        return False, lives

# print(hop_game(2, 1))