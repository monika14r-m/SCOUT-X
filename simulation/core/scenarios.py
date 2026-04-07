import random

def generate_people(n=3):
    objs = []
    for _ in range(n):
        objs.append({
            "type": "person",
            "x": random.randint(0, 640),
            "y": random.randint(0, 480)
        })
    return objs
