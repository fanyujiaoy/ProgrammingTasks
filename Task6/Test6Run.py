# -*- coding: utf-8 -*-
import GraphClass as gc

if __name__== '__main__':
    """
    测试
    """
    maps = [
        [-1, 1, 0, 0],
        [0, -1, 0, 0],
        [0, 0, -1, 1],
        [1, 0, 0, -1]]
    tgc = gc.GraphClass(maps)
    tgc.InsertNode()
    tgc.AddEdge(1, 4)
    print("广度优先遍历")
    tgc.BreadthFirstSearch()
    print("深度优先遍历")
    tgc.DepthFirstSearch()