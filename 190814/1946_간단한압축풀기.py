T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    res = ''

    for i in range(N):
        value = input()
        res += (value[0] * int(value[2:4]))

    print('#{}'.format(tc))
    for i in range(len(res)):
        if i % 10 == 0 and i > 0:
            print()

        print(res[i], end='')

    print()

