n = int(input())
ls = []
for i in range(n):
    ls.append(list(map(int, input().split())))

ans = []
for i in range(n):
    ans.append([])
for i in range(n):
    for j in range(n):
        if ls[i][j] == 1:
            ans[i].append(j + 1)

for i in range(n):
    if ans[i] == []:
        print(0)
    else:
        print(*ans[i])