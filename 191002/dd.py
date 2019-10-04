# import collections
#
# num = [4, 5, 6, 7, 8, 9]
# N = len(num)
# cnt = 10
# visit = [[0] * 1000000 for _ in range(11)]
# MAX = 0
# def backtrack(k):
#     global MAX
#     # MAX = max(MAX, int(''.join(map(str, num))))
#     val = int(''.join(map(str, num)))
#     if visit[k][val]: return
#     visit[k][val] = 1
#     if k == cnt:
#         if val > MAX:
#             MAX = val
#     else:
#         for i in range(N - 1):
#             for j in range(i + 1, N):
#                 num[i], num[j] = num[j], num[i]
#                 backtrack(k + 1)
#                 num[i], num[j] = num[j], num[i]
#
# backtrack(0)
# print(MAX)
#
#
# # ----- 큐 이용
# import collections
#
# d = [1, 10, 100, 1000, 10000, 100000]
#
# def swap(val, i, j):
#     a = (val//d[i]) % 10
#     b = (val//d[j]) % 10
#     return val - a * d[i] + a * d[j] - b * d[j] + b * d[i]
#
# num = 32888
# N = len(num)
# cnt = 10
# visit = [[0] * 1000000 for _ in range(11)]
# MAX = 0
# Q = collections.deque()
# Q.append((num, 0))
#
# while Q:
#     val, k = Q.popleft()
#     if k == cnt:
#         MAX = max(MAX, val)
#     else:
#         for i in range(N - 1):
#             for j in range(N):
#                 t = swap(val, i, j)
#                 if visit[k][t]: continue
#                 Q.append((t, k + 1))
#
# print(MAX)

# ---set
d = [1, 10, 100, 1000, 10000, 100000]

def swap(val, i, j):
    a = (val//d[i]) % 10
    b = (val//d[j]) % 10
    return val - a * d[i] + a * d[j] - b * d[j] + b * d[i]

num = 32888
N = 6
cnt = 10
visit = [[0] * 1000000 for _ in range(11)]
MAX = 0
Q = [{num}] + [set() for _ in range(cnt)]
for k in  range(cnt):
    for val in Q[k]:
        for i in range(N - 1):
            for j in range(N):
                t = swap(val, i, j)
                Q[k + 1].add(t)

print(max(Q))