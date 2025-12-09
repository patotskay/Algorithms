
n, m = map(int, input().split())
ls = []
for i in range(m):
    ls.append(list(map(int, input().split())))

d = {}
d1 = {}
ans = []
for i in range(m):
    for j in range(2):
        if ls[i][j] not in d:
            d[ls[i][j]] = 1
        else:
            d[ls[i][j]] += 1
d1 = dict(sorted(d.items()))
ans = list(d1.values())     
if m == 0:
    print(0)
else:
    print(*ans)