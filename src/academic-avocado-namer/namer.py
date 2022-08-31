from word_lists import adjectives, animals

import random

random.seed(42)


def name(format="<adjective>-<animal>"):
    return f"{random.choice(adjectives)}-{random.choice(animals)}"
