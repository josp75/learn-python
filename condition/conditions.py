def conditions():
    cars = ['audi', 'bmw', 'subaru', 'toyota']
    for car in cars:
        if car == 'subaru':
            print(car.upper())
        else:
            print(car.lower())
    age_0 = 21
    age_1 = 18
    if age_0 >= 21 and age_1 >= 18:
        print(age_0 >= 21 and age_1 >= 18)
    requested_toppings = ['mushrooms', 'onions', 'pineapple']
    if 'mushrooms' in requested_toppings:
        print(requested_toppings)
    banned_users = ['andrew', 'carolina', 'david']
    user = 'marie'
    if user not in banned_users:
        print(user)
    age = 12
    if age < 4:
        print("Your admission cost is $0.")
    elif age < 18:
        print("Your admission cost is $5.")
    else:
        print("Your admission cost is $10.")

    requested_toppings = []
    if requested_toppings:
        print("List is not empty")
    else:
        print("List is empty")