
# -*- coding: utf-8 -*-
"""
【数组】 
- 实现一个支持动态扩容的数组  
- 实现一个大小固定的有序数组，支持动态增删改操作  
- 实现两个有序数组合并为一个有序数组 
"""
class ArrayClass:
    def __init__(self, *args, size=None, fixed_size=False):
        """
        :param args: 可以直接初始生成数组
        :param size: 指定数组长度
        :param fixed_size: 指定数组是否长度固定
        """
        if not isinstance(fixed_size, bool) and fixed_size:
            raise TypeError("fixed_size类型错误，需为bool类型")    
        
        # 设置默认值
        self._size = 0
        self.is_empty = True
        self._data = []
        self._fixed = fixed_size
        
        """
        先判断数组是否有数据
        如果有数据，再判断长度是否固定，默认为False不固定，如果为True就固定
        如果无数据，再判断是否有指定长度，如果有指定长度，就默认长度固定，用None填充
        """
        if args:    # 如果数组有数据
            self.is_empty = False
            self._data = [i for i in args]
            if self._fixed:     # 如果固定就进if，如果不固定就无限制
                if not isinstance(size, int):
                    raise TypeError("size类型错误，需为int类型")
                self._size = size
                if len(self._data) > self._size:
                    raise TypeError("数组越界，请修改")
                else:
                    # 当长度固定时，无值的元素设置为None
                    none_data = [None] * (self._size - len(self._data))
                    self._data += none_data
#            else:               # 如果不固定
#                self.is_empty = False
        else:   # 如果数组无数据
            if size:    # 如果无数据时又固定了长度
                if not isinstance(size, int):
                    raise TypeError("size类型错误，需为int类型")
                self._size = size
                self._fixed = True
                self._data = [None] * self._size
          

    def __str__(self):
        str_res = """
        用__str__方法打印数组的情况：
        Array: {array}
        empty: {empty}
        length: {length}
        fixed: {fixed}
        """.format(array=self._data, empty=self.is_empty, length=self._size, fixed=self._fixed)
        return str_res

    def insert(self, index, value):
        """
        指定位置增加值
        """
        if not isinstance(index, int):
            raise TypeError("index类型错误，需为int类型")
        
        if self._fixed:     # 如果数组长度固定
            if index >= self._size:
                raise IndexError("索引越界，请修改")
            else:
                self._data = self._data[:index] + [value] + self._data[index: -1]
        else:       # 如果数组长度不固定
            # 剩下的慢慢优化
            # 比如当前数组的长度是5时，却在第11个位置增加值，中间要变成None
            self._data = self._data[:index] + [value] + self._data[index:]
    
    def delete(self, index):
        """
        指定位置删除值
        """
        if not isinstance(index, int):
            raise TypeError("index类型错误，需为int类型")
        if self.is_empty:
            raise IOError("当前数组无数据")
        else:
            if index >= self._size:
                raise IndexError("索引越界，请修改")
            else:
                self._data = self._data[:index] + self._data[index + 1:]
                if self._fixed:
                    self._data += [None]
            
    def update(self, index, value):
        """
        指定位置修改值
        """
        if not isinstance(index, int):
            raise TypeError("index类型错误，需为int类型")
        if self.is_empty:
            raise IOError("当前数组无数据")
        else:
            if index >= self._size:
                raise IndexError("索引越界，请修改")
            else:
                self._data = self._data[:index] + [value] + self._data[index + 1:]

    
    def append(self, value):
        """
        合并有序数组
        下次完善
        """
        pass




