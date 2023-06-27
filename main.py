from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_coffee_maker_on = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while is_coffee_maker_on:
    options = menu.get_items()
    users_choice = input(f"What would you like to drink? ({options}): ")

    if users_choice == 'off':
        is_coffee_maker_on = False
    elif users_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        if not isinstance(menu.find_drink(users_choice), type(None)):
            drink = menu.find_drink(users_choice)

            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
