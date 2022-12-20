from .common import get_match_plays, WINMAP


LOSSMAP = {
    WINMAP[hand]: hand for hand in WINMAP
}

def result_cipher(left, ciphered):
    if ciphered == "X":
        return WINMAP[left]

    if ciphered == "Y":
        return left

    return LOSSMAP[left]

def execute():
    return sum([score for score in get_match_plays(result_cipher)])
