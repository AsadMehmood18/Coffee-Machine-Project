from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money = MoneyMachine()
def coffee_machine():
    while True:
        action = input(f"What would you like? ({my_menu.get_items()}): ").lower()
        if action == "off":
            print("COFFEE MACHINE TURNS OFF!")
            return
        elif action == "report":
            my_coffee_maker.report()
            my_money.report()
        else:
            available = my_menu.find_drink(action)
            if my_coffee_maker.is_resource_sufficient(available) and my_money.make_payment(available.cost):
                my_coffee_maker.make_coffee(available)


coffee_machine()

