# 회문 1
for tc in range(1, 11):
    board = []
    N = int(input())
    board = [input() for _ in range(8)]

    ans = 0

    for idx in range(8):
        for s in range(8 - N + 1):
            e = s + N - 1
            for i in range(N//2):
                if board[idx][s + i] != board[idx][e - i]: break
            else:
                ans += 1
            for i in range(N // 2):
                if board[s + i][idx] != board[e - i][idx]: break
            else:
                ans += 1
    print(ans)


# 회문 2
for tc in range(1, 11):
    board = []
    N = int(input())
    board = [input() for _ in range(100)]

    ans = 1

    for idx in range(100):
        for s in range(100):
            for e in range(99, s, -1):
                L = e - s + 1
                if L <= ans: break
                for i in range(N//2):
                    if board[idx][s + i] != board[idx][e - i]: break
                else:
                    ans = L
                if L <= ans: break
                for i in range(N // 2):
                    if board[s + i][idx] != board[e - i][idx]: break
                else:
                    ans = L
    print(ans)

# 다른 방법
for tc in range(1, 11):
    board = []
    N = int(input())
    board = [input() for _ in range(100)]

    ans = 1

    for idx in range(100):
        for x in range(100): # x: 기준 위치
            # 길이가 짝수
            l, r, cnt = x, x + 1, 0
            while l >= 0 and r < 100:
                if board[idx][l] != board[idx][r]: break
                l, r, cnt = l - 1, r + 1, cnt + 2
            ans = max(ans, cnt)

            l, r, cnt = x, x + 1, 0
            while l >= 0 and r < 100:
                if board[l][idx] != board[r][idx]: break
                l, r, cnt = l - 1, r + 1, cnt + 2
            ans = max(ans, cnt)

            l, r, cnt = x, x + 1, 1
            while l >= 0 and r < 100:
                if board[idx][l] != board[idx][r]: break
                l, r, cnt = l - 1, r + 1, cnt + 2
            ans = max(ans, cnt)

            l, r, cnt = x, x + 1, 1
            while l >= 0 and r < 100:
                if board[l][idx] != board[r][idx]: break
                l, r, cnt = l - 1, r + 1, cnt + 2
            ans = max(ans, cnt)

    print(ans)