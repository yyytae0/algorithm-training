a, b = map(int, input().split())

a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))
c_set = a_set - b_set
d_set = c_set.union(b_set-a_set)

print(len(d_set))
