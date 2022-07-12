import numpy as np

def AND(x1):
    w = np.array([3, 0.5])
    x = np.array([x1])
    b = np.array([-0.1, -0.05])
    flag = np.array([0, 0])
    tmpA = w[0]*x
    tmpB = w[1]*x
    
    if tmpA + b[0] <= 0:
        flag[0] = 0
    elif tmpA + b[0] > 0:
        flag[0] = 1
        
    if tmpB + b[1] <= 0:
        flag[1] = 0
    elif tmpB + b[1] > 0:
        flag[1] = 1
    
    if flag[0] == 1\
        and flag[1] == 0:
            return tmpA
    elif flag[0] == 0\
        and flag[1] == 1:
            return tmpB
    elif flag[0] == 1\
        and flag[1] == 1:
            return tmpA + tmpB
    else: return 0

for i in np.arange(0, 0.21, 0.01):
    print(AND(i))
