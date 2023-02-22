sale = []
ans = [0, 0]


def buy(users, emoticons, sale):
    total = []
    for i in users:
        cost = 0
        for idx, j in enumerate(emoticons):
            if sale[idx] >= i[0]:
                cost += ((100 - sale[idx]) * emoticons[idx])//100
        total.append(cost)
    return total


def check(total, users):
    plus = 0
    money = 0
    for idx, i in enumerate(users):
        if i[1] > total[idx]:
            money += total[idx]
        else:
            plus += 1
    return plus, money


def make_sale(users, emoticons, cnt):
    global sale
    global ans
    if not cnt:
        total = buy(users, emoticons, sale)
        plus, money = check(total, users)
        if plus == ans[0]:
            if money >= ans[1]:
                ans = [plus, money]
        elif plus > ans[0]:
            ans = [plus, money]
        return

    for i in [40, 30, 20, 10]:
        sale.append(i)
        make_sale(users, emoticons, cnt - 1)
        sale.pop()


def solution(users, emoticons):
    make_sale(users, emoticons, len(emoticons))
    return ans


print(solution([[40, 10000], [25, 10000]], [7000, 9000]), [1, 5400])
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]), [4, 13860])