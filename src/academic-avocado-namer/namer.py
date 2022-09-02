from .word_lists import adjectives, animals

import random
from datetime import datetime

random.seed(datetime.now().timestamp())

def filter_fn(adjective: str, word: str) -> str:
    if adjective.startswith('f'):
        return word.startswith('f') or word.startswith('ph')
    else:
        return word.startswith(adjective[0])
    

def name() -> str:
    adjective = random.choice(adjectives)
    animal = random.choice(
        list(filter(lambda x: filter_fn(adjective, x), animals)) or animals
    )
    return f"{adjective}-{animal}"
