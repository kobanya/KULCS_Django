import random
import magyar

class NevekLibrary:

    def generate_random_name(self):
        kulcs = ["E04","E05", "E06", "E07", "E12","E13", "E14", "C06", "C04", "C03","A25","C05","C04","C11","C12","C13", "C14", "C15", "C16"]
        first_name = random.choice(magyar.keresztnev_v)
        last_name = random.choice(magyar.vezeteknev)
        kulcs_szam = random.choice(kulcs)
        return first_name, last_name, kulcs_szam
