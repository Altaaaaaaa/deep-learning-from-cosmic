import numpy as np

def AND(x1, x2):
    w1, w2 = 0.5, 0.5
    imgye = 0.7
    tmp = w1*x1 + w2*x2
    if tmp <= imgye:
        return 0
    elif tmp > imgye:
        return 1

def NAND(x1, x2):
    w1, w2, theta = -0.5, -0.5, -0.7
    tmp = w1*x1 + w2*x2
    if theta > tmp:
        return 0
    elif theta <= tmp:
        return 1

def OR(x1, x2):
    w1, w2, b = 0.5, 0.5, -0.2
    tmp = w1*x1 + w2*x2 + b
    if tmp <= 0:
        return 0
    else:
        return 1