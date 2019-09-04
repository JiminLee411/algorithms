import sys

sys.stdin = open('6109_input.txt', 'r')

def leftNup(n):
    global tmp
    for c in range(n - 1):
        while tmp[c] == 0 and (sum(tmp[c:]) != 0):
            tmp.append(tmp.pop(c))
    for c in range(n - 1):
        if tmp[c] == tmp[c+1]:
            tmp[c] += tmp.pop(c+1)
            tmp.append(0)

def rightNdown(n):
    global tmp
    for c in range(n - 1, 0, -1):
        while tmp[c] == 0 and (sum(tmp[0:c]) != 0):
            tmp.pop(c)
            tmp = [0] + tmp
    for c in range(n - 1, 0, -1):
        if tmp[c] == tmp[c-1]:
            tmp[c - 1] += tmp.pop(c)
            tmp = [0] + tmp


for t in range(1, int(input()) + 1):
    N, S = map(str, input().split())
    N = int(N)
    board = []
    tmp2 = []
    res = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        if S == 'left':
            leftNup(N)
            res.append(' '.join(list(map(str, tmp))))

        elif S == 'right':
            rightNdown(N)
            res.append(' '.join(list(map(str, tmp))))
        else:
            board.append(tmp)
    if S == 'up':
        for col in range(N):
            tmp = [row[col] for row in board]
            leftNup(N)
            tmp2.append(tmp)
        for col in range(N):
            tmp = [row[col] for row in tmp2]
            res.append(' '.join(list(map(str, tmp))))

    elif S == 'down':
        for col in range(N):
            tmp = [row[col] for row in board]
            rightNdown(N)
            tmp2.append(tmp)
        for col in range(N):
            tmp = [row[col] for row in tmp2]
            res.append(' '.join(list(map(str, tmp))))

    print('#{}'. format(t))
    for i in range(N):
        print(res[i])
