import numpy as np
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = 0.5
    tmp = np.sum(w*x) + b
    if tmp >= 1:
        return 1
    else:
        return 0

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = 0.2
    tmp = np.sum(w*x) + b
    if tmp < 1:
        return 1
    else:
        return 0

def XOR(x1, x2):
    x=np.array([x1, x2])
    return AND(OR(x[0], x[1]), NAND(x[0], x[1]))