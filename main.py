from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
#Menu,MenuItem,CaffeeMaker and MoneyMachine are class

money_machine = MoneyMachine()     #Object
coffee_maker = CoffeeMaker()       #Object
menu = Menu()
is_on = True

#money_machine.report()             #report how money we have

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)