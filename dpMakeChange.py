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