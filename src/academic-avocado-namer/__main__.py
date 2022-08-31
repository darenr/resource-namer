from typing import List, Optional
from namer import name
import sys

__version__ = "0.0.1"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        count = int(sys.argv[1])
    else:
        count = 1

    for x in range(count):
        print(name())
