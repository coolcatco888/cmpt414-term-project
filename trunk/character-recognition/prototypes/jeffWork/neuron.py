from random import random, uniform, seed
from math import e

import matplotlib.pyplot as plot
import numpy as np

class Neuron:
    """A simplified 'forgetful' neuron"""
    
    #Initializes a neuron with these arguments
    #It is strongly recomended that you set bGain to zero
    def __init__(self, inputs, gain, moment, r = [0.0, 1.0]):
        self.numInputs = inputs
        if len(r) != 2:
            self.weights = [random() for i in range(inputs)]
            self.bias = random()
        else:
            self.weights = [uniform(r[0], r[1]) for i in range(inputs)]
            self.bias = uniform(r[0], r[1])
        self.gain = gain
        self.moment = moment
        self.oldWeights = self.weights
        self.oldBias = self.bias

    def getNumInputs(self):
        return self.numInputs

    def getWeights(self):
        return self.weights

    def getBias(self):
        return self.bias

    def getGain(self):
        return self.gain

    def getMoment(self):
        return self.moment

    def calculate(self, inputs):
        #print "Neuron", self, "calculating", inputs
        if len(inputs) != len(self.weights):
            return 0.0
        
        s = 0.0
        for i in range(self.numInputs):
            s = s + self.weights[i] * inputs[i]
            #print "    Running sum", s
        
        #print "    Adding bias", self.bias
        s = s + self.bias
        #print "    Sigmoid result", self.sigmoid(s)
        return self.sigmoid(s)

    def learn(self, inputs, error):
        #print "Neuron", self, "learning for inputs", inputs, "with error", error
        #print "    Old weights were", self.weights
        g = self.gain
        m = self.moment
        newWeights = [w + g * error * i + m * (w - o) for w, i, o in zip(self.weights, inputs, self.oldWeights)]
        self.oldWeights = self.weights
        self.weights = newWeights
        #print "    New weights are", self.weights
        #print "    Old bias was", self.bias

        newBias = self.bias + g * error + m * (self.bias - self.oldBias)
        self.oldBias = self.bias
        self.bias = newBias
        #print "    New bias is", self.bias

    def sigmoid(self, x):
        #print "Sigmoiding", x
        #if x < -500.0:
            #x = -500.0
        #if x > 500.0:
            #x = 500.0
        r = 1 / (1 + (e ** -x))
        #if r > 0.9999999999:
            #r = 1.0
        #if r < 0.0000000001:
            #r = 0.0
        return r

if __name__ == "__main__":
    def nextC((r, g, b)):
        r = r + 0.1
        if r > 1.0:
            r = 0.0
            g = g + 0.1
        if g > 1.0:
            g = 0.0
            b = b + 0.1
        if b > 1.0:
            b = 0.0
        return (r, g, b)
    neuron = Neuron(2, 0.1, 0.1)

    setSize = 10000
    dEvery = 10000

    lowLimit = -10.0
    highLimit = 10.0

    errors = 0.0
    acceptable = 0.005
    errorRate = 1.0

    plot.ion()
    xs = np.arange(-10.0, 10.5, 0.5)
    c = (0.0, 0.0, 0.0)
    while errorRate >= acceptable:
        errors = 0.0
        seed()
        for i in range(setSize):
            x = uniform(lowLimit, highLimit)
            y = uniform(lowLimit, highLimit)

            dOut = 1.0
            if x < 5.0:
                dOut = 0.0
            
            aOut = neuron.calculate([x, y])
            #print "dOut", dOut
            #print "aOut", aOut
            error = aOut * (1 - aOut) * (dOut - aOut)
            #print "error", error
            neuron.learn([x, y], error)
            bOut = 0.0
            if aOut > 0.5:
                bOut = 1.0
            
            colour = (0.0, 1.0, 0.0)
            if dOut != bOut:
                errors = errors + 1.0
                colour = (1.0, 0.0, 0.0)


            if (i + 1) % dEvery == 0:
                print i + 1, "\t", setSize, "\t", errors
                #if bOut == 0.0:
                    #plot.plot(x, y, 'o', c = colour)
                #else:
                    #plot.plot(x, y, 'x', c = colour)
                #plot.axis([-10.0, 10.0, -10.0, 10.0])
                #plot.draw()
                #print neuron.getWeights(), neuron.getBias()
        errorRate = errors / setSize
        print "Error rate", errorRate

        w = neuron.getWeights()
        slope = -w[0] / w[1]
        intercept = -neuron.getBias() / w[1]
        c = nextC(c)
        plot.plot(xs, slope * xs + intercept, '-', c = c)
        plot.axis([-10.0, 10.0, -10.0, 10.0])
        plot.draw()

    w = neuron.getWeights()
    slope = -w[0] / w[1]
    intercept = -neuron.getBias() / w[1]
    c = nextC(c)
    plot.plot(xs, slope * xs + intercept, '-', c = c, lw = 3)
    plot.axis([-10.0, 10.0, -10.0, 10.0])
    plot.show()
