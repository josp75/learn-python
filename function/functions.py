def functions():
    name = "Jospin"
    greet_user(name)
    describe_pet("harry", "pet")
    describe_pet_1("harry", animal_type="pet")
    print(build_person("Jospin", "Mambou", "45"))


def greet_user(username):
    print(f"Hello, {username}")


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


def describe_pet_1(pet_name, animal_type='dog'):  # with keyword argument and default value
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
