# This program is free software: you can redistribute it and/or modify it under the
# terms of the Apache License (v2.0) as published by the Apache Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the Apache License for more details.
#
# You should have received a copy of the Apache License along with this program.
# If not, see <https://www.apache.org/licenses/LICENSE-2.0>.


# standard libs
import sys
import random
import logging

# internal libs

from .__meta__ import __version__, __description__, __authors__, __contact__

from .word_lists import adjectives, animals, plants


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


def generate_name(joiner: str = "-", prefer_plants: bool = False, seed: int = None) -> str:
    """from two lists (`adjectives` and `animals`) return two joined
    words that form an alliteration pair using phonetics.

    e.g. frisky-ferret, flamboyant-pheasant, cultured-caribou

    Returns:
        str: adjective-animal combination joined on `joiner`
    """

    if seed is not None:
        random.seed(seed)

    adjective = random.choice(adjectives)
    second_set = plants if prefer_plants else animals 
    thing = random.choice(
        list(filter(lambda x: _filter_fn(adjective, x), second_set)) or second_set
    )
    return f"{adjective}{joiner}{thing}"


def main() -> int:
    """Entry-point for `generate_name` console application."""

    """Generate a random name and print it."""

    print(generate_name(prefer_plants=True))
