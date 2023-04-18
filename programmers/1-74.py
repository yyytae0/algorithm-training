def solution(players, callings):
    dct = dict()
    for idx, i in enumerate(players):
        dct[i] = idx
    for i in callings:
        now = dct[i]
        dct[i] = now-1
        dct[players[now-1]] = now
        players[now-1], players[now] = players[now], players[now-1]
    return players
