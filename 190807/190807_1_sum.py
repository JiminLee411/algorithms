# 1번
import sys

sys.stdin = open('190807_1_input.txt', 'r')

for test_case in range(1, 11):
    tc = int(input())
    # 1번
    value = [list(map(int, input().split())) for _ in range(100)]
    N = range(len(value[0]))
    # print(value)
    # 2번
    # arr = []
    # for _ in range(100):
    #     arr.append(list(map(int, input().split())))

    sum_list = []
    # 행 구하기
    # 2차 행렬이므로 value에서 한 방씩 뽑으면 하니의 list가 나온다 (한 행이 나오는 것)
    for x in value:
        # 그거를 다 더해
        sum_list.append(sum(x))
    # 열 구하기
    # 100X100이니까 100가지 인덱스를 뽑는다 -> 열을 구해야하는 거니까 행을 뽑아서 한 방만 구해야하니까 바깥 for문이 열 이라고 생각해야함
    for y in N:
        # 더한 값을 넣을 방을 만든다
        sum_value = 0
        # 행을 반복해서 열어서 거기에 해당하는 같은 열을 다 더해준다
        for x in N:
            sum_value += value[x][y]
        # 다 더한 값을 list에 넣는다
        sum_list.append(sum_value)

    sum_1 = 0
    sum_2 = 0

    for x in N:
        # [0][0], [1][1] ... [100][100]의 합을 다 구해야 함
        sum_1 += value[x][x]
        # [0][100], [1],[99] .... [100],[0]의 합을 다 구해야함
        sum_2 += value[x][-x-1]

    sum_list.append(max(sum_1, sum_2))

    print('#{} {}'. format(tc, max(sum_list)))



# 2번

import sys

sys.stdin = open('190807_1_input.txt', 'r')


for test_case in range(1, 11):
    tc = int(input())

    value = [list(map(int, input().split())) for _ in range(100)]
    N = range(len(value[0]))

    sum_max = 0
    sum_1 = 0
    sum_2 = 0

    for x in N:
        sum_max = max(sum_max, sum(value[x][0:100]))
        sum_1 += value[x][x]
        sum_2 += value[x][-x]
    sum_max = max(sum_max, sum_1, sum_2)

    for y in N:
        # 더한 값을 넣을 방을 만든다
        sum_value = 0
        # 행을 반복해서 열어서 거기에 해당하는 같은 열을 다 더해준다
        for x in N:
            sum_value += value[x][y]
        # 다 더한 값을 list에 넣는다
        sum_max = max(sum_max, sum_value)

    print('#{} {}'. format(tc, sum_max))

# 3번
for test_case in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    Max = 0
    dsum1 = dsum2 = 0

    for i in range(100):
        rsum = csum = 0
        dsum1 += arr[i][i]
        dsum2 += arr[i][99-i]
        for j in range(100):
            rsum += arr[i][j]
            csum += arr[j][i]
        Max = max(Max, rsum, csum, dsum1, dsum2)
