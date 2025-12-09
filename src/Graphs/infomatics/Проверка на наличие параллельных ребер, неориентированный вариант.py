n, m = map(int, input().split())
ls1 = []
ls2 = []
flag = 0
for i in range(m):
    ls1.append(list(map(int, input().split())))

for i in range(m):
    if ls1[i] in ls2:
        flag = 1
    ls2.append(ls1[i])

if flag:
    print("YES")
else:
    print("NO")