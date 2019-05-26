import collections
from operator import itemgetter


def ranking(people):
    position["position"]="123" #any initial value
    x = collections.OrderedDist(sorted(people.items(), key = lambda t: t[1]))
    sorted(x.values())
    sorted(d.items(), key=itemgetter(1))
    return
    ranking([
        {
            "name": "John",
            "points": 100,
        },
        {
            "name": "Bob",
            "points": 130,
        },
        {
            "name": "Mary",
            "points": 120,
        },
        {
            "name": "Kate",
            "points": 120,
        },
    ])