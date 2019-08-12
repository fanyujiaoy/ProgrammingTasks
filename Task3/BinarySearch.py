# -*- coding: utf-8 -*-
class BinarySearch:
    
    def binarysearch(self, data, find):
        #取中位数
        mid=int(len(data)/2)
     
        if len(data)>=1:
            
            if data[mid] > find:
                # 中位数大于要查找的数，则要查找的数在左半部分，继续调用二分算法进行查找
                self.binarysearch(data[:mid], find)
            elif data[mid] < find:  
                # 中位数小于要查找的数，则要查找的数在右半部分
                self.binarysearch(data[mid:], find)
            else:   
                #中位数等于要查找的数
                print("找到了：",data[mid])
        else:
            print("没有找到")