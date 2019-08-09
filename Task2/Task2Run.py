# -*- coding: utf-8 -*-
import StackClass as sc
import QueueClass as qc
import RecursiveClass as rc

if __name__== '__main__':
    """
    测试
    """
    tas = sc.ArrayStack()
    tas.push(4)
    print("栈顶元素为："+str(tas.top()))
    print("栈大小为："+str(tas.size()))
    tas.pop()
    print("弹栈成功")
    tas.pop()
    """
    栈顶元素为：4
    栈大小为：1
    弹栈成功
    栈已经为空
    """
    
    tns = sc.NodeStack()
    tns.push(1)
    print("栈顶元素为："+str(tns.top()))
    print("栈大小为："+str(tns.size()))
    tns.pop()
    print("弹栈成功")
    tns.pop()
    """
    栈顶元素为：1
    栈大小为：1
    弹栈成功
    栈已经为空
    """
    
    
    taq = qc.ArrayQueue()
    taq.enQueue(1)
    taq.enQueue(2)
    
    print("队列头元素为："+str(taq.getFront()))
    print("队列尾元素为："+str(taq.getBack()))
    print("队列的大小为："+str(taq.size()))
    
    taq.deQueue()
    print("队列头元素为："+str(taq.getFront()))
    print("队列尾元素为："+str(taq.getBack()))
    print("队列的大小为："+str(taq.size()))
    """
    队列头元素为：1
    队列尾元素为：2
    队列的大小为：2
    队列头元素为：2
    队列尾元素为：2
    队列的大小为：1
    """
    
    trs = rc.Recursive()
    for i in range(1, 20):
        print(trs.fibonacciseq(i))

    print(trs.factorial(4))