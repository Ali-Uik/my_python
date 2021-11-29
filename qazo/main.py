from counter import *

user_name = input('Ismingizni kiriting: ')
user_age = int(input('Yoshingizni kiriting: '))
n = user_age - 12
main_info = qazo(n)
file = open(f'{user_name.lower()}{user_age}.txt', mode='w', encoding='utf-8')
file.write(main_info)
file.close()
file2 = open('users.txt', mode='a', encoding='utf-8')
file2.write(user_name.lower() + str(user_age)+' ')
file2.close()
print(f'Assalomu aleykum {user_name.title()}.Sizning qazo namozlaringiz:\n{main_info}')

while True:
    command = input('Введите команду:')
    # print(command)
    if command == 'stop':
        break
    elif command == 'help':
        print('bobdod\npeshin\nasr\nshom\nxufton')
