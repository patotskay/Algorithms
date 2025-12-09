n, m = map(int, input().split())
ls = []
for i in range(m):
    ls.append(list(map(int, input().split())))

ans = [0] * n
for i in range(m):
    for j in range(2):
        ans[ls[i][j] - 1] += 1

for i in range(n):
    print(ans[i])