/*
zad 1
A) rodzeństwo
B) kuzyn
C) wspołdziadkowie - nie znalazłem żadnej nazwy do takiej relacji
D) macocha
E) przyrodnie rodzenstwo
F) szwagier
G) wujek (brat rodzica) i przyrodnie rodzenstwo - dziwne_rodzenstwo

zad 2
*/

% ewa i adam to rodzice pabla i slawka
rodzic(pablo,ewa).
rodzic(pablo,adam).
rodzic(slawek,ewa).
rodzic(slawek,adam).

% pawel to rodzic magdy i roberta - magda to rodzic jozefa, a robert to rodzic czarka
rodzic(magda,pawel).
rodzic(robert,pawel).
rodzic(jozef,magda).
rodzic(czarek,robert).

% kamil to rodzic jurka, zbyszek to rodzic ady, jurek i ada to rodzice kuby
rodzic(jurek,kamil).
rodzic(ada,zbyszek).
rodzic(kuba,jurek).
rodzic(kuba,ada).

% staszek to rodzic michala i macka, joanna to rodzic macka
rodzic(michal,staszek).
rodzic(maciek,staszek).
rodzic(maciek,joanna).

% kasia to rodzic zuzi, emilka to rodzic krystiana, wojtek to rodzic zuzi i krystiana
rodzic(zuzia,kasia).
rodzic(krystian,emilka).
rodzic(zuzia,wojtek).
rodzic(krystian,wojtek).

% marcin i julia to rodzice stefana, daniel to rodzic julii i milosza
rodzic(stefan,marcin).
rodzic(stefan,julia).
rodzic(julia,daniel).
rodzic(milosz,daniel).

% roman to rodzic boguslawa i rafala, aneta to rodzic boguslawa i lucyny, lucyna to rodzic rafala
rodzic(boguslaw,roman).
rodzic(rafal,roman).
rodzic(boguslaw,aneta).
rodzic(lucyna,aneta).
rodzic(rafal,lucyna).

% dwie osoby ze wspolna dwojka rodzicow
rodzenstwo(X, Y) :-
    rodzic(X, A),
    rodzic(Y, A),
    rodzic(X, B),
    rodzic(Y, B),
    X \= Y,
    A \= X,
    A \= Y,
    B \= X,
    B \= Y,
    B \= A.

% dwie osoby ze wspolnym dziadkiem, ale roznymi rodzicami
kuzyn(X, Y) :-
    rodzic(A, C),
    rodzic(B, C),
    rodzic(X, A),
    rodzic(Y, B),
    A \= X,
    A \= Y,
    A \= B,
    A \= C,
    B \= X,
    B \= Y,
    B \= A,
    B \= C,
    C \= A,
    C \= B,
    C \= X,
    C \= Y,
    X \= Y.

% dziadkowie ze wspolnym wnukiem, ale dzieci nie sa wspolne
wspoldziadkowie(X, Y) :-
    rodzic(A, X),
    rodzic(B, Y),
    rodzic(C, A),
    rodzic(C, B),
    A \= X,
    A \= Y,
    A \= B,
    A \= C,
    B \= X,
    B \= Y,
    B \= A,
    B \= C,
    C \= A,
    C \= B,
    C \= X,
    C \= Y,
    X \= Y.

% rodzic x ma dziecko z y, ale y nie jest rodzicem x
macocha(X, Y) :-
    rodzic(X, A),
    rodzic(B, A),
    rodzic(B, Y),
    \+rodzic(X ,Y),
    \+rodzic(Y, X),
    A \= X,
    A \= Y,
    A \= B,
    B \= X,
    B \= Y,
    B \= A,
    X \= Y.

% x i y maja wspolnego tylko jednego rodzica
przyrodnie_rodzenstwo(X, Y) :-
    rodzic(X, A),
    rodzic(X, B),
    rodzic(Y, A),
    rodzic(Y, C),
    \+rodzic(X, C),
    \+rodzic(Y, B),
    A \= X,
    A \= Y,
    A \= B,
    A \= C,
    B \= X,
    B \= Y,
    B \= A,
    B \= C,
    C \= A,
    C \= B,
    C \= X,
    C \= Y,
    X \= Y.

% y jest rodzenstwem zony x - x ma dziecko z a, a ma wspolnego rodzica z y
szwagier(X, Y) :-
    (   
    	(   
        	rodzic(A, X),
    		rodzic(A, B),
    		rodzic(B, C),
    		rodzic(Y, C),
    		\+rodzic(A, C),
    		\+rodzic(C, A),
    		\+rodzic(X, Y),
   			\+rodzic(Y, X)
        );
    	(
        	rodzic(A, Y),
    		rodzic(A, B),
    		rodzic(B, C),
    		rodzic(X, C),
    		\+rodzic(A, C),
    		\+rodzic(C, A),
    		\+rodzic(X, Y),
   			\+rodzic(Y, X)
        )
    ),
    A \= X,
    A \= Y,
    A \= B,
    A \= C,
    B \= X,
    B \= Y,
    B \= A,
    B \= C,
    C \= A,
    C \= B,
    C \= X,
    C \= Y,
    X \= Y.

% x i y maja wspolnego rodzica, ale drugi rodzic y to syn drugiego rodzica x
dziwne_rodzenstwo(X, Y) :-
	rodzic(X, A),
    rodzic(X, B),
    rodzic(C, A),
    rodzic(Y, C),
    rodzic(Y, B),
    A \= X,
    A \= Y,
    A \= B,
    A \= C,
    B \= X,
    B \= Y,
    B \= A,
    B \= C,
    C \= A,
    C \= B,
    C \= X,
    C \= Y,
    X \= Y.
    