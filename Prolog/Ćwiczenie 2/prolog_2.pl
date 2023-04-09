% schemat drzewa genealogicznego ktore przygotowalem do tego zadania
% w pliku pdf "Drzewo genealogiczne zad 2.pdf"
osoba(slawek).
osoba(ewa).
osoba(magda).
osoba(kamil).
osoba(oliwia).
osoba(wojtek).
osoba(julia).
osoba(krzysiek).
osoba(mieszko).
osoba(ala).
osoba(zbyszko).
osoba(wladek).
osoba(wanda).
osoba(jurek).
osoba(daniel).
osoba(pola).
osoba(michal).
osoba(zuzia).
osoba(adam).
osoba(emilia).
osoba(kacper).
osoba(pablo).
osoba(ola).
osoba(agata).
osoba(jagoda).
osoba(rysiek).
osoba(robert).

%rodzic(X,Y) - Y jest rodzicem X
rodzic(mieszko,krzysiek).
rodzic(mieszko,ala).
rodzic(zbyszko,ala).
rodzic(zbyszko,wladek).
rodzic(krzysiek,wojtek).
rodzic(krzysiek,julia).
rodzic(wojtek,kamil).
rodzic(wojtek,magda).
rodzic(oliwia,kamil).
rodzic(oliwia,magda).
rodzic(magda,slawek).
rodzic(magda,ewa).
rodzic(ala,wanda).
rodzic(ala,jurek).
rodzic(jurek,daniel).
rodzic(jurek,zuzia).
rodzic(daniel,pola).
rodzic(daniel,michal).
rodzic(zuzia,adam).
rodzic(zuzia,emilia).
rodzic(kacper,zuzia).
rodzic(kacper,pablo).
rodzic(ola,zuzia).
rodzic(ola,pablo).
rodzic(jagoda,agata).
rodzic(jagoda,kacper).
rodzic(robert,ola).
rodzic(robert,rysiek).

mezczyzna(slawek).
mezczyzna(kamil).
mezczyzna(wojtek).
mezczyzna(krzysiek).
mezczyzna(mieszko).
mezczyzna(michal).
mezczyzna(daniel).
mezczyzna(adam).
mezczyzna(pablo).
mezczyzna(jurek).
mezczyzna(kacper).
mezczyzna(wladek).
mezczyzna(zbyszko).
mezczyzna(rysiek).
mezczyzna(robert).

% 1
kobieta(X):-
    osoba(X),
    \+mezczyzna(X).

% 2 - X jest ojcem Y
ojciec(X,Y):-
    osoba(X),
    osoba(Y),
    mezczyzna(X),
    rodzic(Y,X),
    X \= Y.

% 3 - X jest matką Y
matka(X,Y):-
    osoba(X),
    osoba(Y),
    kobieta(X),
    rodzic(Y,X),
    X \= Y.

% 4 - X jest córką Y
corka(X,Y):-
    osoba(X),
    osoba(Y),
    kobieta(X),
    rodzic(X,Y),
    X \= Y.

% 5 - X jest rodzonym bratem Y
brat_rodzony(X,Y):-
    mezczyzna(X),
    ojciec(A,X),
    ojciec(A,Y),
    matka(B,X),
    matka(B,Y),
    X \= Y,
    A \= B,
    A \= X,
    A \= Y,
    B \= X,
    B \= Y.

% 6 - X jest przyrodnim bratem Y
brat_przyrodni(X,Y):- 
    mezczyzna(X),
    rodzic(X,A),
    rodzic(Y,A),
    rodzic(Y,B),
    \+brat_rodzony(X,Y),
    X \= Y,
    A \= B,
    A \= X,
    A \= Y,
	B \= X,
    B \= Y.

% 7 - X jest kuzynem Y
kuzyn(X,Y):-
    mezczyzna(X),
    rodzic(X,A),
    rodzic(A,B),
    rodzic(C,B),
    rodzic(Y,C),
    X \= Y,
	A \= B,
    A \= C,
    A \= X,
	A \= Y,
    B \= X,
	B \= Y,
    B \= C.

% 8 - X jest dziadkiem od strony ojca dla Y
dziadek_od_strony_ojca(X,Y):-
    ojciec(A,Y),
    ojciec(X,A),
    X \= Y,
    A \= X,
	A \= Y.

% 9 - X jest dziadkiem od strony matki dla Y
dziadek_od_strony_matki(X,Y):-
    matka(A,Y),
    ojciec(X,A),
    X \= Y,
    A \= X,
	A \= Y.

% 10 - X jest dziadkiem Y
dziadek(X,Y):-
    dziadek_od_strony_ojca(X,Y);
    dziadek_od_strony_matki(X,Y).

% 11 - X jest babcią Y
babcia(X,Y):-
    osoba(Y),
    rodzic(Y,A),
    matka(X,A),
    X \= Y,
    A \= X,
	A \= Y.

% 12 - Y jest wnuczką X
wnuczka(X,Y):-
    kobieta(Y),
    (   
    	dziadek(X,Y);
    	babcia(X,Y)
    ).

% 13 - X jest przodkiem Y do drugiego pokolenia wstecz
przodek_do2pokolenia_wstecz(X,Y):-
    osoba(X),
    osoba(Y),
	(   
    	rodzic(Y,X);
    	dziadek(X,Y);
    	babcia(X,Y)
    ),
    X \= Y.

% 14 - X jest przodkiem Y do trzeciego pokolenia wstecz
przodek_do3pokolenia_wstecz(X,Y):-
	przodek_do2pokolenia_wstecz(X,Y);
    (   
    	rodzic(Y,A),
        A \= X,
        A \= Y,
        X \= Y,
    	(
        	dziadek(X,A);
        	babcia(X,A)
        )
    ).
    