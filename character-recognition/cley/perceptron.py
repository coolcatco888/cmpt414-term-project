from random import random, uniform
import numpy as np
import matplotlib.pyplot as plot

class Perceptron:

    x = []              # inputs
    theta = 0.0         # threshold
    maxTime = 1000      # max time steps
    w = []              # weights
    y = []              # outputs
    d = []              # desired outputs
    n = 0.1             # gain factor

    # Steps 1 and 2
    def __init__(self, x, theta, maxTime, d, n):
        self.x = x
        self.theta = theta
        self.maxTime = maxTime
        self.d = d # Step 2
        self.n = n
        self.w.append([random() for i in range(len(x))]) # Step 1
        
    # Hardlimiter Function
    def fh(self, alpha):
        retval = 1
        if(alpha < 0):
            retval = -1
        return retval

    # Step 3
    def calculate_output(self, t):
        summation = 0
        for i in range(len(x)):
            summation += self.w[t][i] * self.x[i] - self.theta
        self.y.append(self.fh(summation))

    # Step 4
    def adapt_weights(self, t):
        weights = []
        for i in range(len(x)):
            weights.append(self.w[t][i] + self.n * (self.d[t] - self.y[t]) * self.x[i])
            if self.x[i] > self.y[t]:
                self.d.append(-1.0)
            else:
                self.d.append(1.0)
        self.w.append(weights)


    def final_output(self):
        for t in range(maxTime):
            self.calculate_output(t)
            self.adapt_weights(t)
        return self.y

if __name__ == "__main__":
    x = [uniform(-10.0, 10.0) for i in range(1)]
    theta = 0.1
    maxTime = 100
    d = [1]
    n = 0.15
    p = Perceptron(x, theta, maxTime, d, n)
    y = p.final_output()
    print "y = ", y[maxTime - 1]
    print "end"