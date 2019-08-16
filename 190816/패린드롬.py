T = int(input())

for tc in range(1, T + 1):
    word = input()

    for i in range(len(word)):
        if word[i] != word[-i-1]:
            if word[i] == '?' or word[-i-1] == '?':
                if i == len(word) // 2:
                    res = 1
                    break
                continue
            else:
                res = 0
                break
        else:
            res = 1

    if res:
        print('#{} Exist'. format(tc))
    else:
        print('#{} Not exist'. format(tc))
