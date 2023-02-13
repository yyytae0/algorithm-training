n = int(input())
dct = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 0:0}
mx = 0
while n:
    a = n % 10
    n = n//10
    dct[a] += 1
dummy = dct[6] + dct[9]
dct[6], dct[9] = (dummy+1)//2, (dummy+1)//2
for i in range(10):
    if dct[i] > mx:
        mx = dct[i]
print(mx)
