# Sztuczna Inteligencja

## 1. Czateria

**[Czateria](czateria_updated.md "Czateria")** - pierwsza wersja rozwiązania została oddana w terminie jako "czateria.txt". Po zajęciach 1.06 i Pana sugestii, zrobiłem parę poprawek i ostateczną wersję przerobiłem na markdown do lepszego czytania

## 2. Prolog

**[Prolog](Prolog "Prolog")** - poszczególne ćwiczenia są podzielone na foldery z rozwiązaniami w .txt i .pl oraz plikiem z poleceniem.
Do zadań niektórych zadań dołączyłem pliki pdf obrazujące rozkład bazy wiedzy (drzewo genealogiczne w zad 2 i różne labirynty w zadaniu dodatkowym). W folderze z zadaniem dodatkowym z labiryntu jest również plik labirynt_objasnienie.md w którym opisany jest mój dylemat i powód stworzenia dwóch rozwiązań do tego problemu...

## 3. Drzewa Decyzyjne

**[Drzewa Decyzyjne](Drzewa%20Decyzyjne "Drzewa Decyzyjne")** - w folderze znajdują się trzy pliki:
  - decision_tree.py - uzupełniony szkielet z treści zadania o ciała określonych funkcji.
  - drzewa_decyzyjne.py - dostarczony plik implementujący klasę drzewa decyzyjnego i sprawdzający jego accuracy.
  - test&#46;py - plik stworzony z implementacją sklearn.tree - służył do testowania dokładności predykcji mojego drzewa i drzewa sklearn na bazie różnych seedów.

## 4. Sztuczne Sieci Neuronowe

**[Sztuczne Sieci Neuronowe](Sieci%20Neuronowe "Sieci Neuronowe")** - poszczególne ćwiczenia są podzielone na foldery z 3 plikami:
  - neuron&#46;py - plik wymagany w poleceniu zadania
  - neural_network.py - obiektowa implementacja sieci neuronowej z uruchomieniem i wyświetlaniem (Sieci Neuronowe Rysowanie) lub w pełni funkcjonalna z backtrackingiem i nauką (Sieci Neuronowe Backtracking)
  - sieci_neuronowe.py - plik do uruchamiania całej sieci, operujący dwoma powyższymi - w nim jest użyta klasa Neural Network, a także są w nim zamieszczone dane do zadania.

Dane do nauki sieci stworzyłem sam - są to tablice trójek wartości RGB. Sieć ma za zadanie określić z tych trzech wartości czy jest to kolor zielony (różne odcienie i nasycenia oznaczane wg. mojego oka).

*Klasa neural_network.py jest kompatybilna między folderami - np. do backtrackingu można również przerzucić metodę do rysowania sieci z pierwszego zadania jeżeli jest potrzebna.*

## 5. Algorytmy Genetyczne
**[Algorytmy Genetyczne](Algorytmy%20Genetyczne "Algorytmy Genetyczne")** - w folderze znajduje się plik algorytmy_genetyczne.py w którym jest uzupełniony szkielet programu z zadania.
