import sys

sys.stdin = open('4837_input.txt', 'r')

def getSubset(num, numbers):
    n = len(numbers)
    cnt = 0
    # 가능한 부분집합의 수를 하나씩 뽑아서
    for i in range(2**n):
        t = []
        # 부분 집합의 길이를 뽑아서
        for j in range(n):

            subset = i & (2**j)
            if subset:
                t.append(numbers[j])

        if len(t) == num[0]:
            if sum(t) == num[1]:
                cnt +=1
    return cnt

T = int(input())
numbers = [i for i in range(1, 13)]

for tc in range(1, T + 1):
    num = list(map(int, input().split()))
    res = 0
    res = getSubset(num, numbers)
    print('#{} {}'.format(tc, res))

    # for i in range(len(numbers)):









