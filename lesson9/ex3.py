# def add_hello(obj):
#     return str(obj) + 'hello'
#
#
# list3 = list(map(add_hello, list1))


list1 = [i for i in range(1, 11)]
list2 = list(map(lambda number: str(number) + "hello", list1))
print(list2)
