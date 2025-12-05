
n = int(input())
ls = []
for i in range(n):
    ls.append(list(map(int, input().split())))

ans = 0
for i in range(n):
    for j in range(n):
        if ls[i][j] == 1:
            ans += 1
print(ans//2)