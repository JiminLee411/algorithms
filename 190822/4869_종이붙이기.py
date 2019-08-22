import sys

sys.stdin = open('4869_input.txt', 'r')

def factorial(i):
    if i <= 1:
        return i
    else:
        return i * factorial(i - 1)

for t in range(1, int(input()) + 1):
    N = int(input()) // 10
    cnt = 0

    for square in range(N // 2, -1, -1):
        for horizon in range(N // 2 - square, -1, -1):
            comp = [square, horizon, N - (square + horizon) * 2]
            div_num = 1
            for i in comp:
                if i == 0:
                    continue
                div_num *= factorial(i)

            cnt += int(factorial(sum(comp)) / div_num)

    print('#{} {}'. format(t, cnt))


