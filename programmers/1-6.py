def solution(numbers, hand):
    answer = ''
    dct = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0],
           8: [2, 1], 9: [2, 2], '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    now_l = dct['*']
    now_r = dct['#']
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            now_l = dct[i]
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            now_r = dct[i]
        else:
            d = dct[i]
            dist_l = abs(d[0] - now_l[0]) + abs(d[1] - now_l[1])
            dist_r = abs(d[0] - now_r[0]) + abs(d[1] - now_r[1])
            if dist_l == dist_r:
                if hand == 'right':
                    answer += 'R'
                    now_r = d
                else:
                    answer += 'L'
                    now_l = d
            elif dist_l < dist_r:
                answer += 'L'
                now_l = d
            else:
                answer += 'R'
                now_r = d
    return answer
