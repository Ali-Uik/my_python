import json
from pprint import pprint

#
# def qazo(n):
#     day = n * 365
#     bomdod = 2 * day
#     peshin = 4 * day
#     asr = 4 * day
#     shom = 3 * day
#     xufton = 4 * day
#     vitr = 3 * day
#     main_info = {
#         'day': day,
#         'bobdod': bomdod,
#         'peshin': peshin,
#         'ars': asr,
#         'shom': shom,
#         'xufton': xufton,
#         'vitr': vitr
#     }
#     main_json = json.dumps(main_info)
#
#     return main_json


user_name = input('Ismingizni kiriting: ')
user_age = int(input('Yoshingizni kiriting: '))

# def asr(user_name, user_age):
#     file = open(f'../qazo/users/{user_name.lower()}{str(user_age)}.txt', mode='r',
#                 encoding='utf-8')
#     data = file.read()
#
#     return data
#     # print(asr_num)
#
#
# print(asr(user_name, user_age))


file = open(f'../qazo/users/{user_name.lower()}{str(user_age)}.txt', mode='r', encoding='utf-8')
data = file.read()
data2 = data.split(',')
print(data)
