def functions():
    name = "Jospin"
    greet_user(name)
    describe_pet("harry", "pet")
    describe_pet_1("harry", animal_type="pet")
    print(build_person("Jospin", "Mambou"))


def greet_user(username):
    print(f"Hello, {username}")


def describe_pet(animal_type: str, pet_name: str):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


def describe_pet_1(pet_name, animal_type='dog'):  # with keyword argument and default value
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


def build_person(first_name: str, last_name: str) -> dict:
    """Return a dictionary of information about a person."""

    person = {'first': first_name, 'last': last_name}
    return person


def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keywords ", kwargs.values())
    squares = [_ ** 2 for _ in range(10)]
    print(squares)


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


if __name__ == '__main__':
    magic(1, 11, 1, key="word", key2="test")
    print(build_person('1', "2"))
    scope_test()
