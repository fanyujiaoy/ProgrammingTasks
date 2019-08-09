# -*- coding: utf-8 -*-

a = 1
b = [1, 3]


import ArrayClass as Array


if __name__ == '__main__':
    array = Array.ArrayClass(1, 2, 3,size=5, fixed_size=True)
    print('Array',array)
    array.update(2, 9)
    print('Array',array)
    