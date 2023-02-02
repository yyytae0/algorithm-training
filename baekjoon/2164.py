from collections import deque

n = int(input())
card = deque()
for i in range(1, n+1):
    card.append(i)

if n > 1:
    while n:
        card.popleft()
        n = n - 1
        if n == 1:
            print(card.popleft())
            break

        dummy = card.popleft()
        card.append(dummy)

else:
    print(card.popleft())
