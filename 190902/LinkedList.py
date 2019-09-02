class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __del__(self):
        print(self.data, '삭제')

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def printlist(self):
        if self.head is None: # 공백 리스트인지 체크
            return

        cur = self.head # 현재 위치를 저장
        print('[ ', end='')
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print(']')

    def insertlast(self, node):
        if self.head is None:
            self.head = self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insertfirst(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.size += 1

    def deletelast(self):
        if self.head is None:
            return
        prev, cur = None, self.head
        while cur.next is not None:
            prev = cur
            cur = cur.next
        if prev is None: # 한 개 밖에 없는 경우
            self.head = self.tail = None
        else: # 그 이상이 있는 경우
            prev.next = None
            self.tail = prev

        del cur
        self.size -= 1

    def deletefirst(self):
        if self.head is None: # 하나도 없을 경우
            return
        cur = self.head
        if self.head == self.tail: # 하나 있을 경우
            self.head = self.tail = None
        else: # 2개 이상 있을 경우
            self.head = cur.next
        
        del cur
        self.size -= 1
        
        

    def insertAt(self, idx, node): # 원하는 위치에 삽입 / idx : 삽입 위치, node : 삽입 노드
        if self.head is None:
            self.head = self.tail = node
        else:
            prev, cur = None, self.head
            while idx > 0 and cur is not None:
                prev = cur
                cur = cur.next
                idx -= 1

            if prev is None: # 맨 앞에 추가
                node.next = cur
                self.head = node
            elif cur is None: # 마지막에 추가
                prev.next = self.tail = node
            else: # 원하는 위치에 추가
                node.next = cur
                prev.next = node
            self.size += 1


    def deleteAt(self, idx):
        if self.head is None:
            return
        prev, cur = None, self.head
        while idx > 0 and cur.next is not None:
            prev = cur
            cur = cur.next
            idx -= 1

        if prev is None:
            self.head = cur.next
        elif cur is None:
            prev.next = None
            self.tail = prev
        else:
            prev.next = cur.next

        del cur
        self.size -= 1

