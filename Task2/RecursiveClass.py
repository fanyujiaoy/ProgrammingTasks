# -*- coding: utf-8 -*-
class Recursive:
    
    """
    斐波那契数列
    """
    def fibonacciseq(self, number):
        if number <= 1:
            return number
        return self.fibonacciseq(number-1) + self.fibonacciseq(number-2)
    
    """
    求阶乘：求n!
    """
    def factorial(self, number):
        if number <= 1:
            return 1
        else:
            return number * self.factorial(number - 1)