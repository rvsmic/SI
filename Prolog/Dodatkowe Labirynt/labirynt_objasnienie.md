# Objaśnienie dotyczące rozwiązania zadania dla chętnych "Labirynt"

*Michał Rusinek*

Podpunkt 8 z polecenia był bardzo niejasno napisany, ponieważ we wcześniejszych punktach było wspomniane o wielu kluczach na terenie labiryntu (także takich które nic nie robią), a także nie było wskazania na uporządkowany rozkład kluczy. Przez to standardowa reguła szukaj_wyjscia jest bardzo nielogiczna, ponieważ może ona przenosić jedynie jeden klucz ze sobą.

Gdyby argumentem tej reguły była lista kluczy to można by było to rozwiązać we wskazany sposób, po prostu dopisując napotkane klucze do listy, a potem jedynie sprawdzając czy posiadamy dany klucz.

Jedynym rozwiązaniem, w którym taka funkcja mogłaby działać, byłoby przechodzenie labiryntu, ignorując wszystkie napotkane klucze po drodze, a w momencie napotkania zamknietych drzwi, zacząć się cofać w poszukiwaniu pasującego klucza. Nie rozważałem takiego rozwiązania, ponieważ w przypadku długiego labiryntu byłoby ono potwornie wolne.

Z tego powodu stworzyłem rozwiązanie, które zachowuje składnię wskazanej w poleceniu 8 reguły szukaj_wyjscia, ale przechodzi przez labirynt w inny sposób niż w jest założone w poleceniu (przynajmniej tak mi się wydaje, ponieważ nie używa wszystkich argumentów funkcji).

## Moje rozwiązanie

Aby zapytanie szukaj_wyjscia stworzyło trasę przez labirynt, powinno ono zostać wywołane w następujący sposób:
**szukaj_wyjscia( pokoj_startowy , \_ , \_ , pokoj_docelowy )**

Reguła szukaj_wyjscia i jej argumenty:

* POKOJ_POCZATKOWY - na wejściu pokój startowy, a przy wywoływaniu rekurencji aktualny (następny) pokój
* POKOJ_Z_KLUCZEM - poprzedni pokój
* KLUCZ - argument nieużyty
* POKOJ_Z_WYJSCIEM - docelowy pokój

Testując działanie algorytmu korzystałem ze stworzonego przeze mnie labiryntu zobrazowanego w *labirynt.pdf* (ponieważ na stronie przedmiotu nie znalazłem przykładu). Rozkład kluczy w pomieszczeniach wymaga rozpoczęcia w niższej literze alfabetu od pokoju wyjściowego (trasa od a do z jest najtrudniejsza) - zamkniete drzwi wyjściowe oznaczają, że z perspektywy startowego pokoju drzwi wyjściowe z danego pokoju, w którym jesteśmy są zamknięte.

## Alternatywne rozwiązanie

Po wykonaniu pierwszej wersji programu wpadłem na inny pomysł interpretacji zadania - "drzwi wyjściowe" oznaczają jedynie wyjścia z labiryntu, ale nie są drzwiami wewnętrzymi w labiryncie. W momencie znalezienia klucza powiązanego z określonym pokojem, staje się on naszym celem, a dotarcie do niego kończy działanie programu i zwraca informacje o pokoju z kluczem, kluczu i znalezionym wyjściu.

Stworzyłem alternatywną wersję programu działającą w następujący sposób:
**szukaj_wyjscia( pokoj_startowy , POKOJ_Z_KLUCZEM, KLUCZ , POKOJ DOCELOWY)**

Takie wywołanie reguły szukaj_wyjscia sprawi, że program stworzy trasę potrzebną do znalezienia klucza do wyjścia oraz trasę do samych drzwi wyjściowych, a także zmienne pisane drukowanymi literami zwrócą odpowiednie wartości.

Graficzna reprezentacja bazy danych do tej wersji rozwiązania znajduje się w pliku *Labirynt alt.pdf*
