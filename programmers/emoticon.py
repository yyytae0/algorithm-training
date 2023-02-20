def solution(users, emoticons):
    sale = [40 for _ in range(len(emoticons))]
    sale_d = []
    for i in users:
        sale_d.append(i[0])
    sale_d = set(sale_d)
    answer = []
    return answer


print(solution([[40, 10000], [25, 10000]], [7000, 9000]), [1, 5400])
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]), [4, 13860])