def check(square):
    s1 = square[:4]
    s2 = square[4:]
    # 사각형이 안겹치는 경우
    if (s1[2] < s2[0]) or (s2[2] < s1[0]) or (s1[3] < s2[1]) or (s2[3] < s1[1]):
        return 'd'

    # 점에서 겹치는 경우
    elif (s1[0] == s2[2] and s1[1] == s2[3]) or (s1[2] == s2[0] and s1[3] == s2[1]) or \
            (s1[0] == s2[2] and s1[3] == s2[1]) or (s1[2] == s2[0] and s1[1] == s2[3]):
        return 'c'

    # 선에서 겹치는 경우
    elif ((s1[0] == s2[2]) and ((s2[1] <= s1[1] <= s2[3]) or (s2[1] <= s1[3] <= s2[3]) or (s1[1] <= s2[1] and s1[3] >= s2[1]))) or \
            ((s1[2] == s2[0]) and ((s2[1] <= s1[1] <= s2[3]) or (s2[1] <= s1[3] <= s2[3]) or (s1[1] <= s2[1] and s1[3] >= s2[1]))) or \
            ((s1[1] == s2[3]) and ((s2[0] <= s1[0] <= s2[2]) or (s2[0] <= s1[2] <= s2[2]) or (s1[0] <= s2[0] and s1[2] >= s2[0]))) or \
            ((s1[3] == s2[1]) and ((s2[0] <= s1[0] <= s2[2]) or (s2[0] <= s1[2] <= s2[2]) or (s1[0] <= s2[0] and s1[2] >= s2[0]))):
        return 'b'

    # 사각형으로 겹치는 경우
    else:
        return 'a'


for i in range(4):
    lst = list(map(int, input().split()))
    ans = check(lst)
    print(ans)
