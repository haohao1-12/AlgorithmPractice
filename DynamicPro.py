tr = [None, {'w':2,'v':3}, {'w':3,'v':4},
            {'w':4,'v':8}, {'w':5,'v':8},
            {'w':9,'v':10}]
            
max_w = 20

# 初始化二维表格m[(i,w)]
# 表示前i个宝物，最大重量w的组合，所得到的最大价值
# 当i什么都不取，或者w上限为0，价值均为0

m = {(i, w):0 for i in range(len(tr)) for w in range(max_w + 1)}

for i in range(1, len(tr)):
    for w in range(1, max_w + 1):
        if tr[i]['w'] > w:
            m[(i, w)] = m[(i-1,w)] # 装不下第i个宝物
        else:
            # 不装第i个宝物，装第i个宝物，两种情况下最大价值
            m[(i, w)] = max(m[(i-1, w)], m[(i-1, w-tr[i]['w'])] + tr[i]['v'])

print(m[(len(tr) - 1, max_w)])

