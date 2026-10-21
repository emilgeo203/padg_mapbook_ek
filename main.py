from mapbook_shared.model import users
from mapbook_shared.controler import show_users, add_user, remove_user, update_user, get_map

while True:
    print('============MENU==============')
    print('0. Exit')
    print('1. Show users')
    print('2. Add user')
    print('3. Remove user')
    print('4. Update user')
    print('5. Show map')
    choose: str=input('Wybierz opcję menu: ')
    if choose == '0': break
    if choose == '1': show_users(users)
    if choose == '2': add_user(users)
    if choose == '3': remove_user(users)
    if choose == '4': update_user(users)
    if choose == '5': get_map(users)
# show_users(users)
# add_user(users)
# show_users(users)