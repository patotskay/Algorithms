n, m = map(int, input().split())
edges = []
for i in range(m):
    edges.append(list(map(int, input().split())))

ls1 = [0] * (n + 1)
ls2 = [0] * (n + 1)

for  edge in edges:
    ls2[edge[0]] += 1
    ls1[edge[1]] += 1

for i in range(1, n + 1):
    print(ls1[i])
    print(ls2[i])  