from collections import deque

N, K = map(int, input().split())
visit = [0] * 10001

Q = deque()
visit[N] = 1
Q.append((N,0))
while Q:
    x, d = Q.popleft()
    if x == K:
        print(d); break
    if x<<1 <= 100000 and not visit[x << 1]:
        visit[x << 1] = 1
        Q.append(x<<1)

    if x + 1 <= 100000 and not visit[x + 1]:
        visit[x + 1] = 1
        Q.append((x + 1, d + 1))

    if x - 1 >=0 and not visit[x - 1]:
        visit[x - 1] = 1
        Q.append((x - 1, d + 1))