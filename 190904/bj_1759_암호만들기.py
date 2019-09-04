# import sys
#
# sys.stdin = open('bj_1759_input.txt', 'r')
#
# # 부분집합으로 만들기
# pwd = []
# alpha = ('a', 'e', 'i', 'o', 'u')
# def backtrack(k): # mo : 모음 개수, ja : 자음 개수
#     if len(pwd) == L:
#         print(pwd)
#         return
#     if k == C:
#         return
#     pwd.append(arr[k])
#     a = b= 0
#     # if arr[k] in alpha: a = 1
#     # else: b = 1
#     backtrack(k + 1) # k번째 요소를 포함하는 경우
#     pwd.pop()
#     backtrack(k + 1) # k번째 요소를 포함하지 않는 경우
#
# L, C = map(int, input().split())
# arr = list(input().split())
# arr.sort()
#
# backtrack(0)

import sys

sys.stdin = open('bj_1759_input.txt', 'r')

# 부분집합으로 만들기
pwd = []
alpha = ('a', 'e', 'i', 'o', 'u')
choose = []
def comb(k ,start): # k: 지금까지 선택한 개수, start: 반복문의 시작값
    if k == L:
        print(choose)
        return
    for i in range(start, C):
        # i번째 정보를 저장
        choose.append(arr[i])
        a = b= 0
        if arr[k] in alpha: a = 1
        else: b = 1
        comb(k + 1, i + 1)
        choose.pop()

L, C = map(int, input().split())
arr = list(input().split())
arr.sort()

comb(0, 0)