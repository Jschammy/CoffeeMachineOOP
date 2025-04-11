import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
my_coffee_machine = CoffeeMaker()
my_menu = Menu()
my_money_machine = MoneyMachine()


while machine_on:
    user_input = input(f"Please select from the following options ({my_menu.get_items()}): ").lower()
    if user_input == "report":
        my_coffee_machine.report()
        my_money_machine.report()
    elif user_input == "off":
        machine_on = False
    elif my_menu.find_drink(user_input):
        customer_order = my_menu.find_drink(user_input)
        if my_coffee_machine.is_resource_sufficient(customer_order) and my_money_machine.make_payment(customer_order.cost):
            my_coffee_machine.make_coffee(customer_order)