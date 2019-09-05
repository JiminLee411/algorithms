import sys

sys.stdin = open('BJ_15686_input.txt', 'r')

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
visit = []
home = []
chicken = []
res = 0xffffff

def chickenStore(idx, last, store):
    global res
    global M
    if store > M: return
    if store == M:
        res = min(res, chickenLoad())
        return
    if idx < last:
        visit.append(idx)
        chickenStore(idx + 1, last, store + 1)
        visit.pop()
        chickenStore(idx + 1, last, store)

def chickenLoad():
    total = 0
    for i in range(len(dist)):
        minDist = N*2
        for j in visit:
            minDist = min(minDist, dist[i][j])
        total += minDist
    return total

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            home.append([r, c])
        if city[r][c] == 2:
            chicken.append([r, c])

dist = [[] for _ in range(len(home))]
for i in range(len(home)):
    for rr, cc in chicken:
        dist[i].append(abs(home[i][0] - rr) + abs(home[i][1] - cc))
chickenStore(0, len(dist[0]), 0)

print(res)


