import sys

sys.stdin = open('swep_3752_input.txt', 'r')

# 1. DFS
# def backtrack(k, s):    # k: 트리의 높이, 문항번호  s: 지금까지 점수합
#     global cnt
#     if k == N:
#         if visit[s] == 0:
#             cnt += 1
#             visit[s] = 1
#     else:
#         backtrack(k + 1, s)             # K번 문제 틀림
#         backtrack(k + 1, s + arr[k])    # K번 문제 맞음
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     visit = [0] * 10001
#     cnt = 0
#     backtrack(0, 0)
#
#     print('#{} {}'. format(tc, cnt))


# -> 이것도 시간 많이 걸려 -> 중간 단계에서 커트
# def backtrack(k, s):    # k: 트리의 높이, 문항번호  s: 지금까지 점수합
#     global cnt
#     if visit[k][s]: return
#     visit[k][s] = 1
#     if k == N:
#         cnt += 1
#     else:
#         backtrack(k + 1, s)             # K번 문제 틀림
#         backtrack(k + 1, s + arr[k])    # K번 문제 맞음
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     visit = [[0] * ((N * 100) + 1) for _ in range(N + 1)]
#     cnt = 0
#     backtrack(0, 0)
#
#     print('#{} {}'. format(tc, cnt))


# 2.

# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     visit = [0] * 10001
#     visit[0] = 1
#
#     for s in arr:
#         for i in range(10000, -1, -1):
#             if visit[i]:
#                 visit[i + s] = 1
#     print(visit.count(1))

# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     visit = [0] * 10001
#     visit[0] = 1
#
#     for s in arr:
#         for i in range(10000, -1, -1):
#             if visit[i]:
#                 visit[i + s] = 1
#     print(visit.count(1))

# set으로 풀기
for t in range(1, int(input()) + 1):
    input()
    prev, now = {0}, {0}
    for i in map(int, input().split()):
        for j in prev:
            if j + i not in now:
                now.add(i + j)
        prev = set(now)
    print('#{} {}'.format(t, len(now)))



