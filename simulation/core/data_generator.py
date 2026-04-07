import random
import time
from simulation.core.scenarios import generate_people

def get_frame():
    objects = generate_people(5)

    frame = {
        "image": None,
        "objects": objects,
        "timestamp": time.time()
    }

    return frame
