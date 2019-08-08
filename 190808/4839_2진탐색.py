import sys

sys.stdin = open('4839_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    val = list(map(int, input().split()))
    front = 1
    back = val[0]
    cnt = [0, 0]

    while front <= back:
        mid = int((front + back) / 2)
        cnt[0] += 1
        if val[1] == mid:
            break
        elif val[1] > mid:
            front = mid
        else:
            back = mid

    front = 1
    back = val[0]

    while front <= back:
        mid = int((front + back) / 2)
        cnt[1] += 1
        if val[2] == mid:
            break
        elif val[2] > mid:
            front = mid
        else:
            back = mid

    if cnt[0] == cnt[1]:
        print('#{} 0'. format(tc))
    elif cnt[0] < cnt[1]:
        print('#{} A'. format(tc))
    else:
        print('#{} B'. format(tc))