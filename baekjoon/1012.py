ip = int(input())

for i in range(ip):
    lst = list(map(int, input().split()))
    arr = [[0 for j in range(lst[0])] for i in range(lst[1])]
    for j in range(lst[2]):
        dummy = list(map(int, input().split()))
        arr[dummy[1]][dummy[0]] = 1

    print(arr)

