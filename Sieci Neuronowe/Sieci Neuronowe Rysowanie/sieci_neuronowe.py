from neural_network import NeuralNetwork
import numpy as np

# siec neuronowa do rozpoznawania koloru zielonego z polaczenia wartosci rgb - sam okreslalem "na oko"
train_X = [[1,2,255],[0,0,0],[0,255,0],[255,0,255],
           [60,179,113],[171,255,71],[255,99,71],[171,207,71],
           [80,239,127],[52,193,245],[143,205,143],[125,155,31],
           [253,193,245],[41,86,31],[127,193,125],[253,193,125],
           [72,121,209],[201,175,93],[138,237,43],[19,130,239],
           [115,73,134],[165,139,61],[74,191,16],[0,187,0],
           [188,103,50],[88,180,0],[44,212,20],[117,207,0],
           [165,55,91],[242,216,29],[51,182,61],[0,96,20]
           ]
train_y = [0,0,1,0,
           1,1,0,1,
           1,0,1,1,
           0,1,1,0,
           0,0,1,0,
           0,0,1,1,
           0,1,1,1,
           0,0,1,1
           ]
test_X = [[61,239,143],[177,41,38],[0,150,254],[0,207,13],
          [197,235,255],[40,107,41],[195,12,196],[51,219,82]]
test_y = [1,0,0,1,
          0,1,0,1]

# standardyzacja danych wejsciowych
train_X = np.array(train_X) / 255
test_X = np.array(test_X) / 255
train_y = np.array(train_y)
test_y = np.array(test_y)

# budowanie sieci
network = NeuralNetwork()
network.fit(train_X,train_y)

# narysowanie sieci
network.draw()

# predykcja
predicted_out = network.predict(test_X)

# funkcja do obliczenia procentowej zgodnosci predykcji
def accuracy(expected,predicted):
  # print(expected)
  # print(predicted)
  return np.sum(expected == predicted) / len(expected)

# sprawdzenie dokladnosci - ile procent wynikow sie zgadza
print(f"{round(accuracy(test_y,predicted_out)*100,2)}% accuracy without learning")