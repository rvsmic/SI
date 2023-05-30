import numpy as np
from neuron import Neuron
# do rysowania sieci neuronowej
import matplotlib.pyplot as plt
import networkx as nx

# multilayer perceptron - mozna podac dowolne wymiary ukrytych warstw!
class NeuralNetwork:
  def __init__(self,hidden_layer_sizes=(4,4)):
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

  # predykcja wyjscia z danego wejscia
  def _binary_result(self,x):
    return 0 if x < 0.5 else 1
  def predict(self,test_in):
    out = self._forward_pass(test_in)
    return np.array(list(map(self._binary_result,np.array(out[-1]).flatten())))
  
  def draw(self):
    # wlasciwosci do grafu
    node_size = 3000
    edge_color = 'black'
    colors = ('#ff5c33','#66d9ff','#00cc66')

    # poczatek grafu
    graph = nx.DiGraph()

    # rozmiary warstw
    self.layer_sizes  = []
    self.layer_sizes.append(len(self.neurons[0]))
    for i in range(len(self.hidden_layer_sizes)):
      self.layer_sizes.append(self.hidden_layer_sizes[i])
    self.layer_sizes.append(1)
    

    # start od srodka najwiekszej warstwy do ladnego rysowania
    max_middle_idx = (max(self.layer_sizes) - 1) / 2

    # nodey - rysowane symetrycznie, dlatego tak skomplikowane
    for layer_idx in range(len(self.neurons)):
      layer_size = len(self.neurons[layer_idx])
      neuron_counter = 0
      # warstwa nieparzysta
      if self.layer_sizes[layer_idx] & 1:
        # nad srodkiem
        for i in range(1,layer_size // 2 + 1):
          graph.add_node(f"L{layer_idx} N{layer_size // 2 - neuron_counter - 1}", label=f"L{layer_idx} N{layer_size // 2 - neuron_counter - 1} \nb={round(self.neurons[layer_idx][neuron_counter].b,2)}",
                         pos=(layer_idx,-(max_middle_idx - i)), node_color=colors[0 if layer_idx == 0 else 2 if layer_idx == len(self.layer_sizes)-1 else 1]
          )
          neuron_counter += 1
        # srodek
        graph.add_node(f"L{layer_idx} N{neuron_counter}", label=f"L{layer_idx} N{neuron_counter} \nb={round(self.neurons[layer_idx][neuron_counter].b,2)}",
                       pos=(layer_idx,-(max_middle_idx)), node_color=colors[0 if layer_idx == 0 else 2 if layer_idx == len(self.layer_sizes)-1 else 1]
        )
        neuron_counter += 1
        # pod srodkiem
        for i in range(1,layer_size // 2 + 1):
          graph.add_node(f"L{layer_idx} N{neuron_counter}", label=f"L{layer_idx} N{neuron_counter} \nb={round(self.neurons[layer_idx][neuron_counter].b,2)}",
                         pos=(layer_idx,-(max_middle_idx + i)), node_color=colors[0 if layer_idx == 0 else 2 if layer_idx == len(self.layer_sizes)-1 else 1]
          )
          neuron_counter += 1

        # warstwa parzysta
      else:
        # nad srodkiem
        for i in range(1,layer_size // 2 + 1):
          graph.add_node(f"L{layer_idx} N{layer_size // 2 - neuron_counter - 1}", label=f"L{layer_idx} N{layer_size // 2 - neuron_counter - 1} \nb={round(self.neurons[layer_idx][neuron_counter].b,2)}",
                         pos=(layer_idx,-(max_middle_idx - i + 0.5)), node_color=colors[0 if layer_idx == 0 else 2 if layer_idx == len(self.layer_sizes)-1 else 1]
          )
          neuron_counter += 1
        # pod srodkiem
        for i in range(1,layer_size // 2 + 1):
          graph.add_node(f"L{layer_idx} N{neuron_counter}", label=f"L{layer_idx} N{neuron_counter} \nb={round(self.neurons[layer_idx][neuron_counter].b,2)}",
                         pos=(layer_idx,-(max_middle_idx + i - 0.5)), node_color=colors[0 if layer_idx == 0 else 2 if layer_idx == len(self.layer_sizes)-1 else 1]
          )
          neuron_counter += 1
    
    # krawedzie
    for layer_idx in range(1,len(self.layer_sizes)):
      for neuron_idx in range(self.layer_sizes[layer_idx]):
        for prev_layer_neuron_idx in range(self.layer_sizes[layer_idx-1]):
          graph.add_edge(f"L{layer_idx-1} N{prev_layer_neuron_idx}", f"L{layer_idx} N{neuron_idx}",
                         weight=round(self.neurons[layer_idx][neuron_idx].ws[prev_layer_neuron_idx],2))
        
    # narysowanie grafu
    pos = nx.get_node_attributes(graph,'pos')
    labels = nx.get_node_attributes(graph,'label')
    colors = list(nx.get_node_attributes(graph,'node_color').values())
    weights = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph,pos,node_size=node_size,node_color=colors,edge_color=edge_color,with_labels=True,labels=labels)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=weights)

    plt.title("Sieć neuronowa")
    plt.axis('off')
    plt.show()