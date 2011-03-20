from neuron import Neuron

from random import random, uniform, seed
import matplotlib.pyplot as plot
import numpy as np

class StripPer:
    """WARNING: THIS CLASS IS VERY VERY HARDCODED RIGHT NOW, FIX LATER"""
    """Tries to make a very simple perceptron that can detect strips on a plane"""

    #For now, do not put layers into a list, just keep them hard coded and easy
    #NOTE: Find a better way to placehold these until initialization
    #NOTE: A list will probably fix this
    bottomLeft = 0
    bottomRight = 0

    topLeft = 0
    topRight = 0

    def __init__(self):
        #print "Initializing strip perceptron"
        self.bottomLeft = Neuron(2, 0.5, 0.5)
        self.bottomRight = Neuron(2, 0.5, 0.5)
        self.topLeft = Neuron(2, 0.5, 0.5)
        self.topRight = Neuron(2, 0.5, 0.5)
        #print "Neurons initialized"
        #print

    def getLeft(self):
        return self.bottomLeft

    def getRight(self):
        return self.bottomRight

    def getTopLeft(self):
        return self.topLeft

    def getTopRight(self):
        return self.topRight

    def calculate(self, inputs):
        #print "Attempting to neurate:", inputs
        if len(inputs) != 2:
            return 0.0
        print "Stripper calculating", inputs
        bOut = [self.bottomLeft.calculate(inputs), self.bottomRight.calculate(inputs)]
        print "    Bottom result is", bOut
        r = [self.topLeft.calculate(bOut), self.topRight.calculate(bOut)]
        print "    Final result is", r
        return r

    def learn(self, inputs, dOut):
        print "Stripper learning input", inputs, "with desired", dOut
        #NOTE: Will probably have to implement the sigmoid non-linearity
        bl = self.bottomLeft
        br = self.bottomRight
        tl = self.topLeft
        tr = self.topRight

        bOut = [bl.calculate(inputs), br.calculate(inputs)]
        print "    Bottom outputs", bOut
        aOut = [tl.calculate(bOut), tr.calculate(bOut)]
        print "    Final outputs", aOut
        
        tError = [a * (1.0 - a) * (d - a) for a, d in zip(aOut, dOut)]
        print "    Top error terms", tError
        tl.learn(inputs, tError[0])
        tr.learn(inputs, tError[1])
        
        tlw = tl.getWeights()
        trw = tr.getWeights()
        
        eSum = []
        for i in range(2):
            eSum.append((tError[0] * tlw[i]) * (tError[1] * trw[i]))
        
        print "    Error term sums", eSum
        bError = [b * (1.0 - b) * s for b, s in zip(bOut, eSum)]
        print "    Bottom error terms", bError
        bl.learn(inputs, bError[0])
        br.learn(inputs, bError[1])
        
if __name__ == "__main__":

    def nextColour((r, g, b)):
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


    #Initialize our 'StripPer'
    stripper = StripPer()
    
    setSize = 10000
    dispEvery = 10000

    #for i in range(trains):
    lowLimit = -10.0
    highLimit = 10.0
    
    errors = 0.0
    acceptableError = 0.005
    unacceptableError = 1.0
    errorRate = 1.0
   
    plot.ion()
    colour = (0.0, 0.0, 0.0)
    tl = stripper.getTopLeft()
    tr = stripper.getTopRight()
    bl = stripper.getLeft()
    br = stripper.getRight()
    #while errorRate >= acceptableError:
    while True:
        errors = 0.0
        seed()
        for i in range(setSize):
            #if i % dispEvery == 0:
                #print i, "/", trains
            #print "Train step:", i
    
            x = uniform(lowLimit, highLimit)
            y = uniform(lowLimit, highLimit)
    
            dOut = [0.0, 1.0]
            if y > -5.0 and y < 5.0:
                dOut = [1.0, 0.0]
         
            #print "Inputs:", [x, y]        
            #print "Desired:", dOut
     
            stripper.learn([x, y], dOut)
            aOut = stripper.calculate([x, y])
            bOut = [0.0, 0.0]
            if aOut[0] > aOut[1]:
                bOut = [1.0, 0.0]
            else:
                bOut = [0.0, 1.0]
            if dOut != bOut:
                errors = errors + 1.0
            errorRate = errors / setSize
            if i - 1 % dispEvery == 0:
                print errorRate, "\t",dOut, "\t", bOut, "\t", aOut, "\t", x, "\t", y
                
                for n in [tl, tr, bl, br]:
                    for w in n.getWeights():
                        print w,
                    print n.getThreshold()

        leftWeights = stripper.getLeft().getWeights()
        leftSlope = -leftWeights[0] / leftWeights[1]
        leftInt = stripper.getLeft().getThreshold() / leftWeights[1]
     
        rightWeights = stripper.getRight().getWeights()
        rightSlope = -rightWeights[0] / rightWeights[1]
        rightInt = stripper.getRight().getThreshold() / rightWeights[1]
    
        xs = np.arange(-10.0, 10.5, 0.5)
        colour = nextColour(colour)
        plot.plot(xs, leftSlope * xs + leftInt, '-', c = colour)
        plot.plot(xs, rightSlope * xs + rightInt, '-', c = colour)
        plot.axis([-10, 10, -10, 10])
        plot.draw()

        if errorRate > unacceptableError:
            print "Perceptron is diverging violently, restarting the reactor"
            stripper = StripPer()
    
    #print "Training complete:"
    
    testPoints = 1000

    #print "Test points:", testPoints
    for i in range(testPoints):
        x = uniform(-10.0, 10.0)
        y = uniform(-10.0, 10.0)

        #print "    Testing:", [x, y]

        aOut = stripper.neurate([x, y])
        #print "    Actual:", aOut
        if aOut[0] > aOut[1]:
            colour = (1.0, 0.0, 0.0)
        else:
            colour = (0.0, 0.0, 1.0)
        plot.plot(x, y, 'x', c = colour)
    
    leftWeights = stripper.getLeft().getWeights()
    leftSlope = -leftWeights[0] / leftWeights[1]
    leftInt = stripper.getLeft().getThreshold() / leftWeights[1]
    
    rightWeights = stripper.getRight().getWeights()
    rightSlope = -rightWeights[0] / rightWeights[1]
    rightInt = stripper.getRight().getThreshold() / rightWeights[1]

    xs = np.arange(-10.0, 10.5, 0.5)
    plot.plot(xs, leftSlope * xs + leftInt, 'r-', lw = 3)
    plot.plot(xs, rightSlope * xs + rightInt, 'b-', lw = 3)
   
    plot.ioff()
     
    plot.axis([-10, 10, -10, 10])
    plot.show()
