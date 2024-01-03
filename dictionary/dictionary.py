def dictionary():
    alien_0 = {'color': 'green', 'points': 5}
    print(alien_0['color'])
    alien_0['x_position'] = 0
    alien_0['y_position'] = 25
    print(alien_0)
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }
    print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

    # browse favorite_languages
    for key, value in favorite_languages.items():
        print("\n Key : " + key)
        print("\n value : " + value)

    alien_0 = {'color': 'green', 'points': 5}
    alien_1 = {'color': 'yellow', 'points': 10}
    alien_2 = {'color': 'red', 'points': 15}
    aliens = [alien_0, alien_1, alien_2]
    print(aliens)
    for alien in aliens:
        print("Color is " + alien['color'])
        print("points is " + str(alien['points']))
