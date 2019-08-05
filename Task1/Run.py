# -*- coding: utf-8 -*-
import ArrayClass as Array

# 在加班，先提交，夜里回去补上
if __name__ == '__main__':
    array = Array.ArrayClass(1, 2, 3,size=5, fixed_size=True)
    print('Array',array)
    array.update(2, 9)
    print('Array',array)
    