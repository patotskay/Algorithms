n = int(input())
ls1 = []
ls2 = [0]*n
for i in range(n):
    ls1.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if ls1[i][j] == 1:
            ls2[i] += 1

for i in range(n):
    print(ls2[i])