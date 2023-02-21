import collections


def solution(participant, completion):
    answer = ''
    dct = collections.Counter(completion)
    for i in participant:
        if i in dct and dct[i]:
            dct[i] -= 1
        else:
            return i