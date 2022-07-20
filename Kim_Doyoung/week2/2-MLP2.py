import numpy as np
import matplotlib.pyplot as plt

def AND(x1, x2):
    aw = np.array([[1], [2]])
    bw = np.array([[2], [7]])
    x = np.array([x1, x2])
    b = np.array([-0.1, -0.5])
    flag = np.array([0, 0])
    tmpA = np.sum(aw*x)
    tmpB = np.sum(bw*x)
    
    if tmpA + b[0] > 0:
        flag[0] = 1
    if tmpB + b[1] > 0:
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

# x = []
# y = []
# for i in np.arange(0, 0.16, 0.01):
    x.append(i)
    y.append(AND(i, i + 0.03))

x = np.arange(0, 0.3, 0.01)
y = AND(x, x + 0.03)
# ValueError: operands could not be broadcast together with shapes (2,) (2,30)
# x축과 y축 데이터의 개수가 맞지 않으면 뜨는 에러
# 왜??

'''
plt.plot(x, y)
plt.scatter(x, y)
plt.show()
'''