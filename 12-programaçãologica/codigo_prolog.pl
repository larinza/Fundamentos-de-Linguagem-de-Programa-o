homem(joao).
homem(pedro).
homem(carlos).
homem(antonio).
homem(bruno).
homem(daniel).

mulher(maria).
mulher(ana).
mulher(carla).
mulher(rita).
mulher(bia).

pai(joao, pedro).
pai(joao, ana).
pai(carlos, bia).
pai(antonio, bruno).
pai(pedro, daniel).

mae(maria, pedro).
mae(maria, ana).
mae(carla, bia).
mae(rita, bruno).
mae(ana, daniel).

genitor(X, Y) :- pai(X, Y).
genitor(X, Y) :- mae(X, Y).

filho(X, Y) :- genitor(Y, X), homem(X).
filha(X, Y) :- genitor(Y, X), mulher(X).

irmao(X, Y) :-
    genitor(Z, X),
    genitor(Z, Y),
    homem(X),
    X \= Y.

irma(X, Y) :-
    genitor(Z, X),
    genitor(Z, Y),
    mulher(X),
    X \= Y.

tio(X, Y) :-
    irmao(X, Z),
    genitor(Z, Y).

tia(X, Y) :-
    irma(X, Z),
    genitor(Z, Y).

avo(X, Y) :-
    genitor(X, Z),
    genitor(Z, Y).
