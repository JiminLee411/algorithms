# import sys
#
# sys.stdin = open('5110_input.txt', 'r')
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class List:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0
#
#     def printlist(self): #필요없고
#         if self.head is None:
#             return
#         cur = self.head
#         while cur is not None:
#             print(cur.data, end=' ')
#             cur = cur.next
#         print()
#
#     def deletelast(self):
#         if self.head is None:
#             return
#         prev, cur = None, self.head
#         while cur.next is not None:
#             prev = cur
#             cur = cur.next
#         if prev is None:
#             self.head = self.tail = None
#         else:
#             prev.next = None
#             self.tail = prev
#         del cur
#         self.size -=1
#
#     def printlast(self):
#         cur = self.tail
#         print(cur.data, end=' ')
#
#     def insertlast(self, node):
#         if self.head is None:
#             self.head = self.tail = node
#             self.size += 1
#             return
#         else:
#             self.tail.next = node
#             self.tail = node
#         self.size += 1
#
#     def listextend(self, arr2):
#         prev, cur = None, self.head
#         value = arr2.head
#         if cur.data > value.data:
#             arr2.tail.next = self.head
#             self.size += arr2.size
#             self.head = arr2.head
#         else:
#             while cur.next is not None:
#                 prev = cur
#                 cur = cur.next
#                 if cur.data > value.data:
#                     self.size += arr2.size
#                     prev.next = arr2.head
#                     arr2.tail.next = cur
#                     return
#             self.size += arr2.size
#             self.tail.next = arr2.head
#             self.tail = arr2.tail
#
# T = int(input())
#
# for t in range(1, T + 1):
#     N, M = map(int, input().split())
#     mylist = List()
#     for value in map(int, input().split()):
#         mylist.insertlast(Node(value))
#     for _ in range(M - 1):
#         mylist2 = List()
#         for value in map(int, input().split()):
#             mylist2.insertlast(Node(value))
#         mylist.listextend(mylist2)
#     print('#{}'.format(t), end=' ')
#     for _ in range(10):
#         mylist.printlast()
#         mylist.deletelast()
#     print()

# 다시 해봐!!!!
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def printlist(self):
        if self.head is None:
            return
        cur = self.head
        while cur is not None:
            print(' {}'.format(cur.data), end='')
            cur = cur.next
        print()

    def insertFirst(self, node):
        if self.head is None:
            self.head = self.tail = node
            return
        else:
            node.next = self.head
            self.head = node

    def insertlast(self, node):
        if self.head is None:
            self.head = self.tail = node
            self.size += 1
            return
        else:
            self.tail.next = node
            self.tail = node

    def listExtend(self, arr2):
        prev, cur = None, self.head
        value = arr2.tail
        if cur.data <= value.data:
            arr2.tail.next = self.head
            self.head = arr2.head
        else:
            while cur.next is not None:
                prev = cur
                cur = cur.next
                if cur.data <= value.data:
                    prev.next = arr2.head
                    arr2.tail.next = cur
                    return
            self.tail.next = arr2.head
            self.tail = arr2.tail

import sys

sys.stdin = open('5110_input.txt', 'r')

for t in range(1, int(input())):
    N, M = map(int, input().split())
    arr = List()
    for value in map(int, input().split()):
        arr.insertFirst(Node(value))
        arr.printlist()
    # for _ in range(M - 1):
    #     addArr = List()
    #     for addNum in map(int, input().split()):
    #         addArr.insertlast(Node(addNum))
    #     arr.listExtend(addArr)
    #     print('#{}'. format(t), end='')
    #
    # print()





# #3. 8/10 제한시간초과 : 0.15005s
# for t in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     for _ in range(M - 1):
#         addArr = list(map(int, input().split()))
#
#         if max(arr) < addArr[0]:
#             arr.extend(addArr)
#
#         for i in range(N):
#             if arr[i] > addArr[0]:
#                 arr = arr[:i] + addArr + arr[i:]
#                 break
#     arr = list(map(str, arr[-10:]))
#     arr = ' '.join(reversed(arr))
#     print('#{} {}'. format(t, arr))

# #2. 8/10 : 제한시간 초과 0.16414s
# for t in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     for _ in range(M - 1):
#         addArr = list(map(int, input().split()))
#
#         if max(arr) < addArr[0]:
#             arr.extend(addArr)
#
#         for i in range(N):
#             if arr[i] > addArr[0]:
#                 addArr.extend(list(arr[i:]))
#                 arr = arr[:i]
#                 arr.extend(addArr)
#                 break
#
#     arr.reverse()
#     arr = ' '.join(list(map(str, arr[:10])))
#     print('#{} {}'. format(t, arr))


# #1. 6/10 : 제한시간 초과
# for t in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     for _ in range(M - 1):
#         addArr = list(map(int, input().split()))
#
#         for i in range(N):
#             if arr[i] > addArr[0]:
#                 addArr.extend(list(arr[i:]))
#                 arr = arr[:i]
#                 arr.extend(addArr)
#                 break
#         else:
#             arr.extend(addArr)
#
#     arr.reverse()
#     arr = ' '.join(list(map(str, arr[:10])))
#     print('#{} {}'. format(t, arr))
