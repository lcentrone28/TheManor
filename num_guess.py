import random

def code_game(code, attempts, lives):
    # print(code)
    current_attempts = attempts
    code_str = str(code)

    while current_attempts > 0:
        valid_guess = False

        while not valid_guess:
            guess = int(input("What code should I try next?\n\n"))
            guess_str = str(guess)

            if len(guess_str) == len(code_str):
                valid_guess = True
            else:
                print(f"\nThe code must be {len(code_str)} digits.")

        if guess == code:
            print('''
The box beeps three times and then unlocks, inside is a strange device with a keypad and a little screen that reads 
"READY FOR INPUT".
''')
            return True, lives
        elif guess > code:
            print("\nThe box beeps once.")
            current_attempts -= 1
        elif guess < code:
            print("\nThe box beeps twice.")
            current_attempts -= 1
    lives -= 1

    if lives <= 0:
        print('''
As you fiddle with the lock a loud buzzer goes off, scaring you half to death. “Game master here, miss me? Unfortunately 
you exceeded the amount of allowed attempts, I mean we can't just let you fool with it all day, there are other 
participants waiting for you to finish after all. Such a shame, you made it so far just to have a silly little number 
guessing game be your doom. Kinda embarrassing if you ask me but we thank you for playing nonetheless. Hang out, enjoy 
a cup of coffee while you wait, Niles will retrieve you shortly”
''')
        return False, 0
    else:
        return False, lives

# print(code_game(4579, 3, 2))