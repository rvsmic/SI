from neural_network import NeuralNetwork
import numpy as np
# dane rysowanych cyferek
from keras.datasets import mnist

# DZIAŁA ALE WYKONUJE SIĘ PIEKIELNIE DŁUGO ~ ok. 5 MIN!

# siec neuronowa do rozpoznawania cyfry 5 na obrazku

# przygotowanie danych
# wczytanie danych treningowych i testowych
(train_X, train_y), (test_X, test_y) = mnist.load_data()
# dla oszczedzenia czasu zmniejsze ilosc danych z 60000 na 1000 + standardyzacja danych
train_X = train_X[:1000] / 255
train_y = train_y[:1000]
test_X = test_X[:200] / 255
test_y = test_y[:200]

# spłaszczenie danych
train_X = train_X.reshape((train_X.shape[0], -1))
test_X = test_X.reshape((test_X.shape[0], -1))

# zamiana wynikow na wartosci binarne (1 jak jest 5 na obrazku lub 0 jak cos innego)
train_y = np.array(list(map(lambda x: 1 if x==5 else 0,train_y)))
test_y = np.array(list(map(lambda x: 1 if x==5 else 0,test_y)))

network = NeuralNetwork()
network.fit(train_X,train_y)

# predykcja
predicted_out = network.predict(test_X)

# funkcja do obliczenia procentowej zgodnosci predykcji
def accuracy(expected,predicted):
  return np.sum(expected == predicted) / len(expected)

# sprawdzenie dokladnosci - ile procent wynikow sie zgadza
print(f"{round(accuracy(test_y,predicted_out)*100,2)}% accuracy")

# test czy predykcja nie daje tylko samych 0 (bo jest ich dużo w oczekiwanych wyjsciach danych)
print(f"{len(test_y[test_y == 0]) / len(test_y)*100}% zer w tej próbce (cyfr innych niż 5)")