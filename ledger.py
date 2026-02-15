import random
from stats import stats


def ledger_game(ledger_req, lives):
    statistics = stats
    points = 0

    while lives > 0:
        random_key1, random_value1 = random.choice(list(statistics.items()))

        while True:
            random_key2, random_value2 = random.choice(list(statistics.items()))
            if random_value2 != random_value1:
                break

        # print(f'''{random_key1}: {random_value1}''')
        # print(f'''{random_key2}: {random_value2}''')

        valid_first_answer = False

        while valid_first_answer == False:
            first_answer = input(f'''\nIs the {random_key1}\033[1m higher\033[0m or\033[1m lower\033[0m than the {random_key2}?\n\n''').lower()

            if first_answer == "higher":
                if random_value1 > random_value2:
                    points += 1
                    valid_first_answer = True
                else:
                    return False, lives, points
            elif first_answer == "lower":
                if random_value1 < random_value2:
                    points += 1
                    valid_first_answer = True
                else:
                    return False, lives, points
            else:
                print("\nPlease enter either\033[1m higher\033[0m or\033[1m lower\033[0m.")


        game_started = True

        while game_started == True:
            random_key1, random_value1 = random_key2, random_value2

            while True:
                random_key2, random_value2 = random.choice(list(statistics.items()))
                if random_value2 != random_value1:
                    break

            # print(f'''{random_key1}: {random_value1}''')
            # print(f'''{random_key2}: {random_value2}''')

            valid_answer = False

            while valid_answer == False:
                answer = input(f'''\nIs the {random_key1}\033[1m higher\033[0m or\033[1m lower\033[0m than {random_key2}?\n\n''').lower()

                if answer == "higher":
                    if random_value1 > random_value2:
                        points += 1
                        valid_answer = True
                    else:
                        if points >= ledger_req:
                            return True, lives, points
                        else:
                            return False, lives, points
                elif answer == "lower":
                    if random_value1 < random_value2:
                        points += 1
                        valid_answer = True
                    else:
                        if points >= ledger_req:
                            return True, lives, points
                        else:
                            return False, lives, points
                else:
                    print("\nPlease enter either\033[1m higher\033[0m or\033[1m lower\022[0m.")

    # print(points)

    if lives <= 0:
        return  False, 0, points
    else:
        return False, lives, points

# print(ledger_game(2, 2))