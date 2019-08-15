# -*- coding: utf-8 -*-

class DictClass:
    def __init__(self, num):
        self.__solts__ = []
        self.num = num
        for _ in range(num):
            self.__solts__.append([])
            
    def hash_fun(self,key,num):
        hashval = 0
        x = key
        if x < 0:
                print("the key is low")
                return
        while x != 0:
                hashval = (hashval << 3) + x % 10
                x /= 10
        return hashval % num
    
    def put(self, key, value):
        i = self.hash_fun(key,self.num) % self.num
        for p, (k, v) in enumerate(self.__solts__[i]):
            if k == key:
                break
        else:
            self.__solts__[i].append((key, value))
            return
        self.__solts__[i][p] = (key, value)
    def get(self, key):
        i = self.hash_fun(key,self.num) % self.num
        for k, v in self.__solts__[i]:
            if k == key:
                return v
        raise KeyError(key)
    # keys函数
    def keys(self):
        ret = []
        for solt in self.__solts__:
            for k, _ in solt:
                ret.append(k)
        return ret
    
    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)