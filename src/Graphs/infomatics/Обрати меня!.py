n = int(input())
ls = []
for i in range(n):
    ls.append(list(map(int, input().split())))
ans = []
for i in range(n):
    ans.append([])
for i in range(n):
    for j in range(len(ls[i])):
        ans[ls[i][j] - 1].append(i + 1)
print(n)
for i in range(n):
    print(*ans[i])