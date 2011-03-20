class Layer:

    size = 0
    d = []          # desired outputs

    nodes = []

    def __init__(self, size):
        self.size = size

    def __initialize_nodes(self):
        # TODO: initialize nodes
        return

    def get_nodes(self):
        return self.nodes

    def set_above_layer(self, abovelayer):
        self.aboveLayer = abovelayer

    def set_below_layer(self, belowlayer):
        self.belowLayer = belowlayer

    def set_desired_outputs(self, d):
        self.d = d

    def learn(self, x):
        return

    def calculate(self, inputs):
        return