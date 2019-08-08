import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    value = list(map(int, input().split()))
    num = []
    i = 0
    line = ''
    tmp = ''
    # 받은 리스트를 두개씩 나눠 다시 리스트에 넣어서 2차행렬로 만든다
    # 2개씩 나눠서 비교해야하므로 이게 더 편함
    for _ in range(N):
        num.append(value[i:i + 2])
        i += 2
    # 리스트의 [0]번째에 있는 리스트를 [0][0]과 [0][1]을 각각 빼서 str에 더한다.
    # 그런데 이미 [0][0]을 pop했으므로 [0][1]의 값이 [0][0]의 위치에 있다.
    line += str(num[0].pop(0)) + ' ' + str(num[0].pop(0))
    # [0]번째 방은 빈방인 []으로 남아있다 -> 빈방도 pop을 통해 꺼내준다.
    num.pop(0)
    # 위와 마찬가지로 num의 숫자를 pop을 통해 str로 넣는다
    # 숫자 하나를 넣으면 다시 처음부터 돌려야 하므로 이중 반복문으로 돌린다.
    # 이를 위해 num의 길이가 0보다 클때 동안 while문을 돌린다. num의 길이가 바뀌므로 for문은 X
    while len(num) > 0:
        j = 0
        # j번째 방에 가기 위한 반복문을 돌린다.
        while len(num) > 0:
            # 만약 str의 마지막값이 num의 첫값과 같으면
            if int(line[-2:]) == num[j][0]:
                # 뒤에 더해준다
                line += ' ' + str(num[j].pop(0)) + ' ' + str(num[j].pop(0))
                num.pop(j)
                break
            # 만약 str의 첫값과 num의 마지막값이 같으면
            elif int(line[0:2]) == num[j][1]:
                # 앞에 더해준다.
                tmp += (str(num[j].pop(0)) + ' ' + str(num[j].pop(0)) + ' ' + line)
                line = tmp
                num.pop(j)
                tmp = ''
                break
            j += 1

    print('#{} {}'. format(tc, line))
