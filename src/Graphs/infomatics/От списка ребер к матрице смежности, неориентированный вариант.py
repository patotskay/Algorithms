n, m = map(int, input().split())
ls = []
for i in range(n):
    ls.append([0]*n)
for i in range(m):
    a, b = map(int, input().split())
    ls[a - 1][b - 1] = 1
    ls[b - 1][a - 1] = 1
for i in range(n):
    print(*ls[i])