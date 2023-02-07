for case in range(10):
    n = int(input())
    lst = list(map(int, input().split()))
    m = int(input())
    task = list(map(int, input().split()))
    idx = 0
    while True:
        if task[idx] == 'I':
            dummy = task[idx:idx+3+task[idx+2]]
            idx = idx+3+task[idx+2]
            pass
        elif task[idx] == 'D':
            dummy = task[idx:idx+3]
            idx = idx + 3
            pass
        elif task[idx] == 'A':
            dummy = task[idx:idx+2+task[idx+1]]
            idx = idx + 2 + task[idx+1]
            pass
