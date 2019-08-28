import sys
​
sys.stdin = open('input.txt', 'r')
​
def orderSet(r, c, n, used, min_num):
    # 만약 r == n 이면, 저장한 인덱스의 순서 return
    if r == n:
        if sumNum() < min_num:
            min_num = sumNum()
            return min_num
    # for문을 통해 k번 index를 뽑아서
    for i in range(n):
        # 만약 사용했던 i 이면 continue
        if used & 1 << i:
            continue
        # 원소의 인덱스의 순서로 저장
        order[c] = i
        # 함수 호출(시작 + 1, 끝, 선택한 요소들의 집합)
        orderSet(r + 1, c + 1, n, used | 1 << i, min_num)
def sumNum():
    res = 0
    for i in enumerate(order):
        res += nums[i[0]][i[1]]
    return res
for t in range(1, int(input()) + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    order = [0] * N
    used = [0] * N
​
    for column in range(N):
        min_num = 50
        res = orderSet(0,0,N,0,100)
    print(res)
    # print(order)
    

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