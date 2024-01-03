def lists():
    bicycles = ['trek', 'cannondale', 'redline', 'specialized']
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles)
    print(bicycles)
    print(bicycles[0])  # first element
    print(bicycles[-1])  # last element
    motorcycles.append("ducati")  # add element in last position
    print(motorcycles)
    motorcycles.insert(0, 'Toyota')  # add in specified position
    print(motorcycles)
    del motorcycles[0]  # remove a specified element
    print(motorcycles)
    motorcycles.pop()  # remove last element
    print(motorcycles)
    motorcycles.remove('yamaha')  # remove by value
    print(motorcycles)
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    cars.sort()  # arrange in alphabeth croissant
    print(cars)
    cars.sort(reverse=True)  # arrange in alphabeth desc
    print(cars)
    print(sorted(cars))  # arrange in alphabeth desc without application for list
    print(len(cars))  # length of list

    # working with a list
    for car in cars:  # browse a list
        print(car)

    for value in range(1, 10):  # generate 1 to 9
        print(value)
    numbers = list(range(1, 6))  # create a list of 1 to 5
    print(numbers)
    even_numbers = list(range(1, 11, 2))  # create a list with a part of 2
    print(even_numbers)

    squares = []
    for value in range(1, 11):
        squares.append(value ** 2)  # add expo 2 of value

    print(squares)

    squares = [value ** 2 for value in range(1, 11)]  # equal to line 37 to 39
    print(squares)

    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(players[0:3])  # subt list to index 0 to 2
    print(players[:4])  # end to index 3
    print(players[1:])  # start to index 1

    my_foods = ['pizza', 'falafel', 'carrot cake']
    friend_foods = my_foods[:]  # create a copy off my_foods
    print(friend_foods)

    dimensions = (200, 50)  # create a tuple
    print(dimensions[0])
    print(dimensions[1])
