# -*- coding: utf-8 -*-
import DictClass as dc
import LRUClass as lc

if __name__== '__main__':
    """
    测试
    """
#    tdc = dc.DictClass(13)
#    tdc[54] = "cat"
#    tdc[26] = "dog"
#    tdc[93] = "lion"
#    tdc[17] = "tiger"
#    tdc[77] = "bird"
#    tdc[31] = "cow"
#    tdc[44] = "goat"
#    tdc[55] = "pig"
#    tdc[20] = "chicken"
#    print(tdc.get(54))
#    tdc.put(13,"duck")
#    print('__solts__', tdc.__solts__)
#    print('keys()', tdc.keys())
    
    tlc = lc.LRUClass()
    tlc.set('a',2)
    tlc.set('b',2)
    tlc.set('c',2)
    tlc.set('d',2)
    tlc.set('e',2)
    tlc.set('f',2)
    print(tlc.get('c'))
    print(tlc.get('b'))
    print(tlc.get('a'))
