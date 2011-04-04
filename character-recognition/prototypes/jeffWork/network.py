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
        #print "Training inputs", inputs, "for desired", desired
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

        #print "Intermediate outputs", outputs
        
        error = []
        for i in range(len(self.layers) - 1, -1, -1):
            #print "  Attempting to find error for layer", i, "with numbers", self.layers[i].display()
            if i == len(self.layers) - 1:
                #print "  Calculating output error term using outputs", outputs[-1], "and desired", desired
                error.insert(0, [a * (1.0 - a) * (d - a) for a, d in zip(outputs[-1], desired)])
                #print "  Found error", error
            else:
                #print "  Calculating hidden error term"
                nW = self.layers[i + 1].getNeuronWeights()
                #print "  Neuron weights from layer", i + 1, nW
                r = []
                for j in range(self.layers[i].getSize()):
                    #print "    Finding error for", j, "neuron in layer", i
                    t = 0.0
                    for k in range(self.layers[i + 1].getSize()):
                        #print "      Error for layer", i + 1, "neuron", k, "is", error[0][k]
                        #print "      Weight for layer", i + 1, "neuron", k, "to this is", nW[k][j]
                        t = t + nW[k][j] * error[0][k]
                    #print "    Found sum is", t
                    o = outputs[i][j]
                    #print "    Output for this node is", o
                    e = o * (1 - o) * t
                    #print "    Error for this node is", e
                    r.append(e)
                error.insert(0, r)
                #print "  Found error for layer", i, "is", error[0]
        #print "Found error terms for all layers", error
        
        #print "Teaching all layers"
        for l in range(len(self.layers)):
            if l == 0:
                x = inputs
            else:
                x = outputs[l - 1]
            #print "  Teaching layer", l, "with input", x, "and error", error[l]
            #print "  Layer now has numbers", self.layers[l].display()
            self.layers[l].learn(x, error[l])
            #print "  Layer now has numbers", self.layers[l].display()
        #print

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
        network = Network(2, [2, 2], 0.1, 0.1)
    
        setSize = 10000
        dEvery = 1000
        testSize = 1000
        
        classA = []
        classB = []

        for i in range(setSize):
            x = uniform(5.0, 10.0)
            y = uniform(5.0, 10.0)
            classA.append([x, y])
         
        while len(classB) <= setSize:
            x = uniform(-10.0, 10.0)
            y = uniform(-10.0, 10.0)
            if x < 5.0 or y < 5.0:
                classB.append([x, y])
        
        print "Class a", classA[0 : 10]
        print "Class b", classB[0 : 10]

        tests = len(classA) + len(classB)
         
        errors = 0.0
        acceptable = 0.015
        errorRate = 1.0
        oldError = 1.0
        divergeFor = 3
        divergedFor = 0
        converging = True
    
        plot.ion()
        xs = np.arange(-10.0, 10.5, 0.5)
    
        while errorRate >= acceptable and divergedFor < divergeFor:
            errors = 0.0
            i = 0
            for a, b in zip(classA, classB):
                aX = a[0]
                aY = a[1]

                bX = b[0]
                bY = b[1]
    
                aDOut = [1.0, 0.0]
                bDOut = [0.0, 1.0]
    
                aAOut = network.calculate(a)
                bAOut = network.calculate(b)

                network.learn(a, aDOut)
                network.learn(b, bDOut)

                #aBOut = [0.0]
                #if aAOut[0] > 0.5:
                    #aBOut = [1.0]
             
                #bBOut = [0.0]
                #if bAOut[0] > 0.5:
                    #bBOut = [1.0]


             
                aC = (0.0, 1.0, 0.0)
                if aAOut[0] < aAOut[1]:
                    errors = errors + 1.0
                    aC = (1.0, 0.0, 0.0)
    
                bC = (0.0, 1.0, 0.0)
                if bAOut[0] > bAOut[1]:
                    errors = errors + 1.0
                    bC = (1.0, 0.0, 0.0)
    
                if (i + 2) % dEvery == 0:
                    os.system("clear")
                    print i + 2, "\t", tests, "\t", errors, "\t", errorRate, "\t", oldError, "\t", converging
                    network.display()
                    #plot.plot(aX, aY, 'o', c = aC)
                    #plot.plot(bX, bY, 'x', c = bC)
                    #plot.axis([-10.0, 10.0, -10.0, 10.0])
                    #plot.draw()
                i = i + 2
            oldError = errorRate
            errorRate = errors / tests
            converging = errorRate < oldError
            if converging:
                divergedFor = 0
            else:
                divergedFor = divergedFor + 1
            #print "Error rate", errorRate

        for i in range(testSize):
            x = uniform(-10.0, 10.0)
            y = uniform(-10.0, 10.0)

            out = network.calculate([x, y])

            c = (0.0, 1.0, 0.0)
            if out[0] > 0.5:
                c = (1.0, 0.0, 0.0)

            plot.plot(x, y, 'o', c = c)
        plot.axis([-10.0, 10.0, -10.0, 10.0])
        plot.show()
    test()
