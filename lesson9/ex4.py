# codewars.com

def duplicate_count(text):
    list1 = list(text.lower())
    list2 = list(text.lower())
    x = []
    for item in list2:
        if list1.count(item) > 1:
            x.append(item)
    return len(list(set(x)))


duplicate_count("Izzat")
