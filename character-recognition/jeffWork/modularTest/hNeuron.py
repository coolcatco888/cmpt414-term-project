class HNeuron:
    """Hidden neuron"""
    
    """Output register"""
    output = 0.0

    """The num weights that correspond to inputs for calculate"""
    weights = []
    
    """Connection tuples for neurons above(Neuron, weight)(Must keep these synchronized somehow)"""
    above = []
    
    """Connection tuples for neurons below(Neuron, weight)"""
    below = []

    """Initializes a neuron with the given nonlinearity and stats that can only accept numInputs inputs"""
    def __init__(self, function, stats):

    """Calculates the output of from the neurons and weights in below and stores it in the output register"""
    """A neuron with an output of None is not "ready yet", at this point you recursively ask it for output"""
    def calculate(self):

    def getOutput(self):
        return output
   
    """This neuron learns based on neurons above and below it"""
    """Try and ensure that weight changes try and synchronize with the neurons on the other side of connections"""
    def learn(self):
        
    """Attempts to ensure that neuron becomes connected above to self, and self becomes connected below to neuron"""
    """Also attempts to ensure that the connecting weights are the same"""
    def connectAbove(self, neuron):

    """Like above for below"""
    def connectBelow(self, neuron):
