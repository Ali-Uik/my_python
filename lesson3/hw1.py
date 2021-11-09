a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
five_minus = []
five_plus = []
for item in a:
    if item <= 5:
        five_minus.append(item)
    else:
        five_plus.append(item)
print(five_plus)
print(five_minus)
