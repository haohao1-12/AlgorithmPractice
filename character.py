import math
def func(string):

    # please define the python3 input here. For example: a,b = map(int, input().strip().split())
    #string = input()
    # please finish the function body here.
    hash ={}
    for i in string:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] += 1
    result = 1
    for i in hash:
        result *= math.factorial(hash[i])
    result = math.factorial(len(string))/result
    print(result)
    # please define the python3 output here. For example: print().
if __name__ == "__main__":
    func('ABA')