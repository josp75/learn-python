# This is a sample Python script.
from classes.dog import Dog
from classes.electrical_car import ElectricalCar
from condition.conditions import conditions
from dictionary.dictionary import dictionary
from function.functions import functions
from list.lists import lists
from user_input.user_input import user_input
from variable.numbers import numbers
from variable.strings import strings


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    strings("test")
    numbers()
    lists()
    conditions()
    dictionary()
    user_input()
    functions()
    dog = Dog("Dick", 34)
    print(dog.sit())
    my_tesla = ElectricalCar('Tesla', 'Models', 2016, name="KEL")
    print(my_tesla.get_descriptive_name())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
