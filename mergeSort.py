def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0

        while i < len(lefthalf) and j<len(righthalf):
            # 拉链式交错把左右半部从小到大归并到结果列表中
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                # 之所以从 k = 0 开始是因为当前alist为当前递归体的局部变量
                # 并不是总体的alist，所以返回的alist也只是上一步alist中的
                # 左半或者右半部分
            
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf): # 归并左半部分剩余项
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf): #归并右半部分剩余项
            alist[k] = righthalf[j]
            j += 1
            k += 1

alist = [20, 30, 40, 90, 50, 60, 70 ,80, 100, 110]
mergeSort(alist)
print(alist)

