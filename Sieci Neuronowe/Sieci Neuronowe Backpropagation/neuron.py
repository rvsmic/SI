import numpy as np 

class Neuron:  
  def __init__(self, n_inputs, bias = 0., weights = None):  
    self.b = bias
    if weights: self.ws = np.array(weights)
    else: self.ws = 2 * np.random.random(n_inputs) - 1

# sigmoid
  def _f(self,x):
    return 1 / (1 + np.exp(-x))

# calculate the neuron's output: multiply the inputs with the weights and sum the values together, add the bias value,
# then transform the value via an activation function
  def __call__(self, xs):
    return self._f(xs @ self.ws + self.b)