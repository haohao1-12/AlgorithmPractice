def shellSort(alist):
    sublistcount = len(alist) // 2 # 间隔设定
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertSort(alist, startposition, sublistcount) # 子列表排序

        print("After increments of size", sublistcount, "The list is", alist)

        sublistcount = sublistcount // 2 # 间隔缩小

    

def gapInsertSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentValue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentValue:
            alist[position] = alist[position-gap]
            position -= gap

        alist[position] = currentValue

alist = [20, 30, 40, 90, 50, 60, 70 ,80, 100, 110]
shellSort(alist)
print(alist)
