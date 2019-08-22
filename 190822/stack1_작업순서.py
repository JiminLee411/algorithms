import sys

sys.stdin = open('input.txt', 'r')

def BFS(cnt):
    que = []
    res = []
    for i in range(1, len(cnt)):
        if cnt[i] == 0:
            que.append(i)
    while que:
        len_que = len(que)
        v = que.pop(0)
        for j in R[v]:
            if j not in res:
                que.append(v)
                break
        if v not in res and len(que) == len_que - 1:
            res.append(v)
            print(v, end=' ')
            for w in G[v]:
                if not visit[w]:
                    que.append(w)
    return res

for t in range(1, 11):
    print('#{}'. format(t), end=' ')
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    R = [[] for _ in range(V + 1)] # BFS에서 비교할 리스트
    visit = [False] * (V + 1)
    cnt = [0 for _ in range(V + 1)]
    Es = list(map(int, input().split()))
    for i in range(E):
        G[Es[i * 2]].append(Es[i * 2 + 1])
        R[Es[i * 2 + 1]].append(Es[i * 2])
        cnt[Es[i * 2 + 1]] += 1

    BFS(cnt)
    print()
