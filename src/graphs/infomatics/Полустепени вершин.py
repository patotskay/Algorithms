n = int (input())
ls = []
for i in range(n):
    ls.append(list(map(int, input().split())))

ls1 = [0] * n
ls2 = [0] * n
for i in range(n):
    for j in range(n):
        if ls[i][j] == 1:
            ls1[i] += 1
            ls2[j] += 1

for i in range(n):
    print(ls2[i])
    print(ls1[i])