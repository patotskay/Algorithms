n = int(input())
ls = []
anssum = 3001
anslist = []
for i in range(n):
    ls.append(list(map(int, input().split())))
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if ls[i][j] + ls[j][k] + ls[k][i] < anssum:
                anssum = ls[i][j] + ls[j][k] + ls[k][i]
                anslist = []
                anslist.append(i + 1)
                anslist.append(j + 1)
                anslist.append(k + 1)
print(*anslist)