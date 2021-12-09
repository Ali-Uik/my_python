from counter import *
from pprint import pprint

user_name = input('Ismingizni kiriting: ')
user_age = int(input('Yoshingizni kiriting: '))
count = []
with open('D:/Учебники/Proweb/work_space/qazo/users/users.txt', mode='r', encoding='utf-') as users_file:
    users_data = users_file.read().split(' ')

    for item in users_data:
        if item == user_name + str(user_age):
            count.append(item)

if len(count) == 1:
    file4 = open(f'D:/Учебники/Proweb/work_space/qazo/users/{user_name.lower()}{str(user_age)}.txt', mode='r',
                 encoding='utf-8')
    data = file4.read()
    print(data)
    file4.close()
elif len(count) == 0:
    n = user_age - 12
    main_info = qazo(n)  # def qazo() - ни ишлатамиз
    file = open(f'D:/Учебники/Proweb/work_space/qazo/users/{user_name.lower()}{str(user_age)}.txt', mode='w',
                encoding='utf-8')
    file.write(main_info)
    file.close()
    file2 = open('D:/Учебники/Proweb/work_space/qazo/users/users.txt', mode='a', encoding='utf-8')
    file2.write(' ' + user_name.lower() + str(user_age) + ' ')
    print(main_info, type(main_info))
    file2.close()

# n = user_age - 12
# main_info = qazo(n)
# file = open(f'{user_name.lower()}{user_age}.txt', mode='w', encoding='utf-8')
# file.write(main_info)
# file.close()
# file2 = open('users.txt', mode='a', encoding='utf-8')
# file2.write(user_name.lower() + str(user_age) + ' ')
# file2.close()
# print(f'Assalomu aleykum {user_name.title()}.Sizning qazo namozlaringiz:\n{main_info}')
#
while True:
    command = input('Введите команду:')
    # print(command)
    if command == 'stop':
        break
    elif command == 'help':
        print('bobdod\npeshin\nasr\nshom\nxufton')
    # elif command == 'ars':
    #     asr(user_name, user_age)
