def func(string):

    # please define the python3 input here. For example: a,b = map(int, input().strip().split())
    #string = input()
    # please finish the function body here.
    table = ['a','e','i','o','u','A','E','I','O','U']
    buffer = [0]*len(string)
    for i in range(len(string)):
        if string[i] in table and ord(string[i]) in range(97,123):
            buffer[i] = chr(ord(string[i])-32)
        elif string[i] not in table and ord(string[i]) in range(65,90):
            buffer[i] = chr(ord(string[i])+32)
        else:
            buffer[i] = string[i]
    # please define the python3 output here. For example: print().
    print("".join(buffer))

if __name__ == "__main__":
    func("Who Love Solo")