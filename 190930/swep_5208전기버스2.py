import sys

sys.stdin = open('swep_5208_input.txt', 'r')

def goMax(cur, b):
    global point, cnt
    # 최대로 간다음 하나씩 줄이기
    for i in range(b,0,-1):
        # 배터리 최대가 목적지면 나가라
        if cur + i >= N - 1:
            return
        # 저장되 최대 이동보다 이전 최대 이동이 더 크면 그걸로 바꿔라
        elif arr[cur + i] > arr[cur] - i:
            if arr[point] + (point - (cur + i)) < arr[cur + i]:
                point = cur + i
    cnt += 1
    goMax(point, arr[point])

for tc in range(1, int(input()) + 1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    cnt, point= 0, 0
    res = 0

    goMax(0, arr[0])

    print('#{} {}'. format(tc, cnt))