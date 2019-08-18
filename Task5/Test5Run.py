# -*- coding: utf-8 -*-
import BinaryTreeClass as bc

if __name__== '__main__':
    """
    测试
    """
    tbc = bc.BinaryTree('Tree')  # 构建树
    A = tbc.insertLeft('A')
    C = A.insertLeft('C')
    D = A.insertRight('D')
    F = D.insertLeft('F')
    G = D.insertRight('G')
    B = tbc.insertRight('B')
    E =B.insertRight('E')
    print('*************************')
    print('Binary Tree pre-traversal')
    bc.preOrder(tbc)
    print('*************************')
    print('Binary Tree mid-traversal')
    bc.midOrder(tbc)
    print('*************************')
    print('Binary Tree post-traversal')
    bc.postOrder(tbc)