def strings(test):
    name = "ada lovelace"
    first_name = "ada"
    last_name = "lovelace"
    full_name = first_name + " " + last_name
    favorite_language = ' python '
    print(test)
    print(name.title())
    print(name.upper())
    print(name.lower())
    print(full_name)
    print("Hello, " + full_name.title() + "!")
    print("Python")
    print("\tPython")
    print("Languages:\nPython\nC\nJavaScript")
    print("Languages:\n\tPython\n\tC\n\tJavaScript")
    print(favorite_language.lstrip())
    print(favorite_language.rstrip())
    print(favorite_language.strip())
