def solution(s):
    n = len(s)
    if n == 4 or n == 6:
        for i in s:
            if not i.isdigit():
                break
        else:
            return True
    return False