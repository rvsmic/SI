% modyfikacja aby procedura retract i assert dzialala
% zeby przejsc przez drzwi bez zapetlenia, podniesc klucz (nosimy go ze soba wiec
% drzwi nim zamkniete staja sie otwarte) oraz podnosic klucze jeden raz - sa usuwane fakty
% (lub przywracane przy nawrotach)
:- dynamic drzwi/2.
:- dynamic otwiera/2.
:- dynamic klucz/2.

% drzwi miedzy pokojami X i Y
drzwi(a,b).
drzwi(b,c).
drzwi(c,d).
drzwi(c,e).
drzwi(e,h).
drzwi(f,g).
drzwi(g,h).
drzwi(h,i).
drzwi(i,j).
drzwi(j,k).
drzwi(k,l).
drzwi(l,m).
drzwi(o,n).
drzwi(n,m).
drzwi(k,p).
drzwi(s,r).
drzwi(r,q).
drzwi(q,p).
drzwi(r,t).
drzwi(t,u).
drzwi(u,w).
drzwi(w,x).
drzwi(x,z).
drzwi(o,y).

% pokoj X w ktorym znajduje sie klucz Y
klucz(a,kluczB).
klucz(b,kluczFrancuski).
klucz(d,kluczE).
klucz(f,kluczI).
klucz(i,kluczJ).
klucz(j,kluczQ).
klucz(n,kluczT).
klucz(o,kluczPlaski).
klucz(q,kluczDoKol).
klucz(s,kluczU).
klucz(y,kluczX).
klucz(w,kluczO).

% dany klucz Y otwiera drzwi z pokoju X
otwiera(b,kluczB).
otwiera(e,kluczE).
otwiera(i,kluczI).
otwiera(j,kluczJ).
otwiera(q,kluczQ).
otwiera(t,kluczT).
otwiera(u,kluczU).
otwiera(x,kluczX).
otwiera(o,kluczO).

% --- komunikaty ---

% wypisanie wiadomosci o przejsciu
komunikat_przejdz(A,B) :-
    format('[ przechodze z, ~w, do, ~w ]~n', [A, B]).

% wypisanie wiadomosci o wycofaniu sie z pokoju
komunikat_wyjdz(A) :-
    format('[ wychodze z, ~w ]~n', A).

% wypisanie wiadomosci o znalezieniu klucza
komunikat_klucz(A) :-
    format('[ znalazlem klucz, ~w ]~n', A).

% wypisanie wiadomosci o dotarciu do wyjscia
komunikat_koniec(A) :-
    format('[ dotarlem do wyjscia w ~w ]~n', A).

% --- wazne funkcje ---

% sprawdzenie czy drzwi z danego pokoju sa otwarte
otwarte(A) :-
    \+ otwiera(A,_).

% sprawdza czy drzwi nie zostaly zablokowane "tymczasowym kluczem"
tymczasowo_nie_zamkniete(A) :-
    \+ otwiera(A,tymczasowyKlucz).

% przejscie z pokoju A do B - jak otwarty lub jak juz znalezlismy klucz
przejdz(A,B) :-
    (   
    	drzwi(A,B);
        drzwi(B,A)
    ),
    otwarte(A),
    tymczasowo_nie_zamkniete(B),
    komunikat_przejdz(A,B).

% usuwamy drzwi - zeby sie nie zapetlac
drzwi_sprawdzone(A,B) :-
    retract(drzwi(A,B));
    retract(drzwi(B,A)).

% przywrocenie drzwi przy wycofaniu z pokoju
przywroc_drzwi(A,B) :-
    assert(drzwi(A,B)).

% czy pokoj A ma jakiekolwiek dostepne drzwi
ma_sasiada(A) :-
    drzwi(A,_);
    drzwi(_,A).

% sprawdzenie czy jest klucz w pokoju A
szukaj_klucza(A) :-
    (   
    	klucz(A,NOWY_KLUCZ),
    	NOWY_KLUCZ = _,
    	komunikat_klucz(NOWY_KLUCZ),
    	retract(klucz(A,NOWY_KLUCZ)),
    	retract(otwiera(_,NOWY_KLUCZ)),
        retractall(otwiera(_,tymczasowyKlucz))
    );
    true.

% tymczasowe zamkniecie wejscia do pokoju A
tymczasowo_zamknij(A) :-
    assert(otwiera(A,tymczasowyKlucz)).

% --- glowna funkcja rekurencyjnie szukajaca wyjscia ---

szukaj_wyjscia(POKOJ_POCZATKOWY,POKOJ_Z_KLUCZEM,KLUCZ,POKOJ_Z_WYJSCIEM) :-
    % czy dotarlismy do wyjscia
    POKOJ_POCZATKOWY == POKOJ_Z_WYJSCIEM ->  
    % tak
    komunikat_koniec(POKOJ_POCZATKOWY);
    % jeszcze nie
    (   
    	% wchodzimy do pokoju
    	(   
        	szukaj_klucza(POKOJ_POCZATKOWY),
    		przejdz(POKOJ_POCZATKOWY,NASTEPNY_POKOJ),
        	NASTEPNY_POKOJ \= POKOJ_POCZATKOWY,
            drzwi_sprawdzone(POKOJ_POCZATKOWY,NASTEPNY_POKOJ),
            szukaj_wyjscia(NASTEPNY_POKOJ,POKOJ_POCZATKOWY,KLUCZ,POKOJ_Z_WYJSCIEM)
    	);
    	% nie ma wyjscia lub jest jeszcze zamkniety
    	(   
        	(   
            	% jezeli ma sasiada = drzwi do niego sa zamkniete
        		ma_sasiada(POKOJ_POCZATKOWY) ->  
        		% to wtedy
        		(
                	% czy mozna juz do niego wejsc
                	(
                    	szukaj_klucza(POKOJ_POCZATKOWY),
                    	przejdz(POKOJ_POCZATKOWY,NOWY_POKOJ),
                        NOWY_POKOJ \= POKOJ_POCZATKOWY,
                    	drzwi_sprawdzone(POKOJ_POCZATKOWY,NOWY_POKOJ),
                        szukaj_wyjscia(NOWY_POKOJ,POKOJ_POCZATKOWY,KLUCZ,POKOJ_Z_WYJSCIEM)
                    );
                	% nie mozna wejsc - przywracamy zeby sie dalo potem tam przejsc
            		(   
                    	przywroc_drzwi(POKOJ_Z_KLUCZEM,POKOJ_POCZATKOWY),
                        % "zamyka" drzwi wejsciowe do pokoju zeby sie nie zapetlic
                        tymczasowo_zamknij(POKOJ_POCZATKOWY),
            			komunikat_wyjdz(POKOJ_POCZATKOWY),
            			fail
                    )
           		);
        		% jezeli nie ma sasiada - koniec korytarza
        		(
            		komunikat_wyjdz(POKOJ_POCZATKOWY),
            		fail
            	)
            )
        )
    ).