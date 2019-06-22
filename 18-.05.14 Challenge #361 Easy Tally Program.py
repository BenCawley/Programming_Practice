inputs = [
    'EbAAdbBEaBaaBBdAccbeebaec',
    'dbbaCEDbdAacCEAadcB',
    'abcde'
]


def score_calc(input):
    lower = input.lower()
    players = {}
    for c in sorted(lower):
        if c not in players:
            players[c] = 0
    for c in input:
        for k in players:
            if c.lower() == k:
                players[k] += 1
            elif c.upper() == k:
                players[k] -= 1
    return players

for e in inputs:
    print (score_calc(e))