# -*- coding: utf-8 -*-
"""
堆排序 选择排序的一种，用堆积树来完成排序。
父节点i的左子节点在位置为（2*i+1），右子节点（2*i+2），子节点i的父节点在floor（（i-1）/2）
最大堆调整（MAX_Heapify）：将堆的末端子节点做调整，使得子节点小于父节点
最大堆建立（Build_Max_Heap）：将堆所在数据重新排序，从len/2开始调整，一直到第1个节点
堆排序（Heap_sort）
"""

def MAX_Heapify(heap,Heapsize,root):
    left=2*root+1
    right=left+1
    large=root
    if left<Heapsize and heap[large]<heap[left]:
        large=left
    if right<Heapsize and heap[large]<heap[right] :
        large=right
    if large!=root:
        heap[large],heap[root]=heap[root],heap[large]
        MAX_Heapify(heap,Heapsize,large)
        
def Build_Max_Heap(heap):
    Heapsize=len(heap)
    for i in xrange((Heapsize-2)//2,-1,-1):
        MAX_Heapify(heap,Heapsize,i)

def Heap_sort(heap):
    Build_Max_Heap(heap)
    for i in range(len(heap)-1,-1,-1):
        heap[0],heap[i]=heap[i],heap[0]
        MAX_Heapify(heap,i,0)
    return heap

heap=Heap_sort([4,2,5,8,2,9,7,1])
print(heap)