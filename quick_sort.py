# -*- coding: utf-8 -*-
"""
快速排序 （冒泡排序的升级版）通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比
另一部分所有数据要小，然后在按此方法对两部分数据分别进行快速排序，整个排序过程可以递归进行
"""
def quick_sort(lists):
    if len(lists)<=1:
        return lists
    less=[]
    great=[]
    base=lists.pop()
    for x in lists:
        if x<base:
            less.append(x)
        else:
            great.append(x)
    return quick_sort(less)+[base]+quick_sort(great)
lists=quick_sort([3,4,2,5,1,6])
print(lists)
