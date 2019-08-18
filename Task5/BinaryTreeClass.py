# -*- coding: utf-8 -*-

class BinaryTree:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None
    
    # 向左子树插入节点
    def insertLeft(self,value):
        self.left = BinaryTree(value)
        return self.left
    
    # 向右子树插入节点
    def insertRight(self,value):
        self.right = BinaryTree(value)
        return self.right
    
    # 输出节点数据
    def show(self):
        print(self.data)
        
 
# 先序遍历
def preOrder(node):
    if node.data:
        node.show()
        if node.left:
            preOrder(node.left)
        if node.right:
            preOrder(node.right)
# 中序遍历
def midOrder(node):
    if node.data:
        if node.left:
            midOrder(node.left)
        node.show()
        if node.right:
            midOrder(node.right)
# 后序遍历
def postOrder(node):
    if node.data:
        if node.left:
            postOrder(node.left)
        if node.right:
            postOrder(node.right)
        node.show()
