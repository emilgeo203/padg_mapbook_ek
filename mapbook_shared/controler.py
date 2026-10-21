def show_users(user_list: list) -> None:
    for user in user_list:
        print(f'twój znajomy {user['name']} z miejscowości {user['location']} opublikował {user['posts']} postów')


def add_user(user_list: list) -> None:
    user_list.append({'name': input('Podaj imię: '), 'location': input('Podaj miejscowość: '),
                      'posts': int(input('Podaj liczbę postów: '))})



def remove_user(user_list: list) -> None:
    name_of_user_to_remove: str=input('Podaj imię użytkownika do usunięcia: ')
    for user in user_list:
        if user['name'] == name_of_user_to_remove:
            user_list.remove({'name': 'Emil', 'location': 'Łomża', 'posts': 50})

def update_user(user_list: list) -> None:
    name_of_user_to_update: str=input('Podaj imię użytkownika do edycji: ')
    for user in user_list:
        if user['name'] == name_of_user_to_update:
            user['name'] = input('Podaj nowe imię użytkownika: ')
            user['location'] = input('Podaj nową lokalizację użytkownika: ')
            user['posts'] = int(input('Podaj liczbę postów: '))
