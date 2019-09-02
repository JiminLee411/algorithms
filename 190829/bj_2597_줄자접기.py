import sys
import math
sys.stdin = open('input.txt', 'r')

N = int(input())
colors = [list(map(int, input().split())) for _ in range(3)]
center = []
for color in colors:
    if color[1] > color[0]:
        center.append((color[1] - color[0]) / 2 + color[0])
    else:
        center.append((color[1] - color[0]) / 2 + color[0])

for i in range(2):
    for j in range(i + 1, 3):
        if j < len(center) and center[i] == center[j]:
            center.pop(j)
tmp = []
res = 10
for i in range(len(center)):
    if not tmp:
        res -= center[i]
        tmp.append(res)
    else:
        if tmp[-1] < center[i]:
            res -= (center[i] - center[i-1])
            tmp.append(res)
print('{:.1f}'.format(tmp[-1]))
