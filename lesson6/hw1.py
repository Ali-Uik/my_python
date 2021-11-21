# Есть словарь координат городов.
cities = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
# Составьте словарь словарей расстояний между ними по формуле:
# ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
distances = {}
moscow = cities['Moscow']  # (550, 370),
london = cities['London']
paris = cities['Paris']
m_l = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** 0.5
m_p = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** 0.5
l_p = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** 0.5
distances['m_l'] = m_l
distances['m_p'] = m_p
distances['l_p'] = l_p
print(distances)
