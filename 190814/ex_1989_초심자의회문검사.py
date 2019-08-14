T = int(input())
for tc in range(1, T + 1):
    word = input()
    res = 1

    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            res = 0
            break

    print('#{} {}'.format(tc, res))
