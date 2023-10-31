import random
import magyar

class NevekLibrary:

    def __init__(self, arg=None):
        pass

    def generate_random_name(self):
        kulcs = ["E05", "E06", "E07", "E13", "E14", "C06", "C04", "C03"]
        first_name = random.choice(magyar.keresztnev_v)
        last_name = random.choice(magyar.vezeteknev)
        kulcs_szam = random.choice(kulcs)
        return first_name, last_name, kulcs_szam
