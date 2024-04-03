"""Dzialanie Coffee Machine na podstawie modulu zew"""

import coffee_maker
import menu
import money_machine

if __name__ == '_main__':
    coffee_makerx = coffee_maker.CoffeeMaker()
    money_machinex = money_machine.MoneyMachine()
    coffee_menu = menu.Menu()
    is_on = True

    while is_on:
        coffee_menu_options = coffee_menu.get_items()
        choice = input(f"What would you like? ({coffee_menu_options}): ")

        if choice == 'off':
            is_on = False
        elif choice == 'report':
            coffee_makerx.report()
        else:
            drink = coffee_menu.find_drink(choice)
            if coffee_makerx.is_resource_sufficient(drink):
                if money_machinex.make_payment(drink.cost):
                    coffee_makerx.make_coffee()
            else:
                print("Something went wrong... :( ")
