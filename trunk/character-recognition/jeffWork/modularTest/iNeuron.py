class INeuron:
    """Input neuron"""
    
    """Number of inputs"""
    num = []
   
    """Output register"""
    """Don't like this, I'll probably try and design this away later"""
    output = 0.0

    """The num weights that correspond to inputs for calculate"""
    weights = []
    
    """Connection tuples (Neuron, weight)(Must keep these synchronized somehow)"""
    above = []

    """Initializes a neuron with the given nonlinearity and stats that can only accept numInputs inputs"""
    def __init__(self, numInputs, function, stats):

    """Calculates the output of inputs from this neuron and stores it in the output register"""
    def calculate(self, inputs):

    def getOutput(self):
        return output
   
    """This neuron learns based on inp""" 
    def learn(self, inp):
        
    """Attempts to ensure that neuron becomes connected above to self, and self becomes connected below to neuron"""
    """Also attempts to ensure that the connecting weights are the same"""
    def connectAbove(self, neuron):
