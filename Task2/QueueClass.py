# -*- coding: utf-8 -*-
"""
【队列】
先进先出
用数组实现一个顺序队列
用链表实现一个链式队列
实现一个循环队列
"""
class ArrayQueue:
    """队列"""
    def __init__(self):
        self.items = []
        self.front = 0  # 队列头
        self.rear = 0   # 队列尾

    def is_empty(self):
        """判断队列是否为空"""
        return self.items == self.rear

    def enQueue(self, item):
        """进队列，从队尾加入"""
        self.items.append(item)
        self.rear += 1
        # self.items.insert(0,item)     # 从对头进

    def deQueue(self):
        """出队列，从队头出"""
        if self.rear > self.front:
            self.front += 1
        else:
            print("队列已经为空")
        # return self.items.pop()   # 从对尾出

    def getFront(self):
        if self.is_empty():
            return None
        return self.items[self.front]

    def getBack(self):
        if self.is_empty():
            return None
        return self.items[self.rear-1]

    def size(self):
        """返回大小"""
        return self.rear - self.front
        # return len(self.items)	# 看大小

class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None

class NodeQueue:
    def __init__(self):
        """分配头结点"""
        self.pHead = None
        self.pEnd = None

    def is_empty(self):
        """判断是否为空"""
        if self.pHead == None:
            return True
        return False

    def size(self):
        """获取队列的大小"""
        size=0
        p = self.pHead
        while p != None:
        # while p is not None:
            p = p.next
            size += 1
        return size

    def enQueue(self, element):
        """入队列，从队尾加"""
        p = LNode(element)
        p.data = element
        p.next = None
        if self.pHead == None:
            self.pHead = self.pEnd=p
        else:
            self.pEnd.next = p
            self.pEnd = p

    def deQueue(self):
        """出队列，删除首元素"""
        if self.pHead == None:
            print("出队列失败，队列已经为空")
        self.pHead = self.pHead.next
        if self.pHead == None:
            self.pEnd = None

    def getFront(self):
        """返回队列首元素"""
        if self.pHead == None:
            print("获取队列首元素失败，队列已经为空")
            return None
        return self.pHead.data

    def getBack(self):
        """返回队列尾元素"""
        if self.pEnd == None:
            print("获取队列尾元素失败，队列已经为空")
            return None
        return self.pEnd.data