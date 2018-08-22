# -*- coding: utf-8 -*-
"""
希尔排序 实质是分组插入排序，又称缩小增量排序
"""
def shell_sort(lists):
    step=len(lists)/2
    while step>0 :
        for i in range(step,len(lists)):
            while(i>=step and lists[i]<lists[i-step]):
                lists[i],lists[i-step]=lists[i-step],lists[i]
                i-=step
        step /=2
    return lists

lists=shell_sort([3,4,2,5,1,6])
print(lists)
