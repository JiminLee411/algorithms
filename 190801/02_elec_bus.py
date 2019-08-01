import sys

sys.stdin = open('02_input.txt', 'r')

while 1:
    T = int(input())
    if 1 <= T <= 50:
        break

for test_case in range(1, T + 1):
    max_move, stop, charge = map(int, input().split())
    charge_place = list(map(int, input().split()))
    battery = max_move
    start = 0
    i = 0
    charge_num = 0

    while i <= charge - 1:

        # 예외처리 : 1. 마지막 주유소가 stop 위치에서 먼 경우
        #            2. 첫 주유소가 stop 위치에서 가까운 경우
        #            3. 주유 지점이 범위 내에 없으면 반복문을 종료한다.
        if charge_place[-1] + max_move < stop or charge_place[0] + max_move > stop or charge_place[i] > start + max_move:
            charge_num = 0
            break
        if i != charge - 1 and charge_place[i+1] - charge_place[i] > max_move:
            charge_num = 0
            break
        temp = 0
        # 주유소를 거쳐 갈 수 있게 계산한다.
        for place in charge_place:
            # 현재 주유소의 위치보다 먼 위치의 주유소일때
            if place >= charge_place[i + temp]:
                # 배터리가 주유지점과 현 위치의 차보다 크다면
                if battery > place - start:
                    # 이동시 닳은 배터리 값을 구한다
                    battery -= (place - start)
                    # 한 주유소를 거쳐 간다.
                    temp += 1
                    continue
                # 배터리가 같다면 나간다.
                elif battery == place - start:
                    break
                else:
                    break

        if start + max_move >= stop:
            break

        charge_num += 1
        i += temp
        start = charge_place[i]

    print('#{} {}'.format(test_case, charge_num))


# 2.
# while 1:
#     T = int(input())
#     if 1 <= T <= 50:
#         break
#
# for test_case in range(1, T + 1):
#     max_move, stop, charge = map(int, input().split())
#     charge_place = list(map(int, input().split()))
#     start = 0
#     i = 0
#     charge_num = 0
#
#     while i <= charge - 1:
#         if charge_place[-1] + max_move < stop or charge_place[0] + max_move > stop:
#             charge_num = 0
#             break
#
#         # i번째 인덱스의 주유 지점이 범위 내에 있으면
#         if start < charge_place[i] <= start + max_move:
#             # 다음 주유 지점 또한 범위 내에 있는 지 확인
#             if i < charge - 1 and start < charge_place[i + 1] <= start + max_move:
#                 # i번째 인덱스에 1을 더해준다 -> 최종적으로 다다음 정류장으로 보내기 위해
#                 if i < charge - 2 and start < charge_place[i + 2] <= start + max_move:
#                     i += 1
#                 i += 1
#             # 이동한 주유소로 시작지점을 변경한다.
#             start = charge_place[i]
#             # i번째 인덱스에 1을 더해준다.
#             i += 1
#             # 주유 횟수를 더한다.
#             charge_num += 1
#             if start + max_move >= stop:
#                 break
#         # 주유 지점이 범위 내에 없으면 반복문을 종료한다.
#         else:
#             charge_num = 0
#             break
#         # 최종 주유지점에서부터 목적지 까지의 거리가 max_move를 넘지 않는지 확인한다.
#
#     print('#{} {}'.format(test_case, charge_num))