from geopy import distance

locations = [
{'lat': 11.5148422781311, 'lng': -11.14076957717038766},
{'lat': 41.5148422781311, 'lng': -0.14076957717038766},
{'lat': 61.5148422781311, 'lng': -54.14076957717038766},
{'lat': 31.5148422781311, 'lng': -0.14076957717038766}
]

def calculeDistance(locations):
    distances = []
    for i in locations:
        depart = (i['lat'],i['lng'])
        ar = []
        for j in locations:
            dist = distance.distance(depart, (j['lat'],j['lng'])).km
            ar.append(round(dist, 2))
        distances.append(ar)
    return distances

