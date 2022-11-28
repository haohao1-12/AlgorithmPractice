def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
    if first < last: # 基本结束条件
        splitpoint = partition(alist, first, last) # 分裂

        quickSortHelper(alist, first, splitpoint - 1) # 递归调用
        quickSortHelper(alist, splitpoint + 1, last)

def partition(alist, first, last):
    pivotValue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotValue:
            leftmark += 1
        while alist[rightmark] >= pivotValue and rightmark >= leftmark:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark





alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)

