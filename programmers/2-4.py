def solution(numbers):
    n = len(numbers)
    ans = [-1]
    dummy = numbers[-1]
    dct = dict()
    dct[numbers[-1]] = -1
    for i in range(2, n + 1):
        if dummy > numbers[-i]:
            ans.append(dummy)
            dct[numbers[-i]] = dummy
            dummy = numbers[-i]
        else:
            while dummy != -1:
                dummy = dct[dummy]
                if dummy > numbers[-i]:
                    ans.append(dummy)
                    dct[numbers[-i]] = dummy
                    dummy = numbers[-i]
                    break
            if dummy == -1:
                ans.append(dummy)
                dct[numbers[-i]] = dummy
            dummy = numbers[-i]
    return ans[::-1]
