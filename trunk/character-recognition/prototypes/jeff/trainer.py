from network import Network

def getSet(filename):
    f = open(filename)

    result = []
    for l in f:
        splut = l.split(",")
        splut = [float(s) for s in splut]
        result.append(([s / 16.0 for s in splut[0 : 64]], int(splut[64])))

    f.close()
    del f
    return result

train = getSet("datasets/optdigits.tra")

dataSet = train[0 : 500]

del train

network = Network(64, [30, 20, 10], 0.1, 0.1)

errors = 0.0
acceptable = 0.01
errorRate = 1.0
oldError = 1.0
divergeFor = 3
divergedFor = 0
converging = True

countEvery = 100

tests = len(dataSet)

print "Data set is of size", tests

while errorRate >= acceptable and divergedFor < divergeFor:
    errors = 0.0
    j = 0
    for data in dataSet:
        desired = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        if j % countEvery == 0:
            print j
        j = j + 1
        inputs = data[0]
        desired[data[1]] = 1.0
        #print "Training with inputs", inputs, "and desired", desired
        actual = network.calculate(inputs)
        network.learn(inputs, desired)
        binary = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        mi = 0
        m = 0.0
        for i in range(len(actual)):
            if actual[i] > m:
                m = actual[i]
                mi = i
        binary[mi] = 1.0
        #print "Result was actually", actual, "and binarily", binary
        if desired != binary:
            print "Training with inputs", inputs, "and desired", desired
            print "Result was actually", actual, "and binarily", binary
            print "Error: desired", desired, "is not binary", binary
            errors = errors + 1.0
    oldError = errorRate
    print "Old error", oldError
    errorRate = errors / float(tests)
    print "Errors", errors, "set size", tests, "error rate", errorRate
    converging = errorRate < oldError
    if converging:
        divergedFor = 0
    else:
        divergedFor = divergedFor + 1
    print errorRate, "\t", oldError, "\t", converging


