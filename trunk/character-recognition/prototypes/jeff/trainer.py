from network import Network

def getSet(filename):
    f = open(filename)

    result = []
    for l in f:
        splut = l.split(",")
        splut = [int(s) for s in splut]
        result.append((splut[0 : 64], splut[64]))

    f.close()
    del f
    return result

train = getSet("datasets/optdigits.tra")

network = Network(64, [40, 40, 10], 0.1, 0.1)

errors = 0.0
acceptable = 0.01
errorRate = 1.0
oldError = 1.0
divergeFor = 3
divergedFor = 0
converging = True

countEvery = 100

print "Data set is of size", len(train)

while errorRate >= acceptable and divergedFor < divergeFor:
    errors = 0.0
    desired = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    j = 0
    for data in train:
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
            errors = errors + 1.0
    oldError = errorRate
    errorRate = errors / tests
    converging = errorRate < oldError
    if converging:
        divergedFor = 0
    else:
        divergedFor = divergedFor + 1
    print errorRate, "\t", oldError, "\t", converging


