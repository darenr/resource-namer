from .word_lists import adjectives, animals

import random
from datetime import datetime

random.seed(datetime.now().timestamp())


def _filter_fn(adjective: str, word: str) -> bool:
    """used to filter list of adjectives phonetically

    Args:
        adjective (str): adjective word
        word (str): word to see if should be included in list of alliterationss

    Returns:
        bool: filter or not
    """
    if adjective.startswith("f"):
        return word.startswith("f") or word.startswith("ph")
    elif adjective.startswith("q"):
        return word.startswith("q") or word.startswith("k")
    else:
        return word.startswith(adjective[0])


def name(joiner: str = "-") -> str:
    """from two lists (`adjectives` and `animals`) return two joined
    words that form an alliteration pair using phonetics.

    e.g. frisky-ferret, flamboyant-pheasant, cultured-caribou

    Returns:
        str: adjective-animal combination joined on `joiner`
    """
    adjective = random.choice(adjectives)
    animal = random.choice(
        list(filter(lambda x: _filter_fn(adjective, x), animals)) or animals
    )
    return f"{adjective}{joiner}{animal}"
