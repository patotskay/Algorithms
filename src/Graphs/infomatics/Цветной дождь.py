n = int(input())
ls = []
ls1 = []
for i in range(n):
    ls.append(list(map(int, input().split())))
s = input()
ls1 = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(n):
        if ls[i][j] == 1 and ls1[i] != ls1[j]:
            ans += 1
print(ans//2)