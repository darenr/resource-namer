from word_lists import adjectives, animals

import random
from datetime import datetime

random.seed(datetime.now())


def name(format="<adjective>-<animal>"):
    adjective = random.choice(adjectives)
    animal = random.choice(
        [animal for animal in animals if animal[0] == adjective[0]] or animals
    )
    return f"{adjective}-{animal}"
