# -*- coding: utf-8 -*-
"""
【栈】
先进后出
用数组实现一个顺序栈
用链表实现一个链式栈
编程模拟实现一个浏览器的前进、后退功能（选做）
"""
class ArrayStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断是否为空"""
        return self.items == []

    def size(self):
        """返回栈的大小"""
        return len(self.items)

    def push(self, item):
        """压栈(加入元素)"""
        self.items.append(item)


    def pop(self):
        """弹栈(弹出元素)"""
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print("栈已经为空")
            return None

    def top(self):
        """返回栈顶元素"""
        if not self.is_empty():
            return self.items[len(self.items) - 1]
        else:
            return None
        
class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None

class NodeStack:
    def __init__(self):
        #pHead = LNode
        self.data = None
        self.next = None

    def is_empty(self):
        """判断是否为空"""
        if self.next == None:
            return True
        return False

    def size(self):
        """返回栈的大小"""
        size=0
        p = self.next
        while p != None:
        # while p is not None:
            p = p.next
            size += 1
        return size

    def push(self, element):
        """压栈(加入元素)"""
        p = LNode(element)
        p.data = element
        p.next = self.next
        self.next = p

    def pop(self):
        """弹栈(弹出元素)"""
        tmp = self.next
        if tmp != None:
            self.next = tmp.next
        print("栈已经为空")
        return None

    def top(self):
        """返回栈顶元素"""
        if self.next != None:
            return self.next.data
        print("栈已经为空")
        return None