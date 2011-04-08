from layer import Layer

from random import random, uniform, seed

import matplotlib.pyplot as plot
import numpy as np

import os

class Network:
    """Test of a simple general neural network"""

    def __init__(self, numInputs, layerSizes, gain, momentum):
        self.numInputs = numInputs
        self.layers = []
        first = True
        lastS = 0
        for s in layerSizes:
            if first:
                #print "Layer(numInputs", numInputs, "size", s, "gain", gain, "momentum", momentum, ")"
                self.layers.append(Layer(numInputs, s, gain, momentum))
                first = False
            else:
                #print "Layer(numInputs", lastS, "size", s, "gain", gain, "momentum", momentum, ")"
                self.layers.append(Layer(lastS, s, gain, momentum))
            lastS = s

    def learn(self, inputs, desired):
        if len(inputs) != self.numInputs:
            print "Number of inputs does not match network"
            return 
        if len(desired) != self.layers[-1].getSize():
            print "Number of outputs does not match network"
            return
        outputs = []
        first = True
        for l in self.layers:
            x = []
            if first:
                x = inputs
                first = False
            else:
                x = outputs[-1]
            outputs.append(l.calculate(x))
        
        error = []
        for i in range(len(self.layers) - 1, -1, -1):
            if i == len(self.layers) - 1:
                error.insert(0, [a * (1.0 - a) * (d - a) for a, d in zip(outputs[-1], desired)])
            else:
                nW = self.layers[i + 1].getNeuronWeights()
                r = []
                for j in range(self.layers[i].getSize()):
                    t = 0.0
                    for k in range(self.layers[i + 1].getSize()):
                        t = t + nW[k][j] * error[0][k]
                    r.append(outputs[i][j] * (1 - outputs[i][j]) * t)
                error.insert(0, r)
        
        for l in range(len(self.layers)):
            if l == 0:
                x = inputs
            else:
                x = outputs[l - 1]
            self.layers[l].learn(x, error[l])

    # calculate the final output based on an initial input set
    def calculate(self, inputs):
        #print "Attempting to calculate", inputs
        if len(inputs) != self.numInputs:
            print "Number of inputs does not match network"
            return
        output = []
        first = True
        for l in self.layers:
            if first:
                output = l.calculate(inputs)
                #print "  First result output", output
                first = False
            else:
                output = l.calculate(output)
                #print "  Intermediate result output", output
        #print "Result is", output
        #print
        return output

    def display(self):
        for l in reversed(self.layers):
            for n in l.getNeurons():
                print n.getWeights(), n.getBias(), "\t",
            print
        print

if __name__ == "__main__":
    def test():
        network = Network(2, [4, 4], 0.1, 0.1)
    
        setSize = 1000
        dEvery = 100000
        testSize = 1000
        
        classA = []
        classB = []
        classC = []
        classD = []

        while len(classA) < setSize:
            x = uniform(-10.0, 0.0)
            y = uniform(0.0, 10.0)
            if -x < y:
                classA.append([x,y])
         
        #for x, y in classA:
            #plot.plot(x, y, 'ro')

        while len(classB) < setSize:
            x = uniform(-10.0, 0.0)
            y = uniform(-10.0, 10.0)
            if -x >= y:
                classB.append([x, y])
         
        #for x, y in classB:
            #plot.plot(x, y, 'go')

        while len(classC) < setSize:
            x = uniform(0.0, 10.0)
            y = uniform(0.0, 10.0)
            if x < (3.0*y/10.0):
                classC.append([x, y])
         
        #for x, y in classC:
            #plot.plot(x, y, 'bo')

        while len(classD) < setSize:
            x = uniform(0.0, 10.0)
            y = uniform(-10.0, 10.0)
            if x >= (3.0*y/10.0):
                classD.append([x, y])

        #for x, y in classD:
            #plot.plot(x, y, 'yo')
        #plot.axis([-10.0, 10.0, -10.0, 10.0])
        #plot.show()
         
        tests = 4 * setSize
         
        errors = 0.0
        acceptable = 0.01
        errorRate = 1.0
        oldError = 1.0
        divergeFor = 3
        divergedFor = 0
        converging = True
    
        plot.ion()
        xs = np.arange(-10.0, 10.5, 0.5)

        classes = [classA, classB, classC, classD]
        aDOut = [1.0, 0.0, 0.0, 0.0]
        bDOut = [0.0, 1.0, 0.0, 0.0]
        cDOut = [0.0, 0.0, 1.0, 0.0]
        dDOut = [0.0, 0.0, 0.0, 1.0]
        desired = [aDOut, bDOut, cDOut, dDOut]
    
        while errorRate >= acceptable and divergedFor < divergeFor:
            errors = 0.0
            #i = 0
            for a, b, c, d in zip(classA, classB, classC, classD):
                actuals = []
                binary = []
                actuals.append(network.calculate(a))
                actuals.append(network.calculate(b))
                actuals.append(network.calculate(c))
                actuals.append(network.calculate(d))

                network.learn(a, desired[0])
                network.learn(b, desired[1])
                network.learn(c, desired[2])
                network.learn(d, desired[3])
                
                for actual in actuals:
                    result = [0.0, 0.0, 0.0, 0.0]
                    mi = 0
                    m = 0.0
                    for i in range(len(actual)):
                        if actual[i] > m:
                            m = actual[i]
                            mi = i
                    result[mi] = 1.0
                    binary.append(result)

                #print "Actual", actuals
                #print "Binary", binary

                #aBOut = [0.0]
                #if aAOut[0] > 0.5:
                    #aBOut = [1.0]
             
                #bBOut = [0.0]
                #if bAOut[0] > 0.5:
                    #bBOut = [1.0]
   
                for d, b in zip(desired, binary):
                    if d != b:
                        errors = errors + 1.0
    
                #if (i + len(actual)) % dEvery == 0:
                    #os.system("clear")
                    #print i + 2, "\t", tests, "\t", errors, "\t", errorRate, "\t", oldError, "\t", converging
                    #network.display()
                #i = i + len(actual)
            oldError = errorRate
            errorRate = errors / tests
            converging = errorRate < oldError
            if converging:
                divergedFor = 0
            else:
                divergedFor = divergedFor + 1
            print errorRate, "\t", oldError, "\t", converging
            #print "Error rate", errorRate

        for i in range(testSize):
            x = uniform(-10.0, 10.0)
            y = uniform(-10.0, 10.0)

            out = network.calculate([x, y])
            m = 0.0
            mi = 0
            for r in range(len(out)):
                if out[r] > m:
                    m = out[r]
                    mi = r

            c = (0.0, 0.0, 0.0)
            if mi == 0:
                c = (1.0, 0.0, 0.0)
            if mi == 1:
                c = (0.0, 1.0, 0.0)
            if mi == 2:
                c = (0.0, 0.0, 1.0)
            if mi == 3:
                c = (1.0, 0.6, 0.0)

            plot.plot(x, y, 'o', c = c)
        plot.axis([-10.0, 10.0, -10.0, 10.0])
        plot.show()
    test()
