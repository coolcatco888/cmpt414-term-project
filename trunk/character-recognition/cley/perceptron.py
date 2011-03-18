from random import random, uniform
import numpy as np
import matplotlib.pyplot as plot

class Perceptron:

    x = [][]    # inputs
    theta = 0.0 # threshold
    maxTime     # max time steps
    w = [][]    # weights
    y = []      # outputs
    d = []      # desired outputs
    n = 0.1     # gain factor

    # Steps 1 and 2
    def __init__(self, x, theta, maxTime, d, n):
        self.x.append(x)
        self.theta = theta
        self.maxTime = maxTime
        self.d = d # Step 2
        self.n = n
        self.w.append([random() for i in range(len(x))]) # Step 1
        
    # Hardlimiter Function
    def fh(alpha):
        retval = 1
        if(alpha < 0)
            retval = -1
        return retval

    # Step 3
    def calculateOutput(t):
        summation = 0
        for i in range(len(x)):
            summation += self.w[t][i] * self.x[t][i] - self.theta
        y.append(self.fh(summation))

    # Step 4
    def adaptWeights(t):
    weights = []
        for i in range(len(x)):
            weights.append(self.w[t][i] + self.n * (self.d[t] - self.y[t]) * self.x[t][i])
    w.append(weights)

    def finalOutput():
        for t in range(maxTime):
            self.calculateOutput(t)
            self.adaptWeights(t)
        return y

if __name__ == "__main__":
    x = [random() for i in range(3)]
    theta = 0.1
    maxTime = 1000
    d = [1]
    n = 0.15
    p = Perceptron(x, theta, maxTime, d, n)
