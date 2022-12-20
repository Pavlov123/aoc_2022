from utils import read_data

SCORES = {
    "A": 1,
    "B": 2,
    "C": 3,
}

CIPHER = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}

WINMAP = {
    "A": "C",
    "B": "A",
    "C": "B",
}

def match_resolution(left, right):
    if left == right:
        return 3

    if WINMAP[right] == left:
        return 6

    return 0


def map_cipher(left, ciphered):
    return CIPHER[ciphered]


def get_match_plays(cipher):
    plays = []
    for row in read_data(2):
        left, right = row.strip().split()
        plays.append(
            match_resolution(left, cipher(left, right)) + SCORES[cipher(left, right)]
        )

    return plays
