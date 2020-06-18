# You have a dictionary of cities. Create dictionary of distances

from pprint import pprint

cities = {
    'Los Angeles': (550, 370),
    'Chicago': (510, 510),
    'Dallas': (480, 480)
}

distances = {}

los_angeles = cities['Los Angeles']
chicago = cities['Chicago']
dallas = cities['Dallas']

los_angeles_chicago = ((chicago[0] - los_angeles[0]) ** 2 + (chicago[1] - los_angeles[1]) ** 2) ** 0.5
chicago_dallas = ((chicago[0] - dallas[0]) ** 2 + (chicago[1] - dallas[1]) ** 2) ** 0.5
los_angeles_dallas = ((los_angeles[0] - dallas[0]) ** 2 + (los_angeles[1] - dallas[1]) ** 2) ** 0.5


distances['Los Angeles'] = {}
distances['Los Angeles']['Dallas'] = los_angeles_dallas
distances['Los Angeles']['Chicago'] = los_angeles_chicago

distances['Chicago'] = {}
distances['Chicago']['Dallas'] = chicago_dallas
distances['Chicago']['Los Angeles'] = los_angeles_chicago

distances['Dallas'] = {}
distances['Dallas']['Los Angeles'] = los_angeles_dallas
distances['Dallas']['Chicago'] = chicago_dallas

pprint(distances)
