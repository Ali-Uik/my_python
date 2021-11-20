# Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
from pprint import pprint
numbers2 = {x: x ** 3 for x in range(10)}
pprint(numbers2)
