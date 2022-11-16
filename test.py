import numpy as np
import copy
def deduplicate(point):
    result = copy.deepcopy(point)
    buffer = []
    for i in range(len(point)-1):
        d = np.sqrt(np.square(point[i+1][0]-point[i][0])+np.square(point[i+1][1]-point[i][1]))
        vector = [(point[i+1][0]-point[i][0])/d,(point[i+1][1]-point[i][1])]

        if d < 0.1 :
            result.remove(point[i])
            print(1)
        elif vector not in buffer:
            buffer.append(vector)
        elif vector in buffer:
            result.remove(point[i])
    return result
    

data = [(0.1,0),(4.5,0),(4.5,1.4),(4.5,2.8),(2,4),(1,3.5),(0,3)]

a = deduplicate(data)
print(a)



