import sys

sys.stdin = open('5120_input.txt', 'r')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.forward = None
class List:
    def __init__(self):
        self.head = None
        self.tail = None
    def printList(self):
        if self.head is None:
            return
        cur = self.head
        while cur is not None:
            print(' {}'.format(cur.data), end='')
            cur = cur.next
        print()
    def insertLast(self):
        pass
    def insertAt(self):
        pass
    def insertFirst(self, node):
        if self.head is None:
            self.head = self.tail = node
            return
        else:
            node.next = self.head
            self.head.forward = node
            self.head = node


for t in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    nums = List()
    for num in map(int, input().split()):
        nums.insertFirst(num)
    nums.printList()

