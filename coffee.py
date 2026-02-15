import areas
chose_mocha = False

recipes = {
    "espresso": {"beans": 20, "water": 50},
    "coffee": {"beans": 25, "water": 350},
    "latte": {"beans": 20, "water": 50, "milk": 250},
    "cappuccino": {"beans": 30, "water": 100, "milk": 250, "sugar": 5},
    "mochaccino": {"beans": 30, "water": 100, "milk": 250, "sugar": 5, "cocoa": 5},
}

resources = {
    "beans": 30,
    "water": 350,
    "milk": 250,
    "sugar": 5,
    "cocoa": 5
}

def check_resources(c_choice):
    recipe = recipes.get(c_choice.lower())

    if recipe is None:
        return "invalid entry"

    for item, amount in recipe.items():
        if resources.get(item, 0) < amount:
            return "insufficient resources"

    return None

def deduct_resources(c_choice):
    recipe = recipes[c_choice]

    for ingredient, amount in recipe.items():
        resources[ingredient] -= amount

def run_coffee(coinage, first_number):
    global chose_mocha
    coffee_choice = ""
    # first_number = "numbers"
    choice_made = False

    while choice_made == False:
        print('''You walk up to the coffee machine and inspect it. It looks like an older vending machine, the kind that has pictures of 
cans of soda on the buttons. You've never seen one that dispenses freshly made coffee though. Each button has the name 
of the coffee, how many coins are required, and a picture. Above the buttons is a coin slot and the button to press if 
your coin gets stuck. You press it but nothing happens.
''')

        if areas.coinage > 1:
            print(f"You put your hand in your pocket and pull out the coffee coins you've collected. You have {areas.coinage} coins.\n")
        elif areas.coinage == 1:
            print("You put your hand in your pocket and pull out the single coffee coin you've collected.\n")
        else:
            print("You don't have any coffee coins so you'll just have to wait for your caffeine fix.\n")
            choice_made = True

        if areas.coinage == 1:
            print('''All you can afford is a shot of espresso. You press the button and a plain white disposable cup drops down and 
the smallest amount of espresso is dispensed. You pick up the cup, swirl the espresso around in the cup to help it cool 
a little and then down it in one sip, it's the best espresso you've ever had.
''')
            choice_made = True
        elif areas.coinage == 2:
            coffee_choice = input("You can get a black\033[1m coffee\033[0m or a shot of\033[1m espresso\033[0m.\n\n").lower()
        elif areas.coinage == 7:
            coffee_choice = input("You can get a black\033[1m coffee\033[0m, a shot of\033[1m espresso\033[0m, a\033[1m latte\033[0m, a\033[1m cappuccino\033[0m, or a\033[1m mochaccino\033[0m.\n\n").lower()
        elif areas.coinage >= 5:
            coffee_choice = input("You can get a black\033[1m coffee\033[0m, a shot of\033[1m espresso\033[0m, a\033[1m latte\033[0m, or a\033[1m cappuccino\033[0m.\n\n").lower()
        elif areas.coinage >= 3:
            coffee_choice = input("You can get a black\033[1m coffee\033[0m, a shot of\033[1m espresso\033[0m, or a\033[1m latte\033[0m.\n\n").lower()

        if coffee_choice != "":
            resource_check = check_resources(coffee_choice)
            if resource_check == "invalid entry":
                print("\nYou press the button but nothing happens, perhaps you didn't press it hard enough? Try again.\n")
                continue
            elif resource_check == "insufficient resources":
                print("\nThe coffee machine informs you there are insufficient resources and asks you to make another selection.\n")
                continue
            else:
                deduct_resources(coffee_choice)
                if coffee_choice == "espresso":
                    print('''\nYou press the button, a plain white disposable cup drops down and the smallest amount of espresso is dispensed. 
You pick up the cup, swirl the espresso around in the cup to help it cool a little and then down it in one sip, it's 
the best espresso you've ever had.
''')
                    choice_made = True
                elif coffee_choice == "coffee":
                    print('''\nYou press the button, a plain white disposable cup drops down and fills with black coffee. You pick up the cup, swirl 
it around gently as to not spill any, and sip on it while admiring the different plants, for plain coffee, no milk or 
sugar, it's pretty darn good.
''')
                    choice_made = True
                elif coffee_choice == "latte":
                    print('''\nYou press the button, a plain white disposable cup drops down and fills with coffee and milk. You pick up the cup, 
swirl it around gently as to not spill any, and sip on it while admiring the different plants, for a plain latte, no 
sugar or other flavoring, it's pretty darn good.
''')
                    choice_made = True
                elif coffee_choice == "cappuccino":
                    print('''\nYou press the button, a plain white disposable cup drops down and fills with coffee and milk. You pick up the cup, 
swirl it around gently as to not spill any, and sip on it while admiring the different plants, it's the best 
cappuccino you've ever had.
''')
                    choice_made = True
                elif coffee_choice == "mochaccino":
                    print(f'''\nYou press the button, a disposable cup covered in\033[1m {first_number}\033[0ms drops down and fills with coffee and milk. You pick up the 
oddly designed cup, swirl it around gently as to not spill any, and sip on it while admiring the different plants, 
it's the best mochaccino you've ever had.
''')
                    chose_mocha = True
                    choice_made = True

    # print(chose_mocha)
    # print(resources)


# print(run_coffee(7, 1))