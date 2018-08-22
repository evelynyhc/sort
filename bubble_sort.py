'''
冒泡排序，重复走访要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来，直至排序完成
'''
def bubble_sort(lists):
    count=len(lists)
    for i in range (0,count):
        for j in range(i+1,count):
            if lists[i]>lists[j]:
                lists[i],lists[j]=lists[j],lists[i]
    return lists

lists=bubble_sort([4,3,6,2,8,1])
print(lists)