import sys

sys.stdin = open('4843_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 리스트를 받는다.
    origin = list(map(int, input().split()))
    # 원본 리스트를 복사해 변형할 리스트를 만든다.
    value = list(origin)
    n = len(value)
    res = ''
    # 버블 정렬로 정렬
    for j in range(n-1, 0, -1):
        for i in range(j):
            if value[i] > value[i + 1]:
                value[i], value[i + 1] = value[i + 1], value[i]
    # 원본 리스트와 정렬한 리스트의 차가 10이 될 동안 진행한다.
    while len(origin) < len(value) + 10:
        if len(value) < 1:
            break;
        # 문자열에 정렬된 리스트의 마지막 값과 첫번째 값을 순차적으로 넣는다.
        res += str(value.pop(-1)) + ' '
        if len(value) < 1:
            break;
        res += str(value.pop(0)) + ' '

    print('# {} {}'. format(tc, res))
