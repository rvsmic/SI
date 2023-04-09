# Reprezentacja wiedzy w języku logiki

*Michał Rusinek*

Zadania wykonałem w formie tekstowej, ponieważ zupełnie nie widziałem sensownej możliwości rozwiązania ich w jezyku Prolog (można znaczną część przepisać, ale nie miałoby to sensu względem poleceń zadań).

## Zadanie 1

a)

### Stałe indywiduowe

- Markus
- Cezar

### Predykaty

- człowiek(x)
- pompejańczyk(x)
- rzymianin(x)
- władca(x)
- lojalny(x,y)
- nienawidzi(x,y)
- próba_zamachu(x,y)

### Stwierdzenia w języku predykatów

1. człowiek(Markus)
2. pompejańczyk(Markus)
3. $\forall$x ( pompejańczyk(x) $\rightarrow$ rzymianin(x) )
4. władca(Cezar)
5. $\forall$x ( rzymianin(x) $\rightarrow$ ( lojalny(x,Cezar) $\vee$ nienawidzi(x,Cezar) ) )
6. $\forall$x $\exists$y ( lojalny(x,y) )
7. $\forall$x $\forall$y ( (człowiek(x) $\wedge$ próba_zamachu(x,y) $\wedge$ władca(y) ) $\rightarrow$ $\neg$lojalny(x,y) )
8. próba_zamachu(Markus,Cezar)

*Odpowiedź na pytanie ze stopki:*
Zdanie z jęz. angielskiego można interpretować na dwa sposoby:

1. Ludzie, którzy dokonują zamachu na władcę, nie są wobec niego lojalni.
2. Ludzie, którzy nie są lojalni wobec władcy, podejmą próbę zamachu.

Moim zdaniem w tłumaczeniu została użyta interpretacja 1

b)

#### Czy Markus był lojalny wobec Cezara?

**Na bazie wyłącznie powyższych predykatów można jednoznacznie stwierdzić, że Markus nie był lojalny wobec Cezara.**

Wynika to z faktu iż:

$\neg$lojalny(Markus,Cezar)

co zgodnie z predykatem 7 wymaga udowodnienia:

- człowiek(Markus) - potwierdza to predykat 1
- próba_zamachu(Markus,Cezar) - potwierdza to predykat 7
- władca(Cezar) - potwierdza to predykat 4

Z tego powodu można jednoznacznie wywnioskować, że Markus nie był lojalny wobec Cezara, ponieważ był on człowiekiem, dokonał próby zamachu na Cezara, a Cezar był władcą.

c)

### Postać koniunkcyjna normalna CNF

1. człowiek(Markus)
2. pompejańczyk(Markus)
3. $\neg$pompejańczyk(x) $\vee$ rzymianin(x)
4. władca(Cezar)
5. $\neg$rzymianin(x) $\vee$ lojalny(x,Cezar) $\vee$ nienawidzi(x,Cezar)
6. lojalny(x,y)
7. $\neg$człowiek(x) $\vee$ $\neg$próba_zamachu(x,y) $\vee$ $\neg$władca(y) $\vee$ $\neg$lojalny(x,y)
8. próba_zamachu(Markus,Cezar)

d)

### Dowód b) metodą rezolucji

Chcemy udowodnić
**$\neg$lojalny(Markus,Cezar)**
więc negujemy ten predykat
$\neg$$\neg$lojalny(Markus,Cezar) $\leftrightarrow$ **lojalny(Markus,Cezar)**

A) $\neg$człowiek(Markus) $\vee$ $\neg$próba_zamachu(Markus,Cezar) $\vee$ $\neg$władca(Cezar) - rezolwenta klauzul 7 i negacji twierdzenia
B) $\neg$człowiek(Markus) $\vee$ $\neg$władca(Cezar) - rezolucja klauzul 8 i A
C) $\neg$władca(Cezar) - rezolucja klauzul 1 i B
D) $\Box$ - rezolucja klauzul 4 i C

## Zadanie 2

a)

1. $\forall$x( pożywienie(x) $\rightarrow$ lubi(Jan,x))
2. pożywienie(Jabłka)
3. pożywienie(Kurczak)
4. $\forall$x $\forall$y( ( je(x,y) $\wedge$ $\neg$zabija(y,x) ) $\rightarrow$ pożywienie(y) )
5. je(Adam,orzeszki) $\wedge$ żyje(Adam)
6. $\forall$x( je(Adam,x) $\rightarrow$ je(Basia,x) )

b)

### Postać koniunkcyjna normalna CNF

1. $\neg$pożywienie(x) $\vee$ lubi(Jan,x)
2. pożywienie(Jabłka)
3. pożywienie(Kurczak)
4. $\neg$je(x,y) $\vee$ zabija(y,x) $\vee$ pożywienie(y)
5. Koniunkcja więc rozdzielamy:
  a. je(Adam,orzeszki)
  b. żyje(Adam)
6. $\neg$je(Adam,x) $\vee$ je(Basia,x)

c)

### Dowód metodą rezolucji

Chcemy udowodnić
**lubi(Jan,orzeszki)**
więc negujemy ten predykat
**$\neg$lubi(Jan,orzeszki)**

Do przeprowadzenia dowodu brakuje tylko predykatu mówiącego, że jeżeli coś kogoś zabija to wtedy ten ktoś nie żyje:
7. $\forall$x $\forall$y( zabija(y,x) $\rightarrow$ $\neg$zyje(x)
czyli w CNF:
7. $\neg$zabija(y,x) $\vee$ $\neg$zyje(x)

Teraz można przeprowadzić dowód:

A) $\neg$je(x,y) $\vee$ $\neg$zyje(x) $\vee$ pożywienie(y) - rezolucja klauzul 7 i 4
B) pożywienie(orzeszki) $\vee$ $\neg$zyje(Adam) - rezolucja klauzul A i 5a
C) pożywienie(orzeszki) - rezolucja klauzul B i 5b
D) lubi(Jan,orzeszki) - rezolucja klauzul c i 1
E) $\Box$ - rezolucja klauzuli D i negacji twierdzenia

d)

### Jakie pożywienie je Basia (metodą rezolucji)

Metoda rezolucji służy dowodzeniu twierdzeń w logice, także aby określić jakie pożywienie je Basia, trzeba postawić tezę:
**je(Basia,orzeszki)**
którą negujemy:
**$\neg$je(Basia,orzeszki)**

A) je(Adam,orzeszki) - rezolucja klauzuli 6 i negacji twierdzenia
B) $\Box$ - rezolucja klauzuli A i 5a

Czyli można stwierdzić że Basia je orzeszki

Dla pozostałych stałych indywiduowych będących jedzeniem mamy za mało informacji, ponieważ nie jesteśmy w stanie określić czy Adam coś je poza orzeszkami, a do samej Basi nie mamy bezpośredniej informacji czy je coś innego.

## Zadanie 3

Z treści zadania 3 i zadania 1 można wyciągnąć następujące predykaty (z 1 wybrałem tylko adekwatne do tego zadania):

1. człowiek(Markus)
2. pompejańczyk(Markus)
3. urodzony(Markus,40)
4. wybuch(Wezuwiusz,79)
5. $\forall$x ( ( pompejańczyk(x) $\wedge$ wybuch(Wezuwiusz,79) ) $\rightarrow$ umarł(x,79) )
6. $\forall$x $\forall$t1 $\forall$t2 ( ( człowiek(x) $\wedge$ urodzony(x,t1) $\wedge$ większe(t2 - t1,150) ) $\rightarrow$ $\neg$żyje(x) )
7. teraz(2021)

Jako że zakładamy, że mamy teraz rok 2021 na zdrowy rozsądek można stwierdzić, że **Markus nie żyje**.

Udowodnię to metodą rezolucji:
Jako tezę przyjmiemy
**$\neg$żyje(Markus)**
co zanegujemy do
**żyje(Markus)**

Jako że w powyższych predykatach brakuje nam predykatu *żyje*, musimy dodać parę predykatów:

8. $\forall$x $\forall$t umarł(x,t) $\rightarrow$ $\neg$żyje(x)
9. $\forall$x $\forall$t1 $\forall$t2 ( ( umarł(x,t1) $\wedge$ większe(t2,t1) ) $\rightarrow$ $\neg$żyje(x) )

Teraz już możemy przystąpić do dowodu:

Zamieniamy predykaty na postać CNF:

1. człowiek(Markus)
2. pompejańczyk(Markus)
3. urodzony(Markus,40)
4. wybuch(Wezuwiusz,79)
5. $\neg$pompejańczyk(x) $\vee$ $\neg$wybuch(Wezuwiusz,79) $\vee$ umarł(x,79)
6. $\neg$człowiek(x) $\vee$ $\neg$urodzony(x,t1) $\vee$ $\neg$większe(t2 - t1,150) $\vee$ $\neg$żyje(x)
7. teraz(2021)
8. $\neg$umarł(x,t) $\vee$ $\neg$żyje(x)
9. $\neg$umarł(x,t1) $\vee$ $\neg$większe(t2,t1) $\vee$ $\neg$żyje(x)

Możemy to wykazać na 2 sposoby:

### I sposób

Wskazujemy na pochodzenie Markusa

A) $\neg$umarł(Markus,t) - rezolucja klauzuli 8 i negacji twierdzenia
B) $\neg$pompejańczyk(Markus) $\vee$ $\neg$wybuch(Wezuwiusz,79) - rezolucja klauzul A i 5
C) $\neg$pompejańczyk(Markus) - rezolucja klauzul B i 4
D) $\Box$ - rezolucja klauzul C i 2

Czyli skoro Markus był Pompejańczykiem, to musiał umrzeć podczas wybuchu Wezuwiusza, która zabiła wszystkich.

### II sposób

Wskazujemy na aktualny rok i żywotność ludzi

AA) $\neg$człowiek(x) $\vee$ $\neg$urodzony(x,t1) $\vee$ $\neg$większe(2021 - t1,150) - rezolucja klauzuli 6 i negacji twierdzenia
BB) $\neg$człowiek(x) $\vee$ $\neg$większe(1981,150) - rezolucja klauzul AA i 3
CC) $\neg$większe(1981,150) - rezolucja klauzul BB i 1
DD) $\neg$umarł(x,40) $\vee$ $\neg$żyje(x) - rezolucja klauzul CC i 9
EE) $\Box$ - rezolucja klauzul DD i 8

Czyli skoro Markus urodził się w roku 40, a żaden człowiek nie żył więcej niż 150 lat, to w 2021 Markus nie żyje.