"""Simple NN implementation just for learning purposes,"""

import random


class Neuron:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v


class NeuronNetwork:
    def __init__(self, input_layer, hidden_layers, output_layer,
                 min_weight=0, max_weight=10):
        self._min_weight = min_weight
        self._max_weight = max_weight
        self._layers = [input_layer]
        for layer in hidden_layers:
            self._layers.append(layer)
        self._layers.append(output_layer)
        self._weights = None
        self.initialize_weights()

    def feed_forward(self, x, y):
        assert len(x) == len(self._layers[0])
        assert len(y) == len(self._layers[-1])

        for i, v in enumerate(x):
            self._layers[0][i].value = v

        for i in range(1, len(self._layers)):
            for n2 in self._layers[i]:
                n2.value = 0
                for n1 in self._layers[i - 1]:
                    n2.value += n1.value * self._weights[id(n2), id(n1)]

        error = []
        f



    def backward_propagation(self):
        pass

    def initialize_weights(self):
        self._weights = {}
        for i in range(len(self._layers) - 1):
            l1 = self._layers[i]
            l2 = self._layers[i + 1]
            for n1 in l1:
                for n2 in l2:
                    self._weights[id(n2), id(n1)] = random.uniform(
                        self._min_weight, self._max_weight
                    )


if __name__ == '__main__':

    nn = NeuronNetwork([Neuron()], [], [Neuron()])
    nn.feed_forward([12], [6])

