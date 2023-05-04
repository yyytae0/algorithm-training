ans = [-1]
d = [0 for _ in range(11)]
mx = 0


def dfs(info, cnt, score_idx, total_ryan, total_apeach):
    global ans, d, mx
    if score_idx == 11:
        if cnt:
            d[-1] += cnt
        if total_ryan - total_apeach > mx:
            mx = total_ryan - total_apeach
            ans = d[:]
        elif total_ryan - total_apeach == mx and len(ans) > 1:
            for i in range(10, -1, -1):
                if d[i] > ans[i]:
                    ans = d[:]
                    return
                elif d[i] < ans[i]:
                    return
        return

    for i in [0, info[score_idx]+1]:
        if i <= cnt:
            d_ryan = total_ryan
            d_apeach = total_apeach
            if i:
                d_ryan += 10 - score_idx
            else:
                if info[score_idx]:
                    d_apeach += 10 - score_idx
            d[score_idx] = i
            dfs(info, cnt-i, score_idx+1, d_ryan, d_apeach)
            d[score_idx] = 0


def solution(n, info):
    global ans
    dfs(info, n, 0, 0, 0)
    return ans