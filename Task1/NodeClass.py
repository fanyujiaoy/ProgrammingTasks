# -*- coding: utf-8 -*-
"""
【链表】
- 实现单链表、循环链表、双向链表，支持增删操作
- 实现单链表反转
- 实现两个有序的链表合并为一个有序链表
- 实现求链表的中间结点
"""
class SingleNode:
    def __init__(self, value, next_data=None):
        """
        :param value: 可以直接初始生成数组
        :param next_data: 指定数组长度
        """
        self.data = value
        self.next = next_data

'''
双链表由于相较于单链表每个元素多了一个向前的指针，所以占用的存储空间更大，
一个指针占用的内存空间在64位系统是8个字节，n个字节就需要多8*N个内存消耗，内存浪费严重。
'''
class DoubleNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.data = value
        self.next = next

"""
先提交，夜里继续补
"""        
class LinkList:
    def __init__(self, data, double_link=False, loop=False):
        self.header = None
        if double_link:
            self.double = True
            if data:
                if not loop:
                    self.header = DoubleNode(data[0])
                    link = self.header
                    for i in data[1:]:
                        node = DoubleNode(i, link)
                        link.next = node
                        link = link.next
                else:
                    pass