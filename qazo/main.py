from counter import *

user_name = input('Ismingizni kiriting: ')
user_age = int(input('Yoshingizni kiriting: '))
n = user_age - 12
qazo_namozlar = qazo(n)
print(f'Assalomu aleykum {user_name.title()}.Sizning qazo namozlaringiz:\n{qazo_namozlar}')

while True:
    command = input('Введите команду:')
    # print(command)
    if command == 'stop':
        break
    elif command == 'help':
        print('bobdod\npeshin\nasr\nshom\nxufton\n')
