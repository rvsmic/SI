import numpy as np
from collections import Counter

# pojedynczy node drzewa
class Node:
  def __init__(self, feature=None, threshold=None, left=None, right=None,*, value=None):
    # indeks cechy
    self.feature = feature
    # prog podzialu dla tej cechy
    self.threshold = threshold
    # lewy i prawy syn (prawda i falsz)
    self.left = left
    self.right = right
    # etykieta jezeli jest lisciem
    self.value = value

  # czy jest lisciem
  def is_leaf_node(self):
    return self.value is not None

# drzewo decyzyjne klasyfikacyjne
class DecisionTree:
  def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
    # minimum elementow do podzialu
    self.min_samples_split=min_samples_split
    # max glebokosc drzewa
    self.max_depth=max_depth
    # ilosc cech wybieranych przy podziale
    self.n_features=n_features
    # korzen
    self.root=None

# funkcja tworzaca drzewo z wartosci X i etykiet y
  def fit(self, X, y):
    # ilosc cech to dlugosc wierszy tablicy danych jezeli nie jest podana (jako argument drzewa) lub minimum tych 2 wartosci
    self.n_features = X.shape[1] if not self.n_features else min(self.n_features, X.shape[1])
    # stworzenie drzewa
    self.root = self._grow_tree(X, y)

# funkcja rekurencyjnie tworzaca drzewo
  def _grow_tree(self, X, y, depth=0):
    # ilosc probek i cech w nich
    sample_count, feature_count = X.shape
    # ilosc roznych etykiet w tej chwili
    label_count = len(np.unique(y))

    # kryterium stopu - max glebokosc osiagnieta / za malo probek / zostala tylko jedna etykieta
    if depth >= self.max_depth or sample_count < self.min_samples_split or label_count == 1:
      counter = Counter(y)
      # najczesciej wystepujaca wartosc w etykietach dla tego liscia
      most_common_value = counter.most_common(1)[0][0]
      return Node(value=most_common_value)
    
    # indeksy dla cech w losowej kolejnosci
    features_indexes = np.random.choice(feature_count, self.n_features, replace=False)

    # wybranie najlepszych cech i progu podzialu oraz podzielenie w ten sposob
    best_features_column, best_threshold = self._best_split(X,y,features_indexes)
    left_indexes, right_indexes = self._split(X[:,best_features_column],best_threshold)

    # dalsze rekurencyjne tworzenie drzewa
    left = self._grow_tree(X[left_indexes,:], y[left_indexes], depth+1)
    right = self._grow_tree(X[right_indexes,:], y[right_indexes], depth+1)

    # zwrocenie nodea ktory nie jest lisciem
    return Node(best_features_column, best_threshold, left, right)

# funkcja szukajaca najlepszego podzialu dla danych
  def _best_split(self, X, y, feat_idxs):
    best_gain = -1
    split_index, split_threshold = None, None
    # przechodzimy po indeksach cech
    for i in feat_idxs:
      # bierzemy kolumne danej cechy i unikalne wartosci z niej
      values = X[:,i]
      thresholds = np.unique(values)
      # szukamy sprawdzamy "srodki" miedzy kazdymi progami
      for j in range(1,len(thresholds)):
        middle_threshold = (thresholds[j] + thresholds[j-1]) / 2
        info_gain = self._information_gain(y,values,middle_threshold)
        # wybieramy najlepsze
        if info_gain > best_gain:
          best_gain = info_gain
          split_index = i
          split_threshold = middle_threshold

    return split_index, split_threshold


# funkcja liczaca information gain
  def _information_gain(self, y, X_column, threshold):
    #𝐼𝐺=𝐸(𝑝𝑎𝑟𝑒𝑛𝑡)−[𝑤𝑒𝑖𝑔ℎ𝑡𝑒𝑑_𝑎𝑣𝑒𝑟𝑎𝑔𝑒]∗𝐸(𝑐ℎ𝑖𝑙𝑑𝑟𝑒𝑛)
    parent_entropy = self._entropy(y)

    # podzial na lewe i prawe wartosci wzgledem progu
    left_indexes, right_indexes = self._split(X_column, threshold)

    # jezeli podzial jest czysty
    if len(left_indexes) == 0 or len(right_indexes) == 0:
      return 0
    
    # obliczenie wg wzoru
    count = len(y)
    left_count, right_count = len(left_indexes), len(right_indexes)
    left_entropy, right_entropy = self._entropy(y[left_indexes]), self._entropy(y[right_indexes])
    children_entropy = (left_count/count) * left_entropy + (right_count/count) * right_entropy

    return parent_entropy - children_entropy

# funkcja dokonujaca podzialu kolumny wzgledem progu
  def _split(self, X_column, split_thresh):
    left_indexes = np.argwhere(X_column <= split_thresh).flatten()
    right_indexes = np.argwhere(X_column > split_thresh).flatten()
    return left_indexes, right_indexes

# funkcja liczaca entropie
  def _entropy(self, y):
    hist = np.bincount(y)
    ps = hist / len(y)
    return -np.sum([p * np.log(p) for p in ps if p>0])

# funkcja przechodzaca po stworzonym drzewie
  def _traverse_tree(self, x, node):
    if node.is_leaf_node():
      return node.value
    
    if x[node.feature] <= node.threshold:
      return self._traverse_tree(x,node.left)
    else:
      return self._traverse_tree(x,node.right)

# funkcja dokonujaca predykcji na stworzonym drzewie
  def predict(self, X):
    return np.array([self._traverse_tree(x, self.root) for x in X])