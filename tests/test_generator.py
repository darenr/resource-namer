# This program is free software: you can redistribute it and/or modify it under the
# terms of the Apache License (v2.0) as published by the Apache Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the Apache License for more details.
#
# You should have received a copy of the Apache License along with this program.
# If not, see <https://www.apache.org/licenses/LICENSE-2.0>.

"""Unit tests for random name generator."""


# type annotations
from typing import List, Dict

# standard libs
import re
import random

# internal libs
from academic_avocado_namer import generate_name


def test_generate_name() -> None:
    """Test name generator."""
    for i in range(1000):
        result = generate_name()
        assert "-" in result
        assert len(result.split("-")) == 2


def test_random_seed_consistency() -> None:
    """Test that setting a seed value reproduces the same name pair."""
    for i in range(1000):
        assert generate_name(seed=i) == generate_name(seed=i)
