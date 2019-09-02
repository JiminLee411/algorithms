import sys

sys.stdin = open('1979_input.txt', 'r')
for t in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    word = []
    for _ in range(N):
        word.append(list(map(int, input().split())))
    res = 0
    for y in range(N):
        r_cnt = l_cnt = 0
        for x in range(N):
            if word[y][x]:
                r_cnt += 1
                if x == N-1 and r_cnt == K:
                    res += 1
            else:
                if r_cnt == K:
                    res += 1
                r_cnt = 0

            if word[x][y]:
                l_cnt += 1
                if x == N-1 and l_cnt == K:
                    res += 1
            else:
                if l_cnt == K:
                    res += 1
                l_cnt = 0

    print('#{} {}'. format(t, res))
