from .common import get_match_plays, map_cipher


def execute():
    return sum([score for score in get_match_plays(map_cipher)])
