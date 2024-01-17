import sys
import math
from operator import itemgetter

from functools import partial
debug = partial(print, 'debug: ', file=sys.stderr, flush=True)

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = float(input().replace(',', '.'))
lat = float(input().replace(',', '.'))
n = int(input())

header = ['id_', 'name', 'address', 'phone', 'lon', 'lat']

defibs = [
    dict(zip(header, input().split(';')))
    for _ in range(n)
]

def dist(lat_a, lon_a, lat_b, lon_b):
    x = (lon_b - lon_a) * math.cos((lat_a + lat_b) / 2)
    y = (lat_b - lat_a)
    d = math.sqrt(x**2 + y**2) * 6371
    return d

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for d in defibs:
    d['lat'] = d['lat'].replace(',', '.')
    d['lon'] = d['lon'].replace(',', '.')
    d['dist'] = dist(lat, lon, float(d['lat']), float(d['lon']))

defibs.sort(key=itemgetter('dist'))

debug(defibs)

print(defibs[0]['name'])
