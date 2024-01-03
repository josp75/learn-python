import json

if __name__ == '__main__':

    """ Read """
    with open('pi_digits.txt') as file_object:
        contents = file_object.read()
        print(contents.lstrip())

    with open('pi_digits.txt') as file_object:
        for line in file_object:  # read line by line
            print(line.lstrip())

    """ Write """
    filename = 'programming.txt'
    with open(filename, 'a') as file_object:
        file_object.write("I love programming.\n")
        file_object.write("I love creating new games.\n")

    """ Exception """
    a = 3
    b = 0
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Divide by zero")
    else:
        print("Unknown")

    try:
        age = 00
        print("age" + age)
    except:
        print("Unknown")

    """ Json store"""
    numbers = [2, 3, 5, 7, 11, 13]
    filename = 'numbers.json'
    with open(filename, 'w') as f_obj:
        json.dump(numbers, f_obj)

    alien_0 = {'color': 'green', 'points': 5}
    alien_1 = {'color': 'yellow', 'points': 10}
    alien_2 = {'color': 'red', 'points': 15}
    aliens = [alien_0, alien_1, alien_2]
    filename = 'aliens.json'
    with open(filename, 'w') as f_obj:
        json.dump(aliens, f_obj)
