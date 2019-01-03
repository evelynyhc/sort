# -*- coding: utf-8 -*-
"""
插入排序，将一个数据插入到已经排好序的有序数据中，从而得到一个新的，个数加一的有序数据，适用于少量数据的排序
将插入的元素与有序序列中的元素逐个比较，直到找的比该元素小和大中间的合适位置，插入元素
"""
def insert_sort(lists):
    count=len(lists)
    for i in range(1,count):
        key=lists[i]
        j=i-1
        while j>=0 and key<lists[j]:
            lists[i]=lists[j]
            j-=j
        lists[j+1]=key   
    return lists
lists=insert_sort([4,3,6,2,7,1])
print(lists)        
