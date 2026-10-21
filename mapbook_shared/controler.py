import folium

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


def get_coordinates(city: str) -> list:
    import requests
    from bs4 import BeautifulSoup
    URL = f'https://pl.wikipedia.org/wiki/{city}'

    response = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})

    response_html = BeautifulSoup(response.content, 'html.parser')

    latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
    longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))

    return [latitude, longitude]


def get_map(user_list:list) -> None:
    m = folium.Map(location=(52.23, 21.00), zoom_start=6)

    for user in user_list:
        print(get_coordinates(user['location']))
        folium.Marker(
            location=get_coordinates(user['location']),
            tooltip="Click me!",
            popup=f'{user["name"]}!',
            icon=folium.Icon(icon="cloud"),
        ).add_to(m)

    m.save("index.html")