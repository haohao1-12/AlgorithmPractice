'''
基本结束条件：需要兑换的找零，期勉之正好等于某种硬币
减小问题规模：
numCoins = min{1+numCoins(originalamount - 1)
               1+numCoins(originalamount - 5)
               1+numCoins(originalamount - 10)
               1+numCoins(originalamount - 25)}
'''
def recMC(coinValueList,change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
         for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
                
    return minCoins

import time
start = time.time()
print(recMC([1,5,10,25],63))
end = time.time()

print(end-start)

'''
这个算法的中间结果就是部分找零的最优解，
在递归调用的过程中已经得到的最优解被记录下来。
在递归调用之前，先查找表中是否已有部分找零的最优解
如果有，直接返回最优解而不进行递归调用，
如果没有，才进行递归调用
'''
def recDC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i, knownResults)

            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins

    return minCoins

start = time.time()
print(recDC([1, 5, 10, 25], 63, [0]*64))
end = time.time()
print(end-start)