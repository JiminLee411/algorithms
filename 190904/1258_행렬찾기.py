import sys

sys.stdin = open('1258_input.txt', 'r')

for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = []    # 튜플로 행과 열 크기 저장

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0: continue
            r, c = i, 0
            while r < N and arr[r][j]:
                c = j
                while c < N and arr[r][c]:
                    arr[r][c] = 0
                    c += 1
                r += 1

            ans.append((r - i, c - j))
    ans.sort(key= lambda a: (a[0] * a[1], a[0]))

    print(ans)