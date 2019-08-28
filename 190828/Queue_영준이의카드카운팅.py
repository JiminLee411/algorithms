import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, int(input()) + 1):
    cards = input()
    print('#{}'. format(t), end=' ')
    card = [cards[i:i + 3] for i in range(0,len(cards), 3)]
    cnt = [13, 13, 13, 13]
    tmp = 0
    for i in range(len(card)):
        for j in range(len(card)):
            if i != j:
                if card[i] == card[j]:
                    tmp = 1
                    break
        if tmp == 1:
            break
        elif card[i][0] == 'S':
            cnt[0] -= 1
        elif card[i][0] == 'D':
            cnt[1] -= 1
        elif card[i][0] == 'H':
            cnt[2] -= 1
        else:
            cnt[3] -= 1

    if tmp:
        print('ERROR')
        continue

    for i in cnt:
        print(i, end=' ')
    print()