# В примере найти и вывести трехзначные числа с помощью регулярных выражений.
import re

sample = 'Exercises number 1, 12, 13, and 345 are important 456'

print(re.findall(r'\d\d\d', sample))
