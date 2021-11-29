file = open('romeo.txt', mode='r', encoding='utf-8')
data = []
for line in file:
    print(line)
    for i in line:
        data.append(i)
# data_str = ''
# for i in data:
#     if i != '\n':
#         data_str = data_str + str(i)
# print(data_str)