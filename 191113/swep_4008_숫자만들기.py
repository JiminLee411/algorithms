import sys

sys.stdin = open('swep_4008.txt', 'r')

def calculate(now, res, op):
    global Max, Min
    if now == N - 1:
        Max = max(res, Max)
        Min = min(res, Min)
        return
    for i in range(4):
        if op[i] == 0:
            continue
        op[i] -= 1
        if i == 0:
            calculate(now + 1, res + numbers[now + 1], op)
        elif i == 1:
            calculate(now + 1, res - numbers[now + 1], op)
        elif i == 2:
            calculate(now + 1, res * numbers[now + 1], op)
        else:
            calculate(now + 1, int(res / numbers[now + 1]), op)
        op[i] += 1

# T = int(input())
for tc in range(1, int(input()) + 1):
    N = int(input())
    operators = list(map(int, input().split())) # [+, -, *, /]
    numbers = list(map(int, input().split()))
    Max = -0xfffff
    Min = 0xfffff
    calculate(0, numbers[0], operators)

    print('#{} {}'. format(tc, Max - Min))