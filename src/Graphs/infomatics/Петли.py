n = int(input())
ls = []
flag = 1
for i in range(n):
    ls.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if ls[i][j] == 1 and i == j:
            flag = 0
if flag == 0:
    print("YES")
else:
    print("NO")  