ans = 0

def solution(babbling):
    global ans
    lst = ["aya", "ye", "woo", "ma"]
    dct = {}
    mx = 0
    for word in babbling:
        mx = max(mx, len(word))

    def dfs(st, used):  # 문자열, 바로 이전에 사용 문자열
        global ans
        if len(st) > mx:
            return
        if st in babbling:
            dct[st] = 1
            ans += 1
        for word in lst:
            if word != used:
                dfs(st + word, word)

    dfs('', '')
    answer = sum(dct.values())
    return ans