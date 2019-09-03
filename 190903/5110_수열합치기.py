
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

    def printTen(self):
        if self.head is None:
            return
        cur = self.head
        for _ in range(10):
            print(' {}'.format(cur.data), end='')
            cur = cur.next
        print()

    def deleteLast(self):
        if self.head is None:
            return
        prev, cur = None, self.head
        while cur.next is not None:
            prev = cur
            cur = cur.next
        if prev is None:
            self.head = self.tail = None
        else:
            prev.next = None
            self.tail = prev
        del cur

    def printLast(self):
        cur = self.tail
        print(' {}'.format(cur.data), end='')

    def insertLast(self, node):
        if self.head is None:
            self.head = self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = node

    # def insertFirst(self, node):
    #     if self.head is None:
    #         self.head = self.tail = node
    #         return
    #     else:
    #         node.next = self.head
    #         self.head = node

    def listExtend(self, arr2):
        prev, cur = None, self.head
        value = arr2.head
        while cur.data < value.data and cur.next is not None:
            prev = cur
            cur = cur.next
        if prev is None:
            arr2.tail.next = cur
            self.head = arr2.head
            return
        elif cur.next is None:
            cur.next = arr2.head
            self.tail = arr2.tail
            return
        else:
            arr2.tail.next = cur.next.next
            cur.next = arr2.head
            return

import sys

sys.stdin = open('5110_input.txt', 'r')

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = List()
    for value in map(int, input().split()):
        arr.insertLast(Node(value))
    for _ in range(M - 1):
        addArr = List()
        for addNum in map(int, input().split()):
            addArr.insertLast(Node(addNum))

        arr.listExtend(addArr)

    print('#{}'. format(t), end='')
    for _ in range(10):
        arr.printLast()
        arr.deleteLast()
    print()