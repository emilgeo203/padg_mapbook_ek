users = [
    {'name': 'Emil', 'location': 'Łomża', 'posts': 50},
]


def show_users(user_list: list) -> None:
    for user in user_list:
        print(f'twój znajomy {user['name']} z miejscowości {user['location']} opublikował {user['posts']} postów')

def add_user(user_list: list) -> None:
    user_list.append({'name':input('Podaj imię: '), 'location':input('Podaj miejscowość: '), 'posts':int(input('Podaj liczbę postów: '))})

show_users(users)
add_user(users)
show_users(users)