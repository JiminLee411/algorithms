
T = int(input())

for tc in range(1, T + 1):
    pattern = input()
    p_length = len(pattern)
    target = input()
    t_length = len(target)
    res = 0

    for i in range(t_length):
        if (i > p_length - 1) & (target[i] == pattern[-1]) & (target[i - p_length + 1 : i + 1] == pattern):
            res = 1

    print('#{} {}'.format(tc, res))