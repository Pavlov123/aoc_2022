from .client import AOCClient
import os


AOC_CLIENT = AOCClient()
DATACACHE_DIR = "./._datacache"


def read_data(day=1):
    os.makedirs(DATACACHE_DIR, exist_ok=True)
    name = "day_%s.txt" % day
    path = os.path.join(DATACACHE_DIR, name)
    if not os.path.exists(path):
        with open(path, "w") as data_cache_file:
            response = AOC_CLIENT.get(
                "https://adventofcode.com/2022/day/%s/input" % day
            )
            data_cache_file.write(response.text)
    with open(path, "r") as data_cache_file:
        for row in data_cache_file:
            yield row
