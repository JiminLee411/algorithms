import sys

sys.stdin = open('input.txt', 'r')

from collections import deque

def BFS(s, max_num):
    Q = deque()
    visit = [0] * (max_num + 1)
    D = [0] * (max_num + 1)
    Q.append(s)
    visit[s] = 1
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                Q.append(w)
                visit[w] = 1
                D[w] = D[v] + 1
    last = max(D)
    for i in range(len(D) - 1,0,-1):
        if D[i] == last:
            return i


for t in range(1, 11):
    N, start = map(int, input().split())
    nums = list(map(int, input().split()))
    max_num = max(nums)
    G = [[] for _ in range(max_num + 1)]
    for i in range(0,N,2):
        G[nums[i]].append(nums[i + 1])
    D = BFS(start, max_num)

    print(D)
