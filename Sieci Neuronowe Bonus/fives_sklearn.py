import numpy as np
from sklearn.neural_network import MLPRegressor
# dane rysowanych cyferek
from keras.datasets import mnist

# siec neuronowa do rozpoznawania cyfry 5 na obrazku

# przygotowanie danych
# wczytanie danych treningowych i testowych
(train_X, train_y), (test_X, test_y) = mnist.load_data()
# dla oszczedzenia czasu zmniejsze ilosc danych z 60000 na 10000 + standardyzacja danych
train_X = train_X[:10000] / 255
train_y = train_y[:10000]
test_X = test_X[:2000] / 255
test_y = test_y[:2000]

# spłaszczenie danych
train_X = train_X.reshape((train_X.shape[0], -1))
test_X = test_X.reshape((test_X.shape[0], -1))

# zamiana wynikow na wartosci binarne (1 jak jest 5 na obrazku lub 0 jak cos innego)
train_y = np.array(list(map(lambda x: 1 if x==5 else 0,train_y)))
test_y = np.array(list(map(lambda x: 1 if x==5 else 0,test_y)))

network = MLPRegressor(hidden_layer_sizes= (4,4))
network.fit(train_X,train_y)

# predykcja
predicted_out = network.predict(test_X)

# przekształcenie predykcji wyjscia do 0 i 1
predicted_out = np.array(list(map(lambda x: 1 if x > 0.5 else 0,predicted_out)))

# funkcja do obliczenia procentowej zgodnosci predykcji
def accuracy(expected,predicted):
  return np.sum(expected == predicted) / len(expected)

# sprawdzenie dokladnosci - ile procent wynikow sie zgadza
print(f"{round(accuracy(test_y,predicted_out)*100,2)}% accuracy")