male(kartik).
male(oliver).
male(ali).
 male(dev).
male(simon).
male(harry).
female(avisha).
female(devanshi).
female(priyanka).
female(lily).
parent_of(kartik,priyanka).
parent_of(kartik,lily).
parent_of(avisha, priyanka).
parent_of(avisha, lily).
parent_of(oliver,dev).
parent_of(devanshi, dev).
parent_of(priyanka, simon).
parent_of(ali, simon).
parent_of(lily, harry).
parent_of(dev, harry).

% Rules
father_of(X,Y):- male(X),
 parent_of(X,Y).
mother_of(X,Y):- female(X),
 parent_of(X,Y).
grandfather_of(X,Y):- male(X),
 parent_of(X,Z),
 parent_of(Z,Y).
grandmother_of(X,Y):- female(X),
 parent_of(X,Z),
 parent_of(Z,Y).
ancestor_of(X,Y):- parent_of(X,Y).
ancestor_of(X,Y):- parent_of(X,Z),
 ancestor_of(Z,Y).
 
 %in output we have to write mother_of(Name1,Name2).
