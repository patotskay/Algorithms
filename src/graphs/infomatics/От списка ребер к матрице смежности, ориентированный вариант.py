n, m = map(int, input().split())
ls = []
for i in range(m):
    ls.append(list(map(int, input().split())))

ls1 = []
for i in range(n):
    ls1.append([0] * n)
for i in range(n):
    for j in range(n):
        if [i + 1, j + 1] in ls:
            ls1[i][j] = 1
for i in range(n):
    print(*ls1[i])