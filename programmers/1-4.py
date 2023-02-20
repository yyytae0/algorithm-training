def solution(s):
    lst = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for idx, i in enumerate(lst):
        s = s.replace(i, str(idx))
    return int(s)
