'''
动态规划算法采用了一种更有条理的方式来得到问题的解
找零兑换的动态规划算法从最简单的“1分钱找零”的最优解开始，逐步狄加上去，知道我们需要的
找零前述
在找零低价的过程中，设法保持每一分钱的低价都是最优解，一直加到求解找零钱数，
得到最优解
'''

def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(1, change+1):
        # initialization the max value
        coinCount = cents
        # subtract each coin, back check minimum coin quantity, and 
        # record the total minimum value
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        minCoins[cents] = coinCount

    return minCoins[change]

print(dpMakeChange([1, 5, 10, 21, 25], 63, [0] * 64))

'''
前面的算法已经得到了最少硬币的数量，但没有返回硬币如何组合
扩展思路是在生成最优解列表的同时跟踪记录所选择的那枚硬币币值
在得到最后的解之后，减去选择的硬币币值，回溯到表格之前的部分找零
就能逐步得到每一步所选择的硬币的币值
'''

def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change + 1): 
        coinCount = cents
        newCoin = 1 # initialize next new coin
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

amnt = 63
clist = [1,5,10,21,25]
coinsUsed = [0]*(amnt+1)
coinCount = [0]*(amnt+1)

print("Making change for", amnt, "requires")
print(dpMakeChange(clist, amnt, coinCount, coinsUsed), "coins")
print("They are:")
printCoins(coinsUsed, amnt)
print("The used list is as follows:")
print(coinsUsed)