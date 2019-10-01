import sys

sys.stdin = open('swep_2819_input.txt', 'r')

def DFS(r, c, k):
    global cnt, tmp
    if k == 7:
        storage.add(''.join(tmp))
        return

    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= r + x < 4 and 0 <= c + y < 4:
            tmp.append(str(arr[r + x][c + y]))
            DFS(r + x, c + y, k + 1)
            tmp.pop()

for tc in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    storage = set()
    tmp = []
    cnt = 0
    for r in range(4):
        for c in range(4):
            DFS(r, c, 0)
    print('#{} {}'. format(tc, len(storage)))