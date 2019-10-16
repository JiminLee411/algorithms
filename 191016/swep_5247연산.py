import sys

sys.stdin = open('swep_5247_input.txt', 'r')

from collections import deque

def bfs(n, m, cnt):
    global res
    Q = deque()
    Q.append(n)
    visit[n] = 1
    while Q:
        a = Q.popleft()
        for i in range(4):
            if not C[i]:
                if a * 2 <= 1000000 and not visit[a * 2]:
                    Q.append(a * 2)
                    D[a * 2] = D[a] + 1
                    visit[a * 2] = 1
            else:
                if 0 < a + C[i] <= m and not visit[a + C[i]]:
                    Q.append(a + C[i])
                    D[a + C[i]] = D[a] + 1
                    visit[a + C[i]] = 1

            if D[M] and D[M] < res:
                res = D[M]

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    C = [1, -1, 0, -10]
    D = [0] * 1000001
    visit = [0] * 1000001
    res = 0xfffff
    bfs(N, M, 0)

    print('#{} {}'. format(tc, res))