import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from nwr.utils.grid_search import grid_search_aggregate
from nwr.utils.setup import backend_setup

if __name__ == "__main__":
    backend_setup()
    grid_search_aggregate()
