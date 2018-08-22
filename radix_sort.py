# -*- coding: utf-8 -*-
"""
基数排序（桶排） 
例如【123，2，9，23，41，43】先根据个位数，在走访元素时分配到编号为0到9的木桶中，【41】【2】【123，23，43】【9】-->【41，2，123，23，43，9】
再根据十位数，分配 【2,9】【123，23】【41，43】-->【2.9.123.23.41.41】
再根据百位数，分配【2，9，23，41，43】【123】-->【2.9.23.41.43.123】
直到木桶中的第一个桶中元素个数==len(lists)
"""
def radix_sort(lists):
    bucket,digit=[[]],0
    while len(bucket[0])!=len(lists):
        bucket=[[],[],[],[],[],[],[],[],[],[]]
        for i in range (len(lists)):
            num=(lists[i]//10**digit)%10
            bucket[num].append(lists[i])
        del lists[:]
        for i in range(len(bucket)):
            lists +=bucket[i]
        digit+=1
    return lists

lists=radix_sort([123,2,4,23,42,41])
print(lists)