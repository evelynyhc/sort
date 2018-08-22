# -*- coding: utf-8 -*-
"""
选择排序 第一趟，在序列中找到最小的，将它与第0个元素交换，第二趟，在剩下的序列中找到最小的，将它与第一个
元素交换，以此类推
"""
def select_sort(lists):
    for i in range(0,len(lists)):
        x=i
        for j in range(i,len(lists)):
            if lists[j]<lists[x]:
                x=j
        lists[i],lists[x]=lists[x],lists[i]
    return lists

lists=select_sort([3,4,2,5,1,6])
print(lists)