n = int(input())
ls = []
for i in range(n):
    ls.append(list(map(int, input().split())))

ans = []
for i in range(n):
    ans.append([0] * n)
for i in range(n):
    for j in range(len(ls[i])):
        if ls[i][j] != 0:
            ans[i][ls[i][j] - 1] = 1

for i in range(n):
    print(*ans[i])