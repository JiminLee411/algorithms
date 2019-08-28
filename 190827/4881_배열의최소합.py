import sys

sys.stdin = open('input.txt', 'r')

def perm(k, n, used, cursum):
    global MIN
    res = []
    if cursum >= MIN:
        return
    if k == n:
        MIN = cursum
        return
    for i in range(n):
        if used & (1 << i): continue
        perm(k + 1, n ,used | (1 << i), cursum + arr[k][i])
    return MIN

for t in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    MIN = 0
    for i in range(N):
        arr.append(list(map(int, input().split())))
        MIN += sum(arr[-1])
    used = 0b000
    res = perm(0,N,used,0)
    print(res)

# 선생님코드
# def perm(k, n, used, cursum):
#     global MIN
#     if cursum >= MIN: return
#
#     if k == n:
#         MIN = cursum
#         return
#     for i in range(n):
#         if used & (1 << i): continue
#
#         perm(k + 1, n ,used | (1 << i), cursum + arr[k][i])
# for t in range(1, int(input()) + 1):
#     N = int(input())
#     arr = []
#     for i in range(N):
#         arr.append(list(map(int, input().split())))
#