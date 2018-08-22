# -*- coding: UTF-8 -*-

'''
归并排序 分治法
将已有序的子序列合并，即先将每个子序列有序，再使子序列段有序。若将两个有序表合成一个有序表，
称为二路并归
[4，7，8，3，5，9]-->[4,7,8][3,5,9]-->[4][7,8][3][5,9]-->[4][7][8][3][5][9]  树形图
合并 先合并[7,8],再合并[4,7,8],再合并[5.9],再合并[3,5,9],再合并[3,4,5,7,8,9]
每次比较两个序列中第一个元素大小，小的加入序列中
'''
def merge_sort(array):
    def merge_arr(arr_l,arr_r):
        array=[]
        while len(arr_l)>0 and len(arr_r)>0:
            if arr_l[0]<=arr_r[0]:
                array.append(arr_l.pop[0])
            elif arr_l[0]>arr_r[0]:
                array.append(arr_r.pop[0])
        if len(arr_l)!=0:
            array+=arr_l
        elif len(arr_r)!=0:
            array+=arr_r
        return array
    
    def recursive(array):
        if len(array)==1:
            return array
        mid=len(array)//2
        arr_l=recursive(array[:mid])
        arr_r=recursive(array[mid:])
        return merge_arr(arr_l,arr_r)
    return recursive(array)

array=merge_sort([4,7,8,2,5,9])
print(array)
