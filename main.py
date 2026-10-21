from mapbook_shared.model import users
from mapbook_shared.controler import show_users, add_user


while True:
    print('============MENU==============')
    print('0. Exit')
    print('1. Show users')
    print('2. Add user')
    choose: str=input('Wybierz opcję menu: ')
    if choose == '0': break
    if choose == '1': show_users(users)
    if choose == '2': add_user(users)

# show_users(users)
# add_user(users)
# show_users(users)