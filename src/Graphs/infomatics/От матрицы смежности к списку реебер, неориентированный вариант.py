n = int(input())
ls = []
for i in range(n):
    ls.append(list(map(int, input().split())))

ans = []
for i in range(n):
    for j in range(n):
        if ls[i][j] == 1 and [j + 1, i + 1] not in ans:
            ans.append([i + 1,j + 1])
for i in range(len(ans)):
    print(*ans[i])