def count_two(n):
    cnt = 0
    while True:
        n = n//2
        cnt += n
        if n == 0:
            break

    return cnt


def count_five(n):
    cnt = 0
    while True:
        n = n//5
        cnt += n
        if n == 0:
            break

    return cnt


a, b = map(int, input().split())

print(min(count_two(a) - count_two(b) - count_two(a-b),
          count_five(a) - count_five(b) - count_five(a-b)))
