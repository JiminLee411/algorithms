V, E = map(int, input().split())    # 정점수, 간선수
Edge = [tuple(map(int, input().split())) for _ in range(E)] # (u, v, w)

# disjoin-set
p = [x for x in range(V)]
def findSet(x):
    if x != p[x]:
        p[x] = findSet(p[x]) # path-compression
    return p[x]

Edge.sort(key=lambda x: x[2]) # 가중치 오른차순 정렬
MST = []
idx = 0
while len(MST) < V - 1: # V - 1개의 간선을 선택 ( 정점개수가 V이므로)
    u, v, w = Edge[idx]
    a = findSet(u)
    b = findSet(v)

    if a != b:
        MST.append((u, v, w))
        p[b] = a

    idx += 1

print(MST)