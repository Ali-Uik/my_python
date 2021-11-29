file = open('mbox-short.txt', mode='r', encoding='utf-8')
count = {}
for line in file:
    if line.startswith('From '):
        data = line.split(' ')
        # time = data[6].split(':')
        # hours = time[0]
        hours = line.split(' ')[6].split(':')[0]
        count[hours] = count.get(hours, 0) + 1

file.close()
for key, value in sorted(count.items()):
    print(f'В {key} часов прошло {value} писем')
