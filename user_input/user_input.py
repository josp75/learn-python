def user_input():
    name = input("Please enter your name: ")
    print("Hello, " + name.title() + "!")
    age = input("How old are you? ")
    age = int(age)
    if age > 21:
        print("Your are old")
