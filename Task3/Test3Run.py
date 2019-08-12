# -*- coding: utf-8 -*-
import SortClass as sc
import BinarySearch as bs

if __name__== '__main__':
    """
    测试
    """
    tsc = sc.SortClass()
    
    tbs = bs.BinarySearch()
    data=list(range(1, 100000))
    tbs.binarysearch(data, 6666)