# Generic training data object

__author__="cley"
__date__ ="$29-Mar-2011 1:20:48 PM$"

class TrainingData:

    x = [] #inputs
    d = [] #desired outputs

    def __init__(self):
        """Construct Training Data"""

    def get_data(self):
        return [self.x, self.d]

    def add_dataset(self, x, d):
        self.x.append(x)
        self.d.append(d)
