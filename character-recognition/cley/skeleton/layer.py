class Layer:

    aboveLayer = 0
    belowLayer = 0

    inputs = []
    nodes = []

    def __init__(self, aboveLayer, belowLayer, inputs = []):
        self.aboveLayer = abovelayer
        self.belowLayer = belowlayer
        self.inputs
        return

    def __initialize_nodes(self):
        # TODO: initialize nodes
        return

    def get_nodes(self):
        return self.nodes

    def set_above_layer(self, abovelayer):
        self.aboveLayer = abovelayer

    def set_below_layer(self, belowlayer):
        self.belowLayer = belowlayer

    def learn(self):
        return

    def calculate(self, inputs, t, j):
        return