from random import random, uniform
import numpy as np
import matplotlib.pyplot as plot

class Perceptron:

    x = [][]    # inputs
    kLayers = 1 # number of layers
    theta = 0.0 # threshold
    maxTime     # max time steps
    w = [][]    # weights
    y = []      # outputs
    d = []      # desired outputs
    n = 0.1     # gain factor

    # Steps 1 and 2
    def __init__(self, x, theta, kLayers, maxTime, d, n):
        self.x[0] = x
        self.theta = theta
        self.kLayers = kLayers
        self.maxTime = maxTime
        self.d = d # Step 2
        self.n = n
        self.w[0] = [random() for i in range(len(x))] # Step 1
        
    # Hardlimiter Function
    def fh(alpha):
        retval = 1
        if(alpha < 0)
            retval = -1
        return retval

    # Step 3
    def calculateOutput():
        summation = 0
        for i in range(len(x)):
            summation += w[t][i] * x[t][i] - theta
        y[t] = fh(summation)

    # Step 4
    def adaptWeights():
        for i in range(len(x)):
            w[t + 1][i] = w[t][i] + n * (d[t] - y[t]) * x[t][i]

    def finalOutput():
        for t in range(maxTime):
            self.calculateOutput()
            self.adaptWeights()
        return y

