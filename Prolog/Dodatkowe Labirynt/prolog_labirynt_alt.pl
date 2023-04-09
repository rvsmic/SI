% oznaczenie ze bylismy juz w pokoju - zeby sie nie zapetlac
:- dynamic sprawdzony_pokoj/1.

drzwi(a,b).
drzwi(a,c).
drzwi(b,d).
drzwi(e,f).
drzwi(g,f).
drzwi(e,g).
drzwi(b,e).
drzwi(c,h).

klucz(h,kluczFrancuski).
klucz(c,kluczF).
klucz(e,kluczC).

otwiera(c,kluczC).
otwiera(f,kluczF).

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
przejdz(A,B) :-
    (   
    	drzwi(A,B);
    	drzwi(B,A)
    ),
    \+ sprawdzony_pokoj(B),
    komunikat_przejdz(A,B).

% szuka argumentow ktore dla danego pokoju poczatkowego beda wyjsciem
szukaj_wyjscia(POKOJ_POCZATKOWY,POKOJ_Z_KLUCZEM,KLUCZ,POKOJ_Z_WYJSCIEM) :-
    otwiera(POKOJ_Z_WYJSCIEM,KLUCZ),
    klucz(POKOJ_Z_KLUCZEM,KLUCZ),
    (   
    	szukaj_klucza(POKOJ_POCZATKOWY,POKOJ_Z_KLUCZEM,KLUCZ) ->
    	idz_do_wyjscia(POKOJ_Z_KLUCZEM,POKOJ_Z_WYJSCIEM)
    ).

szukaj_klucza(AKTUALNY_POKOJ,POKOJ_KLUCZ,KLUCZ) :-
    % czy doszlismy do pokoju z kluczem
    AKTUALNY_POKOJ == POKOJ_KLUCZ ->  
    (   
    	retractall(sprawdzony_pokoj(_)),
        komunikat_klucz(KLUCZ)
    );
    (
    	przejdz(AKTUALNY_POKOJ,NOWY_POKOJ),
    	NOWY_POKOJ \= AKTUALNY_POKOJ,
        assert(sprawdzony_pokoj(AKTUALNY_POKOJ)),
    	szukaj_klucza(NOWY_POKOJ,POKOJ_KLUCZ,KLUCZ);
    	komunikat_wyjdz(AKTUALNY_POKOJ),
        assert(sprawdzony_pokoj(AKTUALNY_POKOJ)),
        fail
    ).

idz_do_wyjscia(AKTUALNY_POKOJ,WYJSCIE) :-
    % czy doszlismy do wyjscia
    AKTUALNY_POKOJ == WYJSCIE -> 
    % tak
    (   
    	komunikat_koniec(WYJSCIE)
    );
    % jeszcze szukamy
    (
    	przejdz(AKTUALNY_POKOJ,NOWY_POKOJ),
    	NOWY_POKOJ \= AKTUALNY_POKOJ,
        assert(sprawdzony_pokoj(AKTUALNY_POKOJ)),
    	idz_do_wyjscia(NOWY_POKOJ,WYJSCIE);
    	komunikat_wyjdz(AKTUALNY_POKOJ),
        assert(sprawdzony_pokoj(AKTUALNY_POKOJ)),
        fail
    ).