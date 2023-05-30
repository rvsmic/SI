import numpy as np
from neuron import Neuron

# multilayer perceptron - mozna podac dowolne wymiary ukrytych warstw!
class NeuralNetwork:
  def __init__(self,hidden_layer_sizes=(4,4),learning_rate=0.1,iteration_count=10000):
    self.learning_rate = learning_rate
    self.iteration_count = iteration_count
    self.neurons = []
    self.hidden_layer_sizes = hidden_layer_sizes

  # dopasowanie sieci do danych + nauczenie jej na treningowym wyjsciu
  def fit(self,train_in,train_out):
    train_in = np.array(train_in)
    train_out = np.array(train_out)
    input_size = len(train_in[0])
    # input layer zalezny od wielkosci wejscia - potrzebny do rysowania tylko
    input_layer = [Neuron(1,bias=0,weights=1) for _ in range(input_size)]
    self.neurons.append(input_layer)
    # pierwszy hidden layer
    bias = 2*np.random.random() - 1
    h1_layer = [Neuron(input_size,bias=bias) for _ in range(self.hidden_layer_sizes[0])]
    self.neurons.append(h1_layer)
    # reszta hidden layers
    for l_idx in range(len(self.hidden_layer_sizes[1:])):
      bias = 2*np.random.random() - 1
      h_layer = [Neuron(self.hidden_layer_sizes[l_idx-1],bias=bias) for _ in range(self.hidden_layer_sizes[l_idx])]
      self.neurons.append(h_layer)
    # output layer
    bias = 2*np.random.random() - 1
    out_layer = [Neuron(self.hidden_layer_sizes[-1],bias=bias) for _ in range(1)]
    self.neurons.append(out_layer)
    
    # dostrajanie wag i biasow sieci
    for i in range(self.iteration_count):
      outputs = self._forward_pass(train_in)
      self._backprogation(train_out,outputs)

  def _forward_pass(self,train_in):
    # wyjscie z input layer
    next_in = train_in
    # wyjscie z hidden layer 1
    h1_out = []
    outputs = [next_in]
    # iteracja po pozostalych warstwach i obliczanie wyjsc
    for neurons_layer in self.neurons[1:]:
      layer_set = []
      for set in next_in:
        layer = []
        for neuron in neurons_layer:
          layer.append(neuron(set))
        layer_set.append(layer)
      outputs.append(layer_set)
      next_in = layer_set
    return outputs

  # propagacja wsteczna - aktualizacja wag i biasow na podstawie bledow wzgledem wyjscia
  def _backprogation(self,train_out,outputs):
    # wyciagniecie wag do wektorow
    layers_ws = []
    for layer in self.neurons[1:]:
      layers_ws.append(np.array([n.ws for n in layer]).T)
    errors = []
    # error dla output layer
    out_err = np.reshape(np.array(outputs[-1]).T - train_out,(-1,1))
    errors.append(out_err)
    # errory dla hidden layers
    for layer_idx in range(len(self.hidden_layer_sizes)-1,-1,-1):
      err = self._sigmoid_derivative(np.array(outputs[layer_idx+1])) * np.dot(errors[-1], np.array(layers_ws[layer_idx+1]).T)
      errors.append(err)
    errors = errors[::-1]
    
    # pochodne czastkowe
    pd = []
    for layer_idx in range(1,len(self.neurons)):
      layer_pd = np.array(outputs[layer_idx-1])[:,:,np.newaxis] * errors[layer_idx-1][:,np.newaxis,:]
      pd.append(layer_pd)

    # srednia dla gradientu dla warstw
    total_gradients = []
    for layer_idx in range(1,len(self.neurons)):
      total_layer_gradient = np.average(pd[layer_idx-1], axis=0)
      total_gradients.append(total_layer_gradient)
    # aktualizacja wektora wag
    for layer_idx in range(1,len(self.neurons)):
      layers_ws[layer_idx-1] += - self.learning_rate * total_gradients[layer_idx-1]
    # wyciagniecie biasow z neuronow
    layers_b = []
    for layer in self.neurons[1:]:
      layers_b.append(layer[0].b)
    for layer_idx in range(len(self.neurons[1:])):
      layers_b[layer_idx] += - self.learning_rate * np.average(np.sum(errors[layer_idx],axis=0))
    # aktualizacja wag i biasow w neuronach
    for layer_idx in range(1,len(self.neurons)):
      for neuron_idx in range(len(self.neurons[layer_idx])):
        self.neurons[layer_idx][neuron_idx].ws = layers_ws[layer_idx-1].T[neuron_idx]
        self.neurons[layer_idx][neuron_idx].b = layers_b[layer_idx-1]

  # pochodna sigmoida
  def _sigmoid_derivative(self,x):
    return x * (1 - x)

  # predykcja wyjscia z danego wejscia
  def _binary_result(self,x):
    return 0 if x < 0.5 else 1
  def predict(self,test_in):
    out = self._forward_pass(test_in)
    return np.array(list(map(self._binary_result,np.array(out[-1]).flatten())))