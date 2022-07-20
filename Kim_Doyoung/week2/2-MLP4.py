import numpy as np
import matplotlib.pyplot as plt

def AND(x1, x2):
    w = np.array([[1, 2], [2, 7], [3, 4], [4, 6]])
    x = np.array([x1, x2])
    b = np.array([-0.7, -4.2, -2.3, -2.7])
    flag = np.array([0, 0, 0, 0])
    tmpA = np.sum(w[0,:]*x)
    tmpB = np.sum(w[1,:]*x)
    tmpC = np.sum(w[2,:]*x)
    tmpD = np.sum(w[3,:]*x)
    sum = 0
    
    if tmpA + b[0] > 0:
        flag[0] = 1
    if tmpB + b[1] > 0:
        flag[1] = 1
    if tmpC + b[2] > 0:
        flag[2] = 1
    if tmpD + b[3] > 0:
        flag[3] = 1
        
    if flag[0] == 1:
        sum += tmpA
    if flag[1] == 1:
        sum += tmpB
    if flag[2] == 1:
        sum += tmpC
    if flag[3] == 1:
        sum += tmpD
        
    return sum
'''    
    if flag[0] == 1 and flag[1] == 0 and flag[2] == 0 and flag[3] == 0:
        return tmpA
    elif flag[0] == 0 and flag[1] == 1 and flag[2] == 0 and flag[3] == 0:
        return tmpB
    elif flag[0] == 0 and flag[1] == 0 and flag[2] == 1 and flag[3] == 0:
        return tmpC
    elif flag[0] == 0 and flag[1] == 0 and flag[2] == 0 and flag[3] == 1:
        return tmpD
    elif flag[0] == 1 and flag[1] == 1 and flag[2] == 0 and flag[3] == 0:
        return tmpA + tmpB
    elif flag[0] == 1 and flag[1] == 0 and flag[2] == 1 and flag[3] == 0:
        return tmpA + tmpC
    elif flag[0] == 1 and flag[1] == 0 and flag[2] == 0 and flag[3] == 1:
        return tmpA + tmpD
    elif flag[0] == 0 and flag[1] == 1 and flag[2] == 1 and flag[3] == 0:
        return tmpB + tmpC
    elif flag[0] == 0 and flag[1] == 1 and flag[2] == 0 and flag[3] == 1:
        return tmpB + tmpD
    elif flag[0] == 0 and flag[1] == 0 and flag[2] == 1 and flag[3] == 1:
        return tmpC + tmpD
    elif flag[0] == 1 and flag[1] == 1 and flag[2] == 1 and flag[3] == 0:
        return tmpA + tmpB + tmpC
    elif flag[0] == 1 and flag[1] == 1 and flag[2] == 0 and flag[3] == 1:
        return tmpA + tmpB + tmpD
    elif flag[0] == 1 and flag[1] == 0 and flag[2] == 1 and flag[3] == 1:
        return tmpA + tmpC + tmpD
    elif flag[0] == 0 and flag[1] == 1 and flag[2] == 1 and flag[3] == 1:
        return tmpB + tmpC + tmpD
    elif flag[0] == 1 and flag[1] == 1 and flag[2] == 1 and flag[3] == 1:
        return tmpA + tmpB + tmpC +tmpD   
    else: return 0
'''
x = []
y = []
for i in np.arange(0, 0.6, 0.01):
    x.append(i)
    y.append(AND(i, i + 0.03))
    print(AND(i, i + 0.03))

plt.plot(x, y)
plt.scatter(x, y)
plt.show()